import atexit

import psycopg2
import psycopg2.extras

from settings import config


class PostgresClient(object):
    def __init__(self):
        self.connection = None
        self.cursor = None
        atexit.register(self.close)

    def _create_connection(self):
        if not self.connection:
            pgsql = config.get('pgsql', {})
            self.connection = psycopg2.connect(dbname=pgsql.get('name'),
                                               user=pgsql.get('user'),
                                               password=pgsql.get('password'),
                                               host=pgsql.get('host'),
                                               port=pgsql.get('port'))
        return self.connection

    def _create_cursor(self):
        if not self.cursor:
            self.cursor = self.connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

        return self.cursor

    def query(self, query):
        self._create_connection()
        self._create_cursor()
        try:
            self.cursor.execute(query)
            self.connection.commit()
            return self.cursor
        except:
            raise Exception('Error with query execution')

    def close(self):
        if self.cursor:
            self.cursor.close()

        if self.connection:
            self.connection.close()
