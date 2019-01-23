import unittest
import json
from api.controllers.incident_controller import my_red_flags
from api import create_app


""" Module for running my tests """


class BaseTest(unittest.TestCase):
    """ Class for test data"""

    def setUp(self):
        self.client = create_app()
        self.client = self.client.test_client()
        self.sample_record_data = {
            "createdBy": "anthony",
            "type": "red-flag",
            "location": "kitalanga",
            "status": "resolved",
            "Images": "fed.png",
            "Videos": "gfgg.mp4",
            "comment": "This is good"
        }

        self.post_record = self.client.post(
            "/api/v1/red-flags",
            data=json.dumps(self.sample_record_data),
            content_type="application/json"
        )


class TestRedFlag(BaseTest):
    """ Test for creating a red-flag record"""

    def test_create_red_flag(self):
        response = self.post_record
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.content_type, "application/json")
        self.assertIn(b"Created red-flag record", response.data)

    def test_home(self):
        """ Testing for getting the data at my home route """
        response = self.client.get('/')
        assert b'Welcome to ernest\'s iReporter app.' in response.data
        assert response.status_code == 200

    def test_get_all_redflags(self):
        """ Test for getting all red-flag records"""
        self.post_record
        response = self.client.get(
            "/api/v1/red-flags",
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("createdBy", str(response.data))
        self.assertEqual(response.content_type, "application/json")

    """ missing value field = bad """

    def test_post(self):
        record = {
            "Images": "fed.png",
            "Videos": "gfgg.mp4",
            "comment": ""
        }
        response = self.client.post(
            "/api/v1/red-flags",
            data=json.dumps(record),
            content_type='application/json'
        )
        response_data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        self.assertEqual("Required field is missing", response_data['Error'])

    def test_fetch_specific_redflag(self):
        """ Test for getting a specific red-flag record """
        response = self.client.get(
            '/api/v1/red-flags/1',
            content_type="application/json")
        response_data = json.loads(response.data.decode())
        self.assertEqual(response.content_type, "application/json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_data["status"], 200)
        response = self.client.get(
            '/api/v1/red-flags/100',
            content_type="application/json")
        assert response.status_code == 404

    def test_edit_location_and_comment(self):
        """ Test to edit location and  comment  of a red-flag record"""
        self.client.post(
            "/api/v1/red-flags",
            data=json.dumps(self.sample_record_data),
            content_type="application/json"
        )
        new_location = {"location": "Kampala"}
        response = self.client.patch(
            "/api/v1/red-flags/1/location",
            content_type="application/json",
            data=json.dumps(new_location)
        )
        response_data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(my_red_flags[0]["location"], "Kampala")
        self.assertEqual(response_data["status"], 200)
        self.assertIn("Updated red-flag's record location",
                      response_data["message"])
        self.assertIsInstance(response_data, dict)

        new_comment = {"comment": "Bad reports"}
        response = self.client.patch(
            "/api/v1/red-flags/1/comment",
            content_type="application/json",
            data=json.dumps(new_comment)
        )
        response_data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(my_red_flags[0]["comment"], "Bad reports")
        self.assertEqual(response_data["status"], 200)
        self.assertIn("Updated red-flag's record comment",
                      response_data["message"])
        self.assertIsInstance(response_data, dict)

    def test_delete_record(self):
        """ Test to delete a specific red-flag record """
        self.post_record
        response = self.client.delete(
            "/api/v1/red-flags/1"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(my_red_flags), 0)
        assert response.status_code == 200
