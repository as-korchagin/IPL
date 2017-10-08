class CursorManager:
    db_connection = None
    cursor = None
    data = None

    def __init__(self, db_connection):
        self.db_connection = db_connection

    def __enter__(self):
        self.cursor = self.db_connection.cursor()
        return self

    def execute(self, sql):
        self.cursor.execute(sql)
        if "SELECT" not in sql:
            self.db_connection.commit()
            self.data = "Executed successfully"
        else:
            self.data = self.cursor.fetchall()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        print(self.data)
