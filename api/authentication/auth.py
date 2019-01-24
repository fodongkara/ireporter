import jwt
from functools import wraps
from datetime import datetime, timedelta
from flask import request, jsonify

SECRET_KEY = "fdfdwdcvb"


def generate_token(user_id):
    try:
        # set up a payload with an expiration time
        payload = {
            'exp': datetime.utcnow() + timedelta(minutes=60),
            'iat': datetime.utcnow(),
            'uid': user_id
        }
        # create the byte string token using the payload and the SECRET key
        jwt_string = jwt.encode(payload, SECRET_KEY,
                                algorithm='HS256').decode("utf-8")
        return jwt_string

    except Exception as e:
        # return an error in string format if an exception occurs
        return str(e)


@staticmethod
def decode_token(token):
    """Decodes the access token from the Authorization header."""
    try:
        # try to decode the token using our SECRET variable
        payload = jwt.decode(token, SECRET_KEY)
        return payload['uid']
    except jwt.ExpiredSignatureError:
        # the token is expired, return an error string
        return "Expired token. Please login to get a new token"
    except jwt.InvalidTokenError:
        # the token is invalid, return an error string
        return "Invalid token. Please register or login"


def extract_token_from_header():
    """Get token fromm the headers"""
    authorization_header = request.headers.get("Authorization")
    if not authorization_header or "Bearer" not in authorization_header:
        return jsonify({
            "error": "Bad authorization header",
            "status": 400
        })
    token = authorization_header.split(" ")[1]
    return token


def token_required(func):
    """Only requests with Authorization headers required"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        response = None
        try:
            extract_token_from_header()
            response = func(*args, **kwargs)
        except jwt.ExpiredSignatureError:
            response = jsonify({
                "error": "Your token expired",
                "status": 401
            }), 401
        except jwt.InvalidTokenError:
            response = jsonify({
                "erhror": "Invalid token",
                "status": 401
            }), 401
        return response
    return wrapper


def get_current_identity():
    """Get user_id from the token"""
    return decode_token(extract_token_from_header())["uid"]


def non_admin(func):
    """Restrict the admin from accessing the resource"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        if get_current_role():  # if admin
            return jsonify({
                "error": "Admin cannot access this resource",
                "status": 403
            }), 403
        return func(*args, **kwargs)
    return wrapper


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


def json_data_required(func):
    """Only requests with Content-type json will be allowed"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not request.is_json:
            return jsonify({
                "status": 400,
                "error": "JSON request required"
            }), 400
        return func(*args, **kwargs)
    return wrapper
