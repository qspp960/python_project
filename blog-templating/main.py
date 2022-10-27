from flask import Flask, render_template
from post import Post

app = Flask(__name__)
post = Post()
blog_data = post.get_blog_data()


@app.route('/')
def home():
    return render_template("index.html",blog_post=blog_data)

@app.route('/post/<int:blog_id>')
def read_blog_post(blog_id):
    current_blog_data = post.find_id_blog_data(blog_id)
    return render_template("post.html",blog_post=current_blog_data)


if __name__ == "__main__":
    app.run(debug=True)
