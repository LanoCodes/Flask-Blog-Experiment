from flask import Flask, render_template
import requests

app = Flask(__name__)

blog_posts = requests.get('https://api.npoint.io/6b9672689b45fc078daa').json()


@app.route('/')
def home():
    return render_template(
        'index.html',
        all_posts=blog_posts
    )


@app.route('/about')
def about():
    return render_template(
        'about.html'
    )


@app.route('/contact')
def contact():
    return render_template(
        'contact.html'
    )


@app.route('/post/<int:post_id>')
def post(post_id):
    post_id -= 1
    return render_template(
        'post.html',
        post=blog_posts[post_id]
    )


if __name__ == '__main__':
    app.run(debug=True)
