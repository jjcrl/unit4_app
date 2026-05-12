import sys
import os
from lib.database_connection import DatabaseConnection

# this line is a bit of a hack which allows us to import app without changing anything else
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app

# a descriptive test name
def test_get_books_returns_a_200():
    #connection - seeding test data base  
    connection = DatabaseConnection()
    connection.connect()
    connection.seed('./seeds/books.sql')

    # here's where we make the test client
    client = app.test_client()

    # here's where we make the request
    response = client.get("/books")

    # here's where we assert that the response's status code is 200
    assert response.status_code == 200

# # a descriptive test name
def test_api_all_books_json():
    #connection - seeding test data base  
    connection = DatabaseConnection()
    connection.connect()
    connection.seed('./seeds/books.sql')

    client = app.test_client()
    response = client.get("/api/books")

    # here's where we assert that the response body contains all the books
    # note that we need to call .json on the response
    assert response.json == [
      {
        "title": "The Gruffalo",
        "author": "Julia Donaldson"
      },
      {
        "title": "Ada Twist, Scientist",
        "author": "Andrea Beaty"
      },
      {
        "title": "The Girl Who Drank the Moon",
        "author": "Kelly Barnhill"
      },
      {
        "title": "Dragons in a Bag",
        "author": "Zetta Elliott"
      }
    ]