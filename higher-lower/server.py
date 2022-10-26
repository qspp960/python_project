from flask import Flask
import random

app = Flask(__name__)
random_number = random.randint(1,3)


@app.route("/")
def main_page():
    return "<h1>Guess the number</h1>"

@app.route("/<int:number>")
def guess_number_page(number):
    if number > random_number:
        return "<p>too high</p>"
    elif number < random_number:
        return "<p>too low</p>"
    else:
        return "<p>Good</p>"


if __name__ == "__main__":
    app.run(debug=True)
