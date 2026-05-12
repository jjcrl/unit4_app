import sys
import os
# this line is a bit of a hack which allows us to import app without changing anything else
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app import app

from lib.database_connection import DatabaseConnection

# a descriptive test name
def test_get_films_returns_a_200():
    # here's where we make the test client
    client = app.test_client()
    # here's where we make the request
    response = client.get("/films")
    # here's where we assert that the response's status code is 200
    assert response.status_code == 200

def test_get_all_films():
    connection = DatabaseConnection()
    connection.connect()
    connection.seed('./seeds/films.sql')

    # here's where we make the test client
    client = app.test_client()
    # here's where we make the request
    response = client.get("/api/films")
    
    #raw json from sql 
    assert response.json == [
        {
            'title':'Akira',
            'release_year':'1988'
            },
            {
             'title': 'The Beach',
             'release_year':'2000'
         }
    ]