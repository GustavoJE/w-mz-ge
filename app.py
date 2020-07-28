from flask_restx import Api, Resource, reqparse
from flask import Flask, jsonify, request   
from config.databases import mycollection
from config.app import config
from bson import ObjectId, Binary, Code, json_util
from bson.json_util import dumps
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
import json



app = Flask(__name__)
api = Api(app, version='1.0', title='w-mz-ge', description='Smarted test')
ns = api.namespace('', description="Main app")
app.config["SECRET_KEY"] = config["secret-key"]

jwt = JWTManager(app)



"""
The login route allows for authentication. 
If valid admin credentials are sent, a JWT token is returned. 
Said token is required for the /users methods
"""

@app.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    # Query the DB with username and password fields, if those exist a cursor is returned
    document = mycollection.find_one({"$and": [{"name": username}, {"password": password}]})
    
    # If the query is unsuccesfull, no cursor is returned, then an error is raised
    if not document:
        return jsonify({"msg": "Bad username or password"}), 401
    else:
        # If the query is succesfull, an access token is created and returned
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200



@app.route('/protected', methods=['GET'])
@jwt_required
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200



@ns.route('/users')
class UserData(Resource):

    # Check payload (Documentation)
    parser = reqparse.RequestParser()
    parser.add_argument("name", help='User Name', location='form')
    parser.add_argument("last_name", help='User Last Name', location='form')
    parser.add_argument("email", help='User Email', location='form')
    parser.add_argument("password", help='User Password', location='form')

    """
    Creates a new user
    """

    @api.expect(parser)
    @jwt_required
    def post(self):

        input_data = request.get_json()
        name       = input_data["name"]
        last_name   = input_data["last_name"]
        email      = input_data["email"]
        password   = input_data["password"]
        
        # Check input data
        if name and last_name and email and password:
            user = {
                "name" : name ,
                "last_name" : last_name,
                "email" : email,
                "password" : password
            }

            # Inserts new user into DB
            userid = mycollection.insert_one(user)

            # The id of the object is returned
            return jsonify(id=str(userid.inserted_id))
            
        else: 
            return api.abort(400,"Error, one or more fields are required")

    """
    Displays all users 
    """

    @jwt_required
    def get(self):
        userlist = []

        # Recovers every item in DB
        for user in mycollection.find():
            userlist.append(user)

        return json.loads(json_util.dumps(userlist))



@api.doc(params={'id': 'The user id'})
@ns.route('/users/<string:id>')
class UserData(Resource):

    """
    Displays a single user
    """

    @jwt_required
    def get(self,id):

        oid = ObjectId(id)

        document = mycollection.find({"_id": oid})
        
        return json.loads(json_util.dumps(document))


if __name__ == '__main__':
    app.run(debug=config["debug"], port=config["port"])