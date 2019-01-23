import psycopg2
import psycopg2.extras
from pprint import pprint


class DatabaseConnection:
    def __init__(self):

        self.db_name = 'records_db'

        try:
            self.connection = psycopg2.connect("dbname=self.db_name, user=postgres, \
            host=localhost, password=postgres, port=5432")
            self.connection.autocommit = True
            self.cursor = self.connection.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor)

            print('Connected to the database successfully.')
            print(self.db_name)

            create_users_table = "CREATE TABLE IF NOT EXISTS users(
                userId SERIAL NOT NULL PRIMARY KEY, firstname TEXT NOT NULL,
                lastname TEXT NOT NULL, othernames TEXT NOT NULL,
                email TEXT NOT NULL, phone_number TEXT NOT NULL,
                username TEXT NOT NUL, password TEXT NOT NULL,
                is_admin TEXT NOT NUL
            )"

            self.cursor.execute(create_users_table)
        except Exception as e:
            pprint(e)
            pprint('Failed to connect to the database.')

    def register_user(self, firstname, lastname, othernames, email,
                      phone_number, username, password, is_admin):
        reg_user = f"INSERT INTO users(
            firstname, lastname, othernames, email,
            phone_number, username, password,
            is_admin) VALUES(
                '{firstname}', '{lastname}', '{othernames}, {email}',
                '{phone_number}', '{username}', {password}',
                '{is_admin}'"
            pprint(reg_user)


if __name__ == '__main__':
    db_name=DatabaseConnection()
