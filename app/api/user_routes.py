from flask import Blueprint,jsonify, request
from flask_login import login_required, current_user
from app.models import User, db
from app.forms import UserUpdateForm
from app.models import UpdateUser




user_routes = Blueprint("user", __name__)


@user_routes.route("/")
@login_required
def users():
    """
    Query for all users and returns them in a list of user dictionaries
    """
    users = User.query.all()
    return {"user": {user.id: user.to_dict() for user in users}}

@user_routes.route("/<int:id>", methods=['PUT'])
@login_required
def update_user(id):
    print(f'CURRENT USER {id}')

    if current_user.id == id:

        form= UserUpdateForm()
        form["csrf_token"].data = request.cookies["csrf_token"]
        if form.validate_on_submit():
            user = User(
                email =form.data["email"],
                name =form.data["name"],
                user =form.data["user"]
            )

            db.session.add(user)
            db.session.commit()
            return user.to_dict()
        return form.errors,401
    else:
        return {"error": "User does not have access to this account information"}



    #theUser = user(id)
    #person = theUser["user"]
    #user_email = person[id]['email']
    #user_name = person[id]['user']
    #user_password = person[id]['password']




    return user_email



    #return id
    #currentUser = User.query.get()
    #data = request.get_json()

    #request form data when avaiable

    #if request.form.get("username"):
        #currentUser.username = data['username']
    #if request.form.get("email"):
        #currentUser.email = data['email']
    #if request.form.get("password"):
        #currentUser.password = data['password']

    #db.session.commit()
    #return currentUser




@user_routes.route("/<int:id>")
@login_required
def user(id):
    """
    Query for a user by id and returns that user in a dictionary
    """
    user = User.query.get(id)
    return {"user": {user.id: user.to_dict()}}
