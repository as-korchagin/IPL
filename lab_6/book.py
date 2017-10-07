class Book:
    db_connection = None
    name = None
    description = None

    def __init__(self, db_connection, name, description):
        self.db_connection = db_connection.connection()
        self.name = name
        self.description = description

    def save(self):
        cursor = self.db_connection.cursor()
        cursor.execute("INSERT INTO books (name, description) VALUES (%s, %s)",
                       (self.name, self.description))
        self.db_connection.commit()
        cursor.close()
