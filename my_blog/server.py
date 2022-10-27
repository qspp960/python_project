from flask import Flask,render_template
from datetime import datetime
import requests


app = Flask(__name__)

@app.route("/")
def main_page():
    today = datetime.today()
    today_year = today.year
    return render_template('index.html',today_year = today_year)

@app.route("/guess/<name>")
def gender_guess_page(name):
    response = requests.get(url=f'https://api.genderize.io?name={name}')
    gender_data = response.json()
    your_name = gender_data['name']
    your_gender = gender_data['gender']

    return render_template('index.html',name=your_name,gender=your_gender)



if __name__ == "__main__":
    app.run(debug=True)