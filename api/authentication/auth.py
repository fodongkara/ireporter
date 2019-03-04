import jwt
import os 
from functools import wraps
from datetime import datetime, timedelta
from flask import request, jsonify

SECRET_KEY = os.environ["SECRET_KEY"]


def generate_token(user_id, is_admin):
    try:
        # set up a payload with an expiration time
        payload = {
            'exp': datetime.utcnow() + timedelta(minutes=2),
            'iat': datetime.utcnow(),
            'uid': user_id,
            'is_admin': is_admin
        }
        # create the byte string token using the payload and the SECRET key
        jwt_string = jwt.encode(payload, SECRET_KEY,
                                algorithm='HS256').decode("utf-8")
        return jwt_string

    except Exception as e:
        # return an error in string format if an exception occurs
        return str(e)


def decode_token(token):
    """Decodes the access token from the Authorization header."""
    try:
        # try to decode the token using our SECRET variable
        payload = jwt.decode(token, SECRET_KEY)
        print(payload)
        return payload['uid']
    except jwt.ExpiredSignatureError:
        # the token is expired, return an error string
        return "Expired token. Please login to get a new token"
    except jwt.InvalidTokenError:
        # the token is invalid, return an error string
        return "Invalid token. Please register or login"


def extract_token_from_header():
    """Get token fromm the headers"""
    if 'Authorization' in request.headers:
        authorization_header = request.headers.get('Authorization')
        token = authorization_header.split(" ")[1]
        return token


def token_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        response = None
        try:
            if 'Authorization' not in request.headers:
                return jsonify({
                    "error": "Missing authorization header",
                    "status": 400
                })
        except jwt.ExpiredSignatureError:
            response = (
                jsonify(
                    {"error": "Invalid Token, verification failed", "status": 401}),
                401,
            )
        except jwt.InvalidTokenError:
            response = (
                jsonify({"error": "invalid token message", "status": 401}),
                401,
            )
        return response
    return wrapper


def get_current_identity():
    """Get user_id from the token"""
    return decode_token(extract_token_from_header())["uid"]


def get_current_role():
    """Get user_id from the token"""
    return decode_token(extract_token_from_header())["is_admin"]


def admin_required(func):
    """Restrict non admin from accessing the resource"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not get_current_role():  # if non admin
            return jsonify({
                "error": "Only Admin can access this resource",
                "status": 403
            }), 403
        return func(*args, **kwargs)
    return wrapper
