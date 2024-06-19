from Utils import screen_cleaner
from Score import add_score  # Import add_score function

def welcome(name):
    msg = f"""
    Hello {name} and welcome to the World of Games (WoG).
    Here you can find many cool games to play.
    """
    return msg

def load_game():
    while True:
        msg = """
        Please choose a game to play:
        1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
        2. Guess Game - guess a number and see if you chose like the computer
        3. Currency Roulette - try and guess the value of a random amount of USD in ILS
        """
        try:
            game = int(input(msg))
            if game < 1 or game > 3:
                print("Invalid choice. Please choose a valid game number.")
                continue

            diff = int(input("Please choose game difficulty from 1 to 5: "))
            if diff < 1 or diff > 5:
                print("Invalid difficulty level. Please choose a difficulty from 1 to 5.")
                continue

            game_won = False
            if game == 1:
                from MemoryGame import MemoryGame
                game_instance = MemoryGame(diff)
                game_won = game_instance.play()
            elif game == 2:
                from GuessGame import GuessGame
                game_instance = GuessGame(diff)
                game_won = game_instance.play()
            elif game == 3:
                from CurrencyRouletteGame import CurrencyRouletteGame
                game_instance = CurrencyRouletteGame(diff)
                game_won = game_instance.play()

            if game_won:
                add_score(diff)

            break  # Exit the loop after a successful game session
        except ValueError:
            print("Invalid input. Please enter numbers only.")
        screen_cleaner()
