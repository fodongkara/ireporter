from flask import request, jsonify
from api.authentication.auth import generate_token
from werkzeug.security import generate_password_hash, check_password_hash
from api.models.user_incident import User
from api.utility.validation import UserValidation
from api.database.db import DatabaseConnection
from datetime import datetime, timedelta

db_conn = DatabaseConnection()


class UserController:
    def __init__(self):
        pass

    def signup_user(self):
        """Method for user sign up"""
        data = request.get_json(force=True)
        first_name = data.get('first_name',None)
        last_name = data.get('last_name',None)
        other_names = data.get('other_names',None)
        user_email = data.get('user_email',None)
        phone_number = data.get('phone_number',None)
        user_name = data.get('user_name',None)
        Password = data.get('Password',None)
        registered = datetime.now()
        admin = data.get("admin",None)
        if not first_name or not last_name or not\
                other_names or not user_email or not phone_number or not \
                user_name or not Password or not admin:
            return jsonify({
                'status': 400,
                'error': 'A required field is either missing or empty'
            }), 400

        if not UserValidation.validate_phone_number(phone_number):
            return jsonify({
                'status': 400,
                'error': 'Phone number requires only numbers '
            }), 400
        if not UserValidation.validate_user_email(user_email):
            return jsonify({
                'status': 400,
                'error': 'Please provide correct email format --> abc@gmail.com'
            }), 400
        user = User(first_name, last_name, other_names, user_email,
                    phone_number, user_name, registered, generate_password_hash(Password), admin)

        if db_conn.email_dup(user_email):
            return jsonify({'status': 400,
                            'error': 'User account already exists'}), 400
        db_conn.register_user(
            first_name, last_name, other_names, user_email, phone_number,
            user_name, registered, generate_password_hash(Password), admin
        )

        return jsonify({"data": [{
            "status": 201,
            "message": "user created successfully",
        }]}), 201

    def login_user(self):
        """Method for user login"""
        login_data = request.get_json()
        login_email = login_data.get('user_email')
        login_password = login_data.get('Password')
        if not UserValidation.validate_user_password(login_password):
            return jsonify({
                'status': 400,
                'error': 'Password must be atleast 5 characters and should have atleast one number and one capital letter'
            }), 400
        if not login_email:
            return jsonify({"Message": "Please enter your credentials"})
        if not db_conn.login_user(login_email):
            return jsonify({
                "Error": "User account does not exist",
                "status": 400
            }), 400
        user = db_conn.login_user(login_email)
        if check_password_hash(user["password"], login_password):
            access_token = generate_token(1)
            return jsonify({'access-token': access_token,   "Message": "User successfully logged in"}), 201
        return jsonify({
            "Error": "Invalid  password"
        })
