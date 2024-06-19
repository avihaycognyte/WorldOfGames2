from flask import Flask, render_template_string
from Utils import SCORES_FILE_NAME, BAD_RETURN_CODE

app = Flask(__name__)

@app.route('/')
def score_server():
    try:
        with open(SCORES_FILE_NAME, 'r') as file:
            score = file.read()
        score_html = f"""
        <html>
        <head>
        <title>Scores Game</title>
        </head>
        <body>
        <h1>The score is <div id="score">{score}</div></h1>
        </body>
        </html>
        """
        return render_template_string(score_html)
    except Exception as e:
        print(f"Error reading score file: {e}")
        error_html = f"""
        <html>
        <head>
        <title>Scores Game</title>
        </head>
        <body>
        <h1><div id="score" style="color:red">{BAD_RETURN_CODE}</div></h1>
        </body>
        </html>
        """
        return render_template_string(error_html)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
