from flask import Flask
import random
app = Flask(__name__)
random_number = random.randint(0, 9)


@app.route("/")
def number():
    return "<h1>'Guess a number between 0 and 9'</h1>"\
        "<img src= 'https://media2.giphy.com/media/6znpHNXfBQJnSWhwmm/giphy.gif?cid=ecf05e47cbfcc605d8a5b5e2e49f6595ff36f7d2e72eb9fa&rid=giphy.gif&ct=g',alt='dog'> "\



@app.route("/<int:usernumber>")
def check_number(usernumber):
    if usernumber > random_number:
        return f"{usernumber} is too high:"\
            "<h1 style=color:red;>Too high, try again!"\
            "<img src=  'https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif',alt=high> "

    elif usernumber < random_number:
        return f"{usernumber} is too low:"\
            "<h1 style=color:blue;>Too low, try again!"\
            "<img src = 'https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif',alt=low> "\

    else:
        return f"{usernumber} is correct:"\
            "<h1 style=color:green;>You found me!</h1>"\
            "<img src= 'https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif',alt= 'correct'>"


if __name__ == "__main__":
    app.run(debug=True)
