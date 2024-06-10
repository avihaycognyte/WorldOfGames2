import random
import time
import os
import platform
from Score import add_score  # Import add_score function

class GuessGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.secret_number = None

    def generate_number(self):
        self.secret_number = random.randint(1, self.difficulty)

    def get_guess_from_user(self):
        while True:
            try:
                guess = int(input(f"What is your guess number from 1 to {self.difficulty}: "))
                if 1 <= guess <= self.difficulty:
                    return guess
                else:
                    print(f"Please enter a number between 1 and {self.difficulty}.")
            except ValueError:
                print("Invalid input. Please enter an integer.")

    def compare_results(self, guess):
        return guess == self.secret_number

    def clear_screen(self):
        # Clear the screen based on the OS
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")

    def play(self):
        self.generate_number()
        print(f"Remember this number: {self.secret_number}")
        time.sleep(0.7)
        self.clear_screen()
        guess = self.get_guess_from_user()
        if self.compare_results(guess):
            print("Congratulations! You guessed the correct number.")
            add_score(self.difficulty)  # Update score on winning
            return True
        else:
            print(f"Sorry, the correct number was {self.secret_number}. Better luck next time!")
            return False
