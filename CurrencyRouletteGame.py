import random
import requests
from Score import add_score  # Import add_score function

class CurrencyRouletteGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.api_url = "https://api.exchangerate-api.com/v4/latest/USD"  # Example API endpoint

    def get_exchange_rate(self):
        try:
            response = requests.get(self.api_url, verify=False)  # Disable SSL verification
            response.raise_for_status()
            data = response.json()
            return data['rates']['ILS']
        except requests.RequestException as e:
            print(f"Error fetching exchange rate: {e}")
            return None

    def get_money_interval(self, usd_amount, rate):
        margin = 5 - self.difficulty
        total_value = usd_amount * rate
        lower_bound = total_value - margin
        upper_bound = total_value + margin
        return lower_bound, upper_bound

    def get_guess_from_user(self, usd_amount):
        guess = float(input(f"Guess the value of {usd_amount} USD in ILS: "))
        return guess

    def play(self):
        exchange_rate = self.get_exchange_rate()
        if exchange_rate is None:
            print("Unable to fetch exchange rate. Please try again later.")
            return False

        usd_amount = random.randint(1, 100)
        lower_bound, upper_bound = self.get_money_interval(usd_amount, exchange_rate)

        user_guess = self.get_guess_from_user(usd_amount)

        if lower_bound <= user_guess <= upper_bound:
            print(f"Congratulations! Your guess is correct. The value was between {lower_bound:.2f} and {upper_bound:.2f}.")
            add_score(self.difficulty)  # Update score on winning
            return True
        else:
            print(f"Sorry, your guess was incorrect. The correct value was between {lower_bound:.2f} and {upper_bound:.2f}.")
            return False
