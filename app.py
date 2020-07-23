from flask_restplus import Api, Resource, reqparse
from flask import Flask, jsonify, request   
from config.databases import mycollection
from config.app import config
from bson import ObjectId, Binary, Code, json_util
from bson.json_util import dumps
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp
import json

class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return "User(id='%s')" % self.id

users = [
    User(1, 'user1', 'abcxyz'),
    User(2, 'user2', 'abcxyz'),
]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

def authenticate(username, password):
    user = username_table.get(username, None)
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)


app = Flask(__name__)
api = Api(app, version='1.0', title='w-mz-ge', description='Smarted test')
app.config["SECRET_KEY"] = "super-secret"

jwt = JWT(app, authenticate, identity)

@app.route('/protected')
@jwt_required()
def protected():
    return '%s' % current_identity

@api.route('/users')
class UserData(Resource):

    # Check payload (Documentation)
    parser = reqparse.RequestParser()
    parser.add_argument("name", help='User Name', location='form')
    parser.add_argument("lastname", help='User Last Name', location='form')
    parser.add_argument("email", help='User Email', location='form')
    parser.add_argument("password", help='User Password', location='form')

    """
    Creates a new user
    """

    @api.expect(parser)
    @jwt_required()
    def post(self):

        input_data = request.get_json()
        name       = input_data["name"]
        lastName   = input_data["lastname"]
        email      = input_data["email"]
        password   = input_data["password"]
        
        # Check input data
        if name and lastName and email and password:
            user = {
                "name" : name ,
                "lastname" : lastName,
                "email" : email,
                "password" : password
            }

            # Inserts new user into DB
            userid = mycollection.insert_one(user)

            # The id of the object is returned
            return jsonify(id=str(userid.inserted_id))
            
        else: 
            return api.abort(400,"Error, one or more fields are required")



@api.route('/users/view') 
class UserData(Resource):
    @jwt_required()
    def get(self):
        userlist = []

        # Recovers every item in DB
        for user in mycollection.find():
            userlist.append(user)

        return json.loads(json_util.dumps(userlist))



if __name__ == '__main__':
    app.run(debug=config["debug"], port=config["port"])