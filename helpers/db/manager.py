from helpers.db.client import PostgresClient


class DBManager(object):
    def __init__(self):
        self.db = PostgresClient()

    def query_example(self):
        return self.db.query('SELECT version()').fetchall()


db_manager = DBManager()