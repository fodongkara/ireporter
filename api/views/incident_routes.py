from flask import Flask, jsonify, request, Blueprint
from api.controllers.red_flag_controller import RedflagController
from api.controllers.intervention_controller import InterventionController
from api.authentication.auth import token_required, admin_required
from api.controllers.intervention_controller import InterventionController

inc_controller = RedflagController()
int_controller = InterventionController()
incident_blueprint = Blueprint("incident_blueprint", __name__)


@incident_blueprint.route("/")
def home():
    """A welcoming route to my api"""
    return inc_controller.home()


@incident_blueprint.route("/intervention", methods=["POST"])
@token_required
def create_intervention_record():
    """API end point to create a red-flag record"""
    return int_controller.create_intervention_record()


@incident_blueprint.route("/red-flags", methods=["GET"])
@token_required
def get_all_red_flags():
    """API end point to fetch all records"""
    return inc_controller.get_all_red_flags()


@incident_blueprint.route("/red-flags/<int:flag_id>", methods=["GET"])
@token_required
def get_a_redflag(flag_id):
    """API end point to fetch a specific record"""
    return inc_controller.get_a_redflag(flag_id)


@incident_blueprint.route("/red-flags/<int:flag_id>", methods=["DELETE"])
@admin_required
def delete_red_flag(flag_id):
    """API end point to delete a specific record"""
    return inc_controller.delete_red_flag(flag_id)


@incident_blueprint.route("/red-flags/<int:flag_id>/location", methods=["PATCH"])
@token_required
def edit_red_flag_location(flag_id):
    """API end point to edit location of  red-flag record"""
    return inc_controller.edit_red_flag_location(flag_id)


@incident_blueprint.route("/red-flags/<int:flag_id>/comment", methods=["PATCH"])
@token_required
def edit_red_flag_comment(flag_id):
    """API end point to edit comment of a  red-flag record"""
    return inc_controller.edit_red_flag_comment(flag_id)
