import MySQLdb


class Connection:
    user = None
    host = None
    password = None
    db = None
    _connection = None

    def __init__(self, user, password, db, host='localhost'):
        self.user = user
        self.host = host
        self.password = password
        self.db = db

    def connection(self):
        return self._connection

    def __enter__(self):
        self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._connection:
            self.disconnect()

    def connect(self):
        if not self._connection:
            self._connection = MySQLdb.connect(
                host=self.host,
                user=self.user,
                passwd=self.password,
                charset='utf8',
                db=self.db
            )

    def disconnect(self):
        if self._connection:
            self._connection.close()
