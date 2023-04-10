import random

def generate_code():
    return random.sample(range(1, 10), 4)

def get_feedback(guess, code):
    correct_digits = sum([1 for g, c in zip(guess, code) if g == c])
    common_digits = sum([1 for g in guess if g in code])
    return common_digits, correct_digits

def play_game():
    code = generate_code()
    attempts = 0

    print("Welcome to the 'Guess the Number' game!")
    print("Try to guess the 4-digit code with unique digits (1-9).")
    print("I will provide feedback after each attempt:")
    print("The first number will represent the count of digits in your guess that are in the code.")
    print("The second number will represent the count of digits in your guess that are both in the code and in the correct position.")

    while True:
        user_input = input("Enter your 4-digit guess (unique digits from 1-9): ")
        if len(user_input) != 4 or not user_input.isdigit() or len(set(user_input)) != 4 or '0' in user_input:
            print("Invalid input. Please enter a 4-digit code with unique digits from 1-9.")
            continue

        guess = [int(digit) for digit in user_input]
        attempts += 1
        common_digits, correct_digits = get_feedback(guess, code)

        if correct_digits == 4:
            print(f"Congratulations! You guessed the code {user_input} in {attempts} attempts.")
            break
        else:
            print(f"Feedback: {common_digits} digits in the code, {correct_digits} digits in the correct position.")

if __name__ == "__main__":
    play_game()