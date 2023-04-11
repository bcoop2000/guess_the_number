from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

def generate_code():
    return random.sample(range(1, 10), 4)

def get_feedback(guess, code):
    correct_digits = sum([1 for g, c in zip(guess, code) if g == c])
    common_digits = sum([1 for g in guess if g in code])
    return common_digits, correct_digits

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'code' not in session or request.form.get('reset'):
        session['code'] = generate_code()
        session['attempts'] = 0

    if 'previous_guesses' not in session:
        session['previous_guesses'] = []

    feedback = None
    game_over = False
    if request.method == 'POST' and not request.form.get('reset'):
        user_input = request.form.get('guess')

        if len(user_input) != 4 or not user_input.isdigit() or len(set(user_input)) != 4 or '0' in user_input:
            feedback = "Invalid input. Please enter a 4-digit code with unique digits from 1-9."
        else:
            guess = [int(digit) for digit in user_input]
            session['attempts'] += 1
            common_digits, correct_digits = get_feedback(guess, session['code'])

            session['previous_guesses'].append((user_input, common_digits, correct_digits))

            if correct_digits == 4:
                feedback = f"Congratulations! You guessed the code {user_input} in {session['attempts']} attempts."
                game_over = True
            else:
                feedback = f"Feedback: {common_digits} digits in the code, {correct_digits} digits in the correct position."

    return render_template('index.html', feedback=feedback, attempts=session.get('attempts', 0),
                           previous_guesses=session.get('previous_guesses', []), game_over=game_over)

if __name__ == '__main__':
    app.run(debug=True)