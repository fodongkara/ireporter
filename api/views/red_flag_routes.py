from flask import Flask, jsonify, request, Blueprint
from api.controllers.incident_controller import IncidentController

inc_controller = IncidentController()
red_flag_blueprint = Blueprint("red_flag_blueprint", __name__)


@red_flag_blueprint.route("/")
def home():
    """A welcoming route to my api"""
    return inc_controller.home()


@red_flag_blueprint.route("/red-flags", methods=["POST"])
def create_redflag():
    """API end point to create a red-flag record"""
    return inc_controller.create_redflag()


@red_flag_blueprint.route("/red-flags", methods=["GET"])
def get_all_red_flags():
    """API end point to fetch all records"""
    return inc_controller.get_all_red_flags()


@red_flag_blueprint.route("/red-flags/<int:flag_id>", methods=["GET"])
def get_a_redflag(flag_id):
    """API end point to fetch a specific record"""
    return inc_controller.get_a_redflag(flag_id)


@red_flag_blueprint.route("/red-flags/<int:flag_id>", methods=["DELETE"])
def delete_red_flag(flag_id):
    """API end point to delete a specific record"""
    return inc_controller.delete_red_flag(flag_id)


@red_flag_blueprint.route("/red-flags/<int:flag_id>/location", methods=["PATCH"])
def edit_red_flag_location(flag_id):
    """API end point to edit location of  red-flag record"""
    return inc_controller.edit_red_flag_location(flag_id)


@red_flag_blueprint.route("/red-flags/<int:flag_id>/comment", methods=["PATCH"])
def edit_red_flag_comment(flag_id):
    """API end point to edit comment of a  red-flag record"""
    return inc_controller.edit_red_flag_comment(flag_id)
