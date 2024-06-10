import os
from Utils import SCORES_FILE_NAME, BAD_RETURN_CODE


# Points calculation formula
def calculate_points(difficulty):
    return (difficulty * 3) + 5


# Add score function
def add_score(difficulty):
    points_to_add = calculate_points(difficulty)

    try:
        # Try to read the current score from the file
        if os.path.exists(SCORES_FILE_NAME):
            with open(SCORES_FILE_NAME, 'r') as file:
                current_score = int(file.read())
        else:
            current_score = 0

        # Add the new points to the current score
        new_score = current_score + points_to_add

        # Save the new score back to the file
        with open(SCORES_FILE_NAME, 'w') as file:
            file.write(str(new_score))
    except (IOError, ValueError) as e:
        print(f"Error managing the score file: {e}")
        return BAD_RETURN_CODE

    return new_score
