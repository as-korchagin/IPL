from lab_6.cursormgr import CursorManager


class Book:
    db_connection = None
    name = None
    description = None
    cursor = None

    def __init__(self, db_connection, name=None, description=None):
        self.cursor = CursorManager(db_connection.connection())
        self.name = name
        self.description = description

    def save(self):
        self.exec("INSERT INTO books (name, description) VALUES ('%s', '%s')" %
                  (self.name, self.description))

    def delete(self):
        self.exec("DELETE FROM books WHERE name='%s'" % self.name)

    def update(self):
        with self.cursor as c:
            c.execute("UPDATE books SET description='%s' WHERE name='%s'" %
                      (self.description, self.name))

    def select(self, *args, **kwargs):
        sql = ''.join(i for i in ("SELECT %s FROM books" % ','.join(args)))
        if len(kwargs) != 0:
            params = list('{}={}'.format(i,
                                         kwargs.get(i) if type(kwargs.get(i)) == int else "'{}'".format(kwargs.get(i)))
                          for i in kwargs.keys())
            sql += " WHERE %s" % ' AND '.join(params)
        self.exec(sql)

    def exec(self, sql):
        with self.cursor as c:
            c.execute(sql)
