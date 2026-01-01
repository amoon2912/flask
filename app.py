from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Game variables
number = random.randint(1, 100)
guesses = 0
message = "Guess a number between 1 and 100 🎯"

@app.route("/", methods=["GET", "POST"])
def home():
    global number, guesses, message

    if request.method == "POST":
        guess = int(request.form["guess"])
        guesses += 1

        if guess > number:
            message = "📉 Lower number please!"
        elif guess < number:
            message = "📈 Higher number please!"
        else:
            message = f"🎉 Correct! You guessed it in {guesses} tries!"
            number = random.randint(1, 100)
            guesses = 0

    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
