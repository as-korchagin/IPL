from lab_6.book import Book
from lab_6.connection import Connection

connection = Connection(user='lab6_user', password='test', db='first_db')
with connection:
    book = Book(connection, 'Война и мир', 'Лев Толстой')
    book.select(['id', 'name'], **{'description': 'Лев Толстой'})
