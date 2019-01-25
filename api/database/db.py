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
                registered VARCHAR NOT NULL,
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
        phone_number, username, registered, Password, admin
    ):
        reg_user = "INSERT INTO users(\
            firstname, lastname, othernames, email,\
            phone_number, username, password,\
            registered,is_admin) VALUES ('{}','{}', '{}', '{}','{}','{}','{}','{}', '{}')".format(firstname, lastname, othernames, email, phone_number, username, Password, registered, admin)
        return self.cursor.execute(reg_user)

    def insert_incident(self, created_by, incident_type, status, images, location, videos, comments):
        insert_incident = "INSERT INTO records_table(createdBy, record_type, incident_location, Image, Videos, comment, incident_status) VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
            created_by, incident_type, status, images, location, videos, comments)
        self.cursor.execute(insert_incident)

    def email_dup(self, email):
        query = "SELECT * FROM users WHERE email = '{}'".format(email)
        self.cursor.execute(query)
        user = self.cursor.fetchone()
        if user:
            return True
        return False

    def check_username(self, username):
        query = "SELECT username FROM users WHERE username='{}'".format(
            username)
        self.cursor.execute(query)
        user = self.cursor.fetchone()
        return user

    def login_user(self, email):
        query = "SELECT * FROM users WHERE email='{}'".format(email)
        self.cursor.execute(query)
        user = self.cursor.fetchone()
        return user

    def get_all_incidents(self):
        query = "SELECT * FROM records_table WHERE record_type='redflag'"
        self.cursor.execute(query)
        incidents = self.cursor.fetchall()
        return incidents

    def get_all_interventions(self):
        query = "SELECT * FROM records WHERE record_type='intervention'"
        self.cursor.execute(query)
        incidents = self.cursor.fetchall()
        return incidents

    def get_one_incident(self, incident_Id):
        query_incident = "SELECT * FROM records_table WHERE id='{}' AND record_type='red-flag'".format(
            incident_Id)
        self.cursor.execute(query_incident)
        incident = self.cursor.fetchone()
        return incident

    def get_one_intervention(self, incident_Id):
        query_incident = "SELECT * FROM records_table WHERE id='{}' AND record_type='intervention'".format(
            incident_Id)
        self.cursor.execute(query_incident)
        incident = self.cursor.fetchone()
        return incident

