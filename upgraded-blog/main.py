from flask import Flask, render_template
import requests

POST_API_URL = 'https://api.npoint.io/5a9a97267b128ec41bd8'
response = requests.get(url=POST_API_URL)
post_data = response.json()

app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template('index.html',post_data=post_data)

@app.route("/contact")
def contact_page():
    return render_template('contact.html')

@app.route("/about")
def about_page():
    return render_template('about.html')

@app.route("/post/<int:post_id>")
def post_page(post_id):
    return render_template('post.html',post_data=post_data[post_id-1])





if __name__ == "__main__":
    app.run(debug=True)