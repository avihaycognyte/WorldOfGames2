import os
import platform

# A string representing a file name. By default “Scores.txt”
SCORES_FILE_NAME = "Scores.txt"

# A number representing a bad return code for a function
BAD_RETURN_CODE = -1

# A function to clear the screen (useful when playing memory game or before a new game starts)
def screen_cleaner():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
