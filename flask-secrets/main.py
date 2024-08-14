from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, Length
from flask_bootstrap import Bootstrap


class LoginForm(FlaskForm):
    email = StringField(label='Email: ', validators=[InputRequired(), Email(
        check_deliverability=True), Length(min=8, max=25)], render_kw={'style': 'width:30ch'})
    password = PasswordField(label='Password: ', validators=[
                             InputRequired(), Length(min=8, max=16)], render_kw={'style': 'width:30ch'})
    submit = SubmitField(label="Log In", render_kw={'btn-primary': 'True'})


app = Flask(__name__)
Bootstrap(app)
app.secret_key = "raktim_das_619"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")

    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
