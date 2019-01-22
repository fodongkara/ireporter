from flask import request, jsonify
from api.models.user_incident import User, user_data
from api.utility.validation import UserValidation


def signup_user():
    """Method for user sign up"""
    data = request.get_json()
    first_name = data.get('firstname')
    last_name = data.get('lastname')
    other_names = data.get('othernames')
    email = data.get('email')
    phone_number = data.get('phone_number')
    user_name = data.get('username')
    Password = data.get('password')
    if not first_name or not last_name or not\
            other_names or not email or not phone_number or not \
            user_name or not userPassword:
        return jsonify({'status': 400,
                        'error': 'A required field is either missing or empty'
                        }), 400

    if not UserValidation.validate_phone_number(number):
        return jsonify({'status': 400,
                        'error': 'Only numbers are allowed for the phonenumber field'
                        }), 400
    if not validate_email(email):
        return jsonify({'status': 400, 'error': 'Invalid email'}), 400
    if not UserValidation.validate_password(password):
        return jsonify({'status': 400,
                        'error': 'Password must be atleast 8 characters and should have atleast one number and one capital letter'}), 400
    user = User(first_name, last_name, other_names, email,
                phone_number, user_name, generate_password_hash(userPassword))
    if User.check_user_exists(email):
        return jsonify({'status': 400,
                        'error': 'User account already exists'}), 400
    user_db.append(user.to_json())
    return jsonify({'status': 201, 'data': user.to_json(),
                    'message': 'Your Account was created successfuly'}), 201


def login_user():
    """Method for user login"""
    login_data = request.get_json()
    login_email = login_data.get('email')
    login_password = login_data.get('password')
    if not login_email or not login_password:
        return jsonify({'status': 400,
                        'error': 'No email or password have been provided'
                        }), 400

    if not validate_email(login_email):
        return jsonify({'status': 400, 'error': 'Invalid email'}), 400

    if not validateUser.validate_password(login_password):
        return jsonify({'status': 400,
                        'error': 'Password must be atleast 8 characters and should have atleast one number and one capital letter'}), 400
    for search_data in user_db:
        if search_data['email'] == login_email and \
                check_password_hash(search_data['userpassword'],
                                    login_password):
            access_token = create_access_token(identity=search_data['email'])
            print(user_db)
            return jsonify({'status': 200, 'access_token': access_token,
                            'message': 'You are now loggedin'}), 200
    return jsonify({'status': 403, 'error': 'Wrong email or password'}), 403


def create_admin():
    admin = User('kato', 'ernest', 'henry', 'henry38ernest@gmail.com',
                 '0706578719', 'ernest_henry',
                 generate_password_hash('ernest54637'), isAdmin=True)
    user_db.append(admin.format_user_record())


create_admin()
