from tests.base_test import BaseTest
from flask import jsonify, json

class TestAddingIncident(BaseTest):
    """ Test for creating an intervention/red-flag record"""
    def test_create_intervention_successfully(self):
        with self.client:
            response = self.create_intervention()
            reply = json.loads(response.data.decode())
            self.assertIn("incident successfully added", reply['message'])
            self.assertEqual(response.status_code, 201)
    
    def test_create_redflag_successfully(self):
        with self.client:
            response = self.create_redflag()
            reply = json.loads(response.data.decode())
            self.assertIn("incident successfully added", reply['message'])
            self.assertEqual(response.status_code, 201)
