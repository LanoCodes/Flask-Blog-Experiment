from flask import Flask, render_template, request
import requests, smtplib
from email.message import EmailMessage

posts = requests.get('YOUR POST API URL HERE').json()

app = Flask(__name__)

my_email = "YOUR EMAIL HERE"
email_pass = "YOUR EMAIL/APP PASSWORD HERE"


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template(
        "about.html"
    )

@app.route("/contact", methods=['POST', 'GET'])
def contact():
    if request.method == 'GET':
        return render_template(
        "contact.html"
        )
    else:
        msg = EmailMessage()
        msg['Subject'] = "Blog Testing"
        msg['From'] = my_email
        msg['To'] = "lanoforcoding@yahoo.com"
        msg.set_content(f'Testing WORKS!\n'
                        f'Name: {request.form["name"]}\n'
                        f'Email: {request.form["email"]}\n'
                        f'Phone: {request.form["phone"]}\n'
                        f'Message: {request.form["message"]}')
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=email_pass)
            connection.send_message(msg)
        return render_template(
            'details.html'
        )

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template(
        "post.html",
        post=requested_post
    )


if __name__ == "__main__":
    app.run(debug=True, port=5001)