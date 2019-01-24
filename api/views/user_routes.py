from flask import Blueprint
from api.controllers.user_controller import UserController

u_controller = UserController()

user_blueprint = Blueprint("user_blueprint", __name__)


@user_blueprint.route('/auth/signup', methods=['POST'])
def signup():
    """signup user route """
    return u_controller.signup_user()


@user_blueprint.route('/auth/login', methods=['POST'])
def login():
    """login user or admin route"""
    return u_controller.login_user()
