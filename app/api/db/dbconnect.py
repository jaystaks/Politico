import psycopg2
import click

from flask.cli import with_appcontext
from .schema import schema


class Database:
    """
    Database class
    """

    def __init__(self):
        self.conn = psycopg2.connect(
            database='test_db',
            user='postgres',
            password='root',
            host='127.0.0.1',
            port='5432'
        )

        self.cur = self.conn.cursor()

    def execute_query(self, query):
        try:
            self.cur.execute(query)
            self.conn.commit()
        except (Exception, psycopg2.DatabaseError) as e:
            print(e)

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
