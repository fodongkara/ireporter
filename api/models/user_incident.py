from datetime import datetime


class User:
    """ model class for users """

    def __init__(self, firstname, lastname, othernames, email, phone_number,
                 username, password, registered, is_admin):
        self.firstname = firstname
        self.lastname = lastname
        self.othernames = othernames
        self.email = email
        self.phone_number = phone_number
        self.username = username
        self.password = password
        self.registered = registered
        self.is_admin = is_admin
