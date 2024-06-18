import requests
from bs4 import BeautifulSoup
import sys

def test_scores_service(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        soup = BeautifulSoup(response.text, 'html.parser')
        score_element = soup.find(id="score")

        if score_element and score_element.text.isdigit():
            score = int(score_element.text)
            if 1 <= score <= 1000:
                return True
            else:
                print(f"Score out of range: {score}")
                return False
        else:
            print("Score element not found or not a digit.")
            return False
    except requests.RequestException as e:
        print(f"Error testing scores service: {e}")
        return False

def main():
    url = "http://127.0.0.1:8777"  # Updated URL to match the exposed port
    if test_scores_service(url):
        print("Test passed.")
        sys.exit(0)
    else:
        print("Test failed.")
        sys.exit(-1)

if __name__ == "__main__":
    main()
