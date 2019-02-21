import psycopg2
import click
import os

from flask.cli import with_appcontext
from .dbschema import schema


class Database:
    """
    Database class
    """

    def __init__(self):
        self.conn = psycopg2.connect(
            database='test_db',
            user='postgres',
            password=os.getenv('DB_PASS'),
            host='127.0.0.1',
            port='5432'
        )

        self.cur = self.conn.cursor()

    def execute_query(self, query, return_data=True):
        cursor = self.conn.cursor()

        try:
            cursor.execute(query)
            self.conn.commit()

            if (return_data):
                col = [desc[0] for desc in cursor.description]
                results = []
                for row in cursor.fetchall():
                    results.append(dict(zip(col, row)))

                cursor.close()
                return results
        except (Exception, psycopg2.DatabaseError) as e:
            print(e)
        finally:
            cursor.close()

    def close_db(self):
        self.cur.close()
        self.conn.close()

def close_db(e=None):
    db = Database()
    db.close_db()

@click.command('init-db')
@with_appcontext
def init_db_command():
    """
    Clear the existing data and create new tables
    """
    db = Database()
    db.execute_query(schema)

    click.echo('Database Initialized')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
