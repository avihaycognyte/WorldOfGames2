import random
import time
from Utils import screen_cleaner  # Import the screen_cleaner function
from Score import add_score  # Import add_score function

class MemoryGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def generate_sequence(self):
        sequence = [random.randint(1, 101) for _ in range(self.difficulty)]
        return sequence

    def get_list_from_user(self):
        while True:
            try:
                user_input = input(f"Enter the {self.difficulty} numbers you remember, separated by spaces: ")
                user_list = list(map(int, user_input.split()))
                if len(user_list) != self.difficulty:
                    print(f"Please enter exactly {self.difficulty} numbers.")
                else:
                    return user_list
            except ValueError:
                print("Invalid input. Please enter numbers only.")

    def is_list_equal(self, list1, list2):
        return list1 == list2

    def play(self):
        sequence = self.generate_sequence()
        print(f"Remember this sequence: {sequence}")
        time.sleep(0.7)
        screen_cleaner()  # Use the screen_cleaner function
        user_sequence = self.get_list_from_user()
        if self.is_list_equal(sequence, user_sequence):
            print("Congratulations! You remembered all the numbers correctly.")
            add_score(self.difficulty)  # Update score on winning
            return True
        else:
            print(f"Sorry, the correct sequence was {sequence}. Better luck next time!")
            return False
