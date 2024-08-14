from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-movies-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
db = SQLAlchemy(app)
api_key = "ccca76edc681646cde88f545f100e10c"

MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(400), unique=True, nullable=True)
    year = db.Column(db.Integer, unique=False, nullable=True)
    description = db.Column(db.String(600), unique=False, nullable=True)
    rating = db.Column(db.Float, unique=False, nullable=True)
    ranking = db.Column(db.Integer, unique=True, nullable=True)
    review = db.Column(db.String(500), unique=False, nullable=True)
    img_url = db.Column(db.String, unique=True, nullable=True)

    def __repr__(self):
        return f"Movies {self.title}"


db.create_all()


class RateMovieForm(FlaskForm):
    rating = StringField(
        label='Your Rating Out Of 10 e.g. 7.5', validators=[DataRequired()])
    review = StringField(label='Your Review', validators=[DataRequired()])
    submit = SubmitField(label='Submit')


class AddMovie(FlaskForm):
    title = StringField(label="Movie Title", validators=[DataRequired()])
    submit = SubmitField(label="Add Movie")


@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route('/edit', methods=['POST', 'GET'])
def edit():
    my_forms = RateMovieForm()
    movie_id = request.args.get('id')
    movie_to_update = Movie.query.get(movie_id)
    if my_forms.validate_on_submit():
        print("Rate Form Validation Successfull")
        movie_to_update.rating = float(my_forms.rating.data)
        movie_to_update.review = my_forms.review.data
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('edit.html', form=my_forms, movie=movie_to_update)


@app.route("/delete", methods=['POST', 'GET'])
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/add', methods=['POST', 'GET'])
def add():
    my_form = AddMovie()
    movie_search = my_form.title.data

    if my_form.validate_on_submit():
        print("Add Form Validation Successfull")

        params = {
            "api_key": api_key,
            "query": movie_search,

        }
        response_text = requests.get(MOVIE_DB_SEARCH_URL, params=params)
        data = response_text.json()["results"]

        return render_template("select.html", options=data)
    return render_template("add.html", form=my_form)


@app.route("/find")
def find():
    movie_api_id = request.args.get('id')
    if movie_api_id:
        movie_api_url = f"{MOVIE_DB_INFO_URL}/{movie_api_id}"
        response = requests.get(movie_api_url, params={"api_key": api_key})
        data = response.json()
        new_movie = Movie(
            title=data['title'],
            img_url=f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
            year=data["release_date"].split("_")[0],
            description=data["overview"]

        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('edit'))


if __name__ == '__main__':
    app.run(debug=True)
