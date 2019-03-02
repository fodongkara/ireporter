import re


class ValidateRecord():
    """Validator Class for the red-flag records"""
    def __init__self():
        pass

    @staticmethod
    def validate_type(record_type):
        """method validates the type of red-flag record"""
        return isinstance(record_type, str) and  record_type !="" and record_type in ['intervention','red-flag'] 

    @staticmethod
    def validate_comment(comment):
        """method validates the comment of a red-flag record"""
        return isinstance(comment, str) and comment != ""

    @staticmethod
    def validate_status(status):
        """method validates the status of an red-flag record"""
        return isinstance(status, str) and status =="draft"
    @staticmethod
    def validate_location(location):
        """method validates the location of an incident record"""
        return isinstance(location, list) and len(location) == 2 and isinstance(location[0], float) and isinstance(location[1], float)

    @staticmethod
    def validate_images(images):
        """method validates images of an incident record"""
        return isinstance(images, str) and images !=""

    @staticmethod
    def validate_videos(videos):
        """method validates videos of an incident record"""
        return isinstance(videos, str) and videos !=""



class UserValidation:
    """Validation class for users """
    @staticmethod
    def validate_user_name(name):
        """method validates user name """
        return isinstance(name, str) and name != "" and not re.search(r'[\s]', name)

    @staticmethod
    def validate_phone_number(phone_number):
        """method validates user's phone number """
        return isinstance(phone_number, int) and phone_number != ""

    @staticmethod
    def validate_user_password(password):
        """method validates user's password """
        return isinstance(password, str) and len(password) >= 5 and password != "" and re.search(r'[a-zA-Z]', password) and re.search(r'[0-9]', password)

    @staticmethod
    def validate_user_email(email):
        """method that validates user's email"""
        return re.match(r"[^@]+@[^@]+\.[^@]+", email) and email != ""

    def get_user(current_user):
        """function returns data of the current user """
        for user in user_data:
            if user['email'] == current_user:
                return user

    def check_is_admin(current_user):
        """function checks if a user is an admin """
        if current_user["is_admin"]:
            return True
