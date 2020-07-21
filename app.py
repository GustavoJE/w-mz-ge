from flask_restplus import Api, Resource, reqparse
from flask import Flask, jsonify, request   
from config.databases import mycollection
from config.app import config
from bson import ObjectId, Binary, Code, json_util
from bson.json_util import dumps
import json



app = Flask(__name__)
api = Api(app, version='1.0', title='w-mz-ge', description='Smarted test')

@api.route('/users')
class UserData(Resource):

    # Check payload (Documentation)
    parser = reqparse.RequestParser()
    parser.add_argument("name", help='User Name', location='form')
    parser.add_argument("lastName", help='User Last Name', location='form')
    parser.add_argument("email", help='User Email', location='form')
    parser.add_argument("password", help='User Password', location='form')

    """
    Creates a new user
    """

    @api.expect(parser)
    def post(self):

        input_data = request.get_json()
        name       = input_data["name"]
        lastName   = input_data["lastName"]
        email      = input_data["email"]
        password   = input_data["password"]
        
        # Check input data
        if name and lastName and email and password:
            user = {
                "name" : name ,
                "lastName" : lastName,
                "email" : email,
                "password" : password
            }

            userid = mycollection.insert_one(user)

            # The id of the object is returned
            return jsonify(id=str(userid.inserted_id))
            
        else: 
            return api.abort(400,"Error, one or more fields are required")



@api.route('/users/view')     
class UserData(Resource):
    def get(self):
        userlist = []
        for user in mycollection.find():
            userlist.append(user)

        return json.loads(json_util.dumps(userlist))
        
if __name__ == '__main__':
    app.run(debug=config["debug"], port=config["port"])