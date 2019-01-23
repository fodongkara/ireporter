from datetime import datetime

user_data = []


class User:
    """ model class for users """

    def __init__(self, firstname, lastname, othernames, email, phone_number,
                 username, password, is_admin):
        self.firstname = firstname
        self.lastname = lastname
        self.othernames = othernames
        self.email = email
        self.phone_number = phone_number
        self.username = username
        self.password = password
        self.registered = datetime.now()
        self.is_admin = is_admin

    def format_user_record(self):
        """Method that returns dictionary representation of the object"""
        return {
            'id': self._id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'othernames': self.othernames,
            'email': self.email,
            'phoneNumber': self.phone_number,
            'username': self.username,
            "Password": self.password,
            'registered': self.registered,
            'isAdmin': self.is_admin
        }

    @staticmethod
    def check_user_exists(email):
        """method checks if a user exists in the system"""
        for user in user_data:
            return user['email'] == email
