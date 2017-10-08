from lab_6.book import Book
from lab_6.connection import Connection

connection = Connection(user='lab6_user', password='test', db='first_db')
with connection:
    book = Book(connection, 'Как закалялась сталь', "Николай Островский")
    book.select(*['id', 'name'], **{'id': 16})
