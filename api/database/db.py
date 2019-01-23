import psycopg2
import psycopg2.extras
from pprint import pprint


class DatabaseConnection:
    def __init__(self):

        self.db_name = 'records_db'

        try:
            self.connection = psycopg2.connect(dbname=self.db_name, user="postgres",
                                               host="localhost", password="andela2018", port=5432)
            self.connection.autocommit = True
            self.cursor = self.connection.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor)

            print('Connected to the database successfully.')
            self.create_tables()

        except Exception as e:
            pprint(e)
            pprint('Failed to connect to the database.')

    def create_tables(self):

        create_tables = (
        """
            CREATE TABLE IF NOT EXISTS users (
                userId SERIAL NOT NULL PRIMARY KEY,
                firstname VARCHAR NOT NULL,
                lastname VARCHAR NOT NULL,
                othernames VARCHAR NOT NULL,
                email VARCHAR NOT NULL,
                phone_number VARCHAR NOT NULL,
                username VARCHAR NOT NULL,
                password VARCHAR NOT NULL,
                registered TIMESTAMP,
                is_admin BOOLEAN
            );
        """,

        """
            CREATE TABLE IF NOT EXISTS records_table(
                incident_id SERIAL PRIMARY KEY,
                createdOn TEXT NOT NULL,
                createdBy VARCHAR(50) NOT NULL,
                record_type VARCHAR(50) NOT NULL,
                incident_location TEXT NOT NULL,
                Image VARCHAR(50) NOT NULL,
                Videos VARCHAR(50) NOT NULL,
                comment TEXT NOT NULL,
                incident_status VARCHAR(50) NOT NULL
            );
        """
        )
        for table in create_tables:
            self.cursor.execute(table)

    def register_user(
        self, firstname, lastname, othernames, email,
        phone_number, username, password, is_admin
    ):
        reg_user = "INSERT INTO users(\
            firstname, lastname, othernames, email,\
            phone_number, username, password,\
            is_admin) VALUES ('{}','{}', '{}', '{}','{}','{}','{}','{}')".format(firstname, lastname, othernames, email, phone_number, username, password, is_admin)
        return self.cursor.execute(reg_user)


if __name__ == '__main__':
    db_name = DatabaseConnection()

