from api.controllers.user_controller import login_user, signup_user


"""signup user route """


@app.route('api/v1/users', methods=['POST'])
def signup():
    return signup_user()


"""login user or admin route"""


@app.route('api/v1/users/login', methods=['POST'])
def login():
    return login_user()
