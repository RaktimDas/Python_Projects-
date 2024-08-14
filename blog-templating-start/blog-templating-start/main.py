from flask import Flask, render_template
import requests
BLOG_URL = " https://api.npoint.io/ed99320662742443cc5b"

app = Flask(__name__)


@app.route('/')
def home():
    blog_response = requests.get(BLOG_URL)
    blog_index = blog_response.json()
    return render_template("index.html", blog_index=blog_index)


@app.route("/post/<int:blog_id>")
def show_post(blog_id):
    blog_response = requests.get(BLOG_URL)
    blog_post = blog_response.json()
    return render_template("post.html", blog_post=blog_post, blog_id=blog_id)


if __name__ == "__main__":
    app.run(debug=True)
