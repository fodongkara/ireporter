import unittest
from api import create_app
from flask import json

from api.database.db import DatabaseConnection
from api.models.user_incident import User
from api.controllers.user_controller import UserController
from api.authentication.auth import generate_token

db_conn = DatabaseConnection()
user_controller = UserController()

class BaseTest(unittest.TestCase):
    """ Class for test data"""

    def setUp(self):
        self.run = create_app()
        self.client = self.run.test_client()
        self.admin_data = {
            "firstname": "Admin",
            "lastname": "ireporter",
            "othernames": "",
            "email": "adminireporter@gmail.com",
            "username": "admin007",
            "password": "nadra2526#A",
            "phone_number": "+256779004531",
            "is_admin":"True"
        }
        self.reporter_data = {
            "firstname": "Ernest",
            "lastname": "henry",
            "othernames": "",
            "email": "henry@gmail.com",
            "username": "ernest007",
            "password": "ernest2526#A",
            "phone_number": "+256779004830",
            "is_admin":"False"
        }
        self.sample_record_data = {
            "createdBy": "anthony",
            "type": "red-flag",
            "location": "kitalanga",
            "status": "resolved",
            "Images": "fed.png",
            "Videos": "gfgg.mp4",
            "comment": "This is good"
        }
        self.register_admin()
        self.register_reporter()

    def tearDown(self):
        """Method to drop tables after the test is run"""
        pass

    def register_admin(self):
        """Method to register an admin"""
        return self.client.post(
            "/api/v1/auth/signup",
            data=json.dumps(self.admin_data),
            content_type="application/json"
        )
        
    def register_reporter(self):
        """Method to register a reporter"""
        return self.client.post(
            "/api/v1/auth/signup",
            data=json.dumps(self.reporter_data),
            content_type="application/json"
        )

    def admin_token(self):
        """Method to create a token for admin"""
        pass

    def reporter_token(self):
        """Method to create a token for reporter"""
        pass

    def create_intervention(self):
        """
        Function to create a intervention
        """
        return self.client.post(
            "/api/v1/interventions",
            data=json.dumps(self.sample_record_data),
            content_type="application/json"
        )
    def create_redflag(self):
        """
        Function to create a redflags
        """
        return self.client.post(
            "/api/v1/red-flags",
            data=json.dumps(self.sample_record_data),
            content_type="application/json"
        )