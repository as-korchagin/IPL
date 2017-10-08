class Book:
    junk = {'[', ']', "'"}
    db_connection = None
    name = None
    description = None

    def __init__(self, db_connection, name=None, description=None):
        self.db_connection = db_connection.connection()
        self.name = name
        self.description = description

    def save(self):
        cursor = self.db_connection.cursor()
        cursor.execute("INSERT INTO books (name, description) VALUES ('%s', '%s')" %
                       (self.name, self.description))
        self.db_connection.commit()
        cursor.close()

    def delete(self):
        cursor = self.db_connection.cursor()
        cursor.execute("DELETE FROM books WHERE name='%s'" % self.name)
        self.db_connection.commit()
        cursor.close()

    def update(self):
        cursor = self.db_connection.cursor()
        cursor.execute("UPDATE books SET description='%s' WHERE name='%s'" %
                       (self.description, self.name))
        self.db_connection.commit()
        cursor.close()

    def select(self, *args, **kwargs):
        cursor = self.db_connection.cursor()
        sql = ''.join(i for i in ("SELECT %s FROM books" % args) if i not in self.junk)
        if len(kwargs) != 0:
            params = list('{}={}'.format(i,
                                         kwargs.get(i) if type(kwargs.get(i)) == int else "'{}'".format(kwargs.get(i)))
                          for i in kwargs.keys())
            sql += " WHERE %s" % ' AND '.join(params)
        cursor.execute(sql)
        print(cursor.fetchall())
        cursor.close()
