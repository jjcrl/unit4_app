#18.134.6.18
from flask import Flask, render_template,request,redirect,jsonify
from lib.database_connection import DatabaseConnection
from lib.book_repository import BookRepository
from lib.book import Book
from lib.user import User
from lib.user_repository import UserRepository

# instantiate a Flask app object
app = Flask(__name__)

#index or home 
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


#new route
@app.route("/users/new",methods=['GET'])
def signup():
    return render_template("signup_form.html")

#new throd on existing route
@app.route("/users",methods=["POST"])
def create_user():
    #set up DB and connection
    connection = DatabaseConnection()
    connection.connect()
    #connect book repo
    user_repository = UserRepository(connection)
    #new book = form data
    user_details = request.form
    #new book instance
    user = User(username=user_details["username"],password=user_details["password"])
    #create the book 
    user_repository.create(user)
    #redirect to books
    return redirect("/books")





#new route
@app.route('/books', methods =['GET'])
def get_all_books():
    #DB set up
    connection = DatabaseConnection()
    connection.connect()
    #sql set up
    book_repository = BookRepository(connection)
    #methods on class 
    books = book_repository.all()
    #render page
    return render_template("books.html", books=books)

#new method on existing route
@app.route('/books',methods =['post'])
def create_books():
    #set up DB and connection
    connection = DatabaseConnection()
    connection.connect()
    #connect book repo
    book_repository = BookRepository(connection)
    #new book = form data
    book_details = request.form
    #new book instance
    book = Book(title=book_details["title"],author=book_details["author"])
    #create the book 
    book_repository.create(book)
    #redirect to books
    return redirect("/books")

#new route
@app.route('/films', methods=['GET'])
def get_all_films():
    #connect to DB
    connection = DatabaseConnection()
    connection.connect()
    #run SQL file direcly onto connection and assign return value to variable 
    films = connection.execute('SELECT * FROM films')
    # render html file and pass variable     
    return render_template('films.html',films = films)


# - API ROUTES -

#api route
@app.route('/api/books', methods =['GET'])
def api_get_all_books():
    #DB set up
    connection = DatabaseConnection()
    connection.connect()
    #sql set up
    book_repository = BookRepository(connection)
    #methods on class 
    books = book_repository.all()
    #return json
    return jsonify([{"title": b.title, "author": b.author} for b in books])

#api route
@app.route('/api/films', methods=['GET'])
def api_get_all_films():
    #connect to DB
    connection = DatabaseConnection()
    connection.connect()
    #run SQL file direcly onto connection and assign return value to variable 
    films = connection.execute('SELECT * FROM films')
    # return json
    return jsonify([{"title": b["title"], "release_year": b["release_year"]} for b in films])


# make the server run in response to `python app.py`
# on port 5001 (you'll learn more about what this means later)
# and use debug mode so that changing code restarts the app
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5001, debug=True)