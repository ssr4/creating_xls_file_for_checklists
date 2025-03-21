import psycopg2
from psycopg2 import Error
import psycopg2.extras
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


class DB:
    def __init__(self, host, port, user, password, db_name):
        self.connection = None
        self.connection = psycopg2.connect(host=host,
                                           port=port,
                                           user=user,
                                           password=password,
                                           database=db_name,
                                           )

    def query(self, sql, args):
        cursor = self.connection.cursor()
        cursor.execute(sql, args)
        return cursor

    def query_with_a_dictionary(self, sql, args):
        cursor = self.connection.cursor(
            cursor_factory=psycopg2.extras.RealDictCursor)
        cursor.execute(sql, args)
        return cursor

    def fetch(self, sql, args):
        rows = []
        cursor = self.query(sql, args)
        rows = cursor.fetchall()
        cursor.close()
        return rows

    def insert(self, sql, args):
        try:
            cursor = self.query(sql, args)
            self.connection.commit()
            cursor.close()
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL при вставке", error)

    def __del__(self):
        if self.connection != None:
            self.connection.close()
