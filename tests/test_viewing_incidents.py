from tests.base_test import BaseTest
from flask import jsonify, json

class TestViewingIncidents(BaseTest):

     def test_get_all_redflags(self):
        """ Test for getting all red-flag records"""
        with self.client:
            response = self.create_redflag()
            response1 = self.client.get(
                "/api/v1/red-flags",
                content_type="application/json"
            )
            self.assertEqual(response1.status_code, 200)