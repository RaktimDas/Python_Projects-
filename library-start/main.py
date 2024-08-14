"""Note This is a Practice Project Using Flask Framework
    There Might Be Some Erros in the code or in your system provided system and the database.
    Please Don't Concede to the errors it modify the code and make it run it will run.
    Be carefull using the database.
"""
#Importing The Required Modules.
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

# Creating the Flask App.
app = Flask(__name__)
#Declaring The SQL Database and It's URL.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Using Bootstrap To Style The UI.
Bootstrap(app)
# Inhereting the Falsk app Through SQLAlChmy.
db = SQLAlchemy(app)

#Declaring a Predefined Class Called Model and Creating the Table.
#The Table Consist of id, title, author and rating.
#The id is integer and has primary key which is unique.
#The title is integer and max character of 250 characters it's unique and cannot be empty same goes for author but it works if it's not unique.
#The rating is float and it's not unique and it cannot be null.
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), unique=False, nullable=False)
    rating = db.Column(db.Float, unique=False, nullable=False)
#This is special function represents the title of book as class object string.
    def __repr__(self):
        return f"<Books {self.title}"

#Finally we use this function to create the above table and it's required parameter.
db.create_all()

#The Route for the home page and reading all the entries in all_books and inserting in the index page.
@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template("index.html", books=all_books)

#This route is used to add the required data i.e the Title--Author--Rating and finally Submit it.
#After The Submission the Inputs get rendered into the Home page to be viewed
#we get redirected to the home page and also the input  gets updated or inserted in the database.
#Post method is used in most cases as we are inputing are data and not getting it.
@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        new_book = Book(
            title=request.form["title"],
            author=request.form["author"],
            rating=request.form["rating"]
        )

        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("add.html")

#This route is specifically made tp edit the rating of the book.
#Using the form function we get the id of the updateable table.
#We use SQLAlchemy methods to update the database.
# https://www.sqlalchemy.org/
#All the Details Will be Found in The SQLAlchemy Documentations.
#After the update process get's redirected to home page.
#The id is requested as args and get rendered along the edit.html page.
@app.route("/edit", methods=['GET', 'POST'])
def edit():
    if request.method == "POST":
        book_id = request.form['id']
        book_to_update = Book.query.get(book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = Book.query.get(book_id)
    return render_template("edit.html", book=book_selected)

#This route is used for deleting records in the home page as well the database.
#The id is requested as args and deleted by user choice as inputed.
# After that it get's redirected to home page. 
@app.route("/delete", methods=["POST", "GET"])
def delete():

    book_id = request.args.get('id')
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

#Using the name attribute to run and activate the debug mode.
if __name__ == "__main__":
    app.run(debug=True)
