import psycopg2
import psycopg2.extras
from pprint import pprint


class DatabaseConnection:
    def __init__(self):

        self.db_name = 'records_db'

        try:
            self.connection = psycopg2.connect(dbname=self.db_name, user="postgres",
                                               host="localhost", password="", port=5432)
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
                user_id SERIAL NOT NULL PRIMARY KEY,
                firstname VARCHAR(50) NOT NULL,
                lastname VARCHAR(50) NOT NULL,
                othernames VARCHAR(50) NOT NULL,
                email VARCHAR(20) NOT NULL,
                phone_number bigint NOT NULL,
                username VARCHAR(50) NOT NULL,
                user_password TEXT NOT NULL,
                registered DATE NOT NULL,
                is_admin BOOLEAN NOT NULL
            );
        """,

            """
            CREATE TABLE IF NOT EXISTS records_table(
                incident_id SERIAL PRIMARY KEY,
                createdOn DATE NOT NULL,
                createdBy VARCHAR(50) NOT NULL,
                record_type VARCHAR(50) NOT NULL,
                incident_location TEXT [] NOT NULL,
                Image TEXT,
                Videos TEXT,
                comment TEXT NOT NULL,
                incident_status VARCHAR(50) NOT NULL
            );
        """
        )
        for table in create_tables:
            self.cursor.execute(table)

    def register_user( self, firstname, lastname, othernames, email,
                      phone_number, username, registered, Password, admin):
        reg_user = "INSERT INTO users(\
            firstname, lastname, othernames, email,\
            phone_number, username, user_password,\
            registered,is_admin) VALUES ('{}','{}', '{}', '{}',\
            '{}','{}','{}','{}', '{}')".format(firstname, \
            lastname, othernames, email, phone_number, username, Password, registered, admin)
        return self.cursor.execute(reg_user)

    def insert_incident(self, created_on, created_by, incident_type, location_lat,
                        location_long, images,videos, comments, status):
        insert_incident = "INSERT INTO records_table(createdOn, createdBy, record_type,\
        incident_location, Image, Videos, comment, incident_status) VALUES('{}',\
        '{}', '{}', ARRAY['{}', '{}'], '{}', '{}', '{}', '{}')".format(
        created_on, created_by, incident_type, location_lat, location_long, images,
        videos, comments, status)
        self.cursor.execute(insert_incident)

    def select_one_user(self, table_column, input_data):
        query = "SELECT * FROM users WHERE {} = '{}'".format(table_column,
        input_data)
        self.cursor.execute(query)
        return self.cursor.fetchone()


    def select_all_users(self):
        query = "SELECT * from users"
        self.cursor.execute(query)
        return self.cursor.fetchall()


    def get_all_incidents(self, incident_type):
        query = "SELECT * FROM records_table WHERE record_type ='{}'"\
            .format(incident_type)
        self.cursor.execute(query)
        return self.cursor.fetchall()


    def gell_all_incidents_created_by_one_user(self, record_type, user_data):
        query = "SELECT * FROM records_table WHERE record_type = '{}' AND createdBy = '{}'"\
            .format(record_type, user_data)
        self.cursor.execute(query)
        return self.cursor.fetchall()


    def get_one_incident(self, record_type, incident_id):
        query_incident = "SELECT * FROM records_table WHERE incident_id = '{}' AND \
            record_type = '{}'".format( incident_id, record_type)
        self.cursor.execute(query_incident)
        return self.cursor.fetchone()


    def delete_incident(self, record_type, incident_id):
        query = "DELETE FROM records_table WHERE record_type = '{}' AND incident_id = '{}'"\
            .format(record_type, incident_id)
        return self.cursor.execute(query)


    def update_location(self, record_type, incident_id, lat_input, long_input):
        query = "UPDATE records_table SET incident_location[1] = '{}', incident_location[2] = '{}'\
             WHERE record_type = '{}' AND \
            incident_id = '{}'".format(lat_input, long_input, record_type,\
            incident_id)
        return self.cursor.execute(query)


    def update_incident_data(self, record_type, field_to_update, incident_id,
        input_data):
        query = "UPDATE records_table SET {} = '{}' WHERE record_type = '{}' AND\
            incident_id = '{}'".format(field_to_update, input_data, record_type,
            incident_id)
        return self.cursor.execute(query)


    def drop_tables(self):
        commands = ("""DROP TABLE users""",
                   """DROP TABLE records_table"""
                   )
        for command in commands:
            self.cursor.execute(command)

