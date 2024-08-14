from flask import Flask, render_template, request
import requests
import smtplib
app = Flask(__name__, template_folder='template')
post = "https://api.npoint.io/5808b1a3304a496f4c65"
all_post = requests.get(post).json()
g_email = "forvideos619@gmail.com"
password = "gamerfunky619"


@app.route('/')
@app.route('/index.html')
def home():
    return render_template("index.html", all_post=all_post)


@app.route("/about.html")
def about():
    return render_template("about.html")


@app.route("/contact.html", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])

        send_mail(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


@app.route("/post/<int:blog_id>")
def new_post(blog_id):
    return render_template("post.html", blog_id=blog_id, all_post=all_post)


@app.route("/form-entry", methods=["POST", "GET"])
def receive_data():
    if request.method == "POST":
        data = request.form

        print(
            f"Name: {data['name']}\nEmail: {data['email']}\nPhone: {data['phone']}\nMessage: {data['message']}")

        return "<h1>The Message Was Sent Successfully</h1>"


def send_mail(name, email, phone, message):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"

        connection.starttls()
        connection.login(g_email, password=password)
        connection.sendmail(from_addr=g_email, to_addrs="gamerfunky619@gmail.com",
                            msg=email_message)


if __name__ == '__main__':
    app.run(debug=True)
