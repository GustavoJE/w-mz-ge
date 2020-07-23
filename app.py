from flask_restx import Api, Resource, reqparse
from flask import Flask, jsonify, request   
from config.databases import mycollection
from config.app import config
from bson import ObjectId, Binary, Code, json_util
from bson.json_util import dumps
from flask_jwt import JWT, jwt_required, current_identity
from security import authenticate, identity 
import json



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
    parser.add_argument("last_name", help='User Last Name', location='form')
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



@api.route('/users') 
class UserData(Resource):
    
    """
    Displays all users 
    """
    @jwt_required()
    def get(self):
        userlist = []

        # Recovers every item in DB
        for user in mycollection.find():
            userlist.append(user)

        return json.loads(json_util.dumps(userlist))



@api.doc(params={'id': 'The user id'})
@api.route('/users/<string:id>')
class UserData(Resource):

    """
    Displays a single user
    """
    @jwt_required()
    def get(self,id):

        oid = ObjectId(id)

        document = mycollection.find({"_id": oid})
        
        return json.loads(json_util.dumps(document))


if __name__ == '__main__':
    app.run(debug=config["debug"], port=config["port"])