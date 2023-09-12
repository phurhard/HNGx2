#!/usr/bin/env python3
"""HNG stage 2 task
    Building a simple REST API capable of CRUD
    Operations on a persons ressource.
    DB of choice is mySQL
"""
# importing important/ required modules
from flask import Flask, make_response, jsonify, request, Blueprint
from flask_cors import (CORS, cross_origin)
from users import User

# setting up the flask app
app = Flask(__name__)
app_views = Blueprint("app_views", __name__, url_prefix="")
CORS(app, resources={r"/api/*": {"origins": "*"}})

# A route to show if the app is up and running

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """ GET /api/v1/status
    Return:
      - the status of the API
    """
    return jsonify({"status": "OK"})

# Error handlers

@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(401)
def not_authorised(error) -> str:
    """ Unauthorised error
    """
    return jsonify({"error": "Unauthorized"}), 401

# start of CRUD Operations
# input validator
def strValidation(self, x: str = None) -> str:
    '''Validate input'''
    if x is None or type(x) is not str:
        return None
    else:
        return x

# Create a new persons instance

@app_views.route('/api', methods=["POST"], strict_slashes=False)
def newUser() -> str:
    """POST: Creates a new user instance
    
    Keyword arguments:
    data -- The JSON data needed to be filled into the user instance
            - name
    Return: A 200 response showing the instance has been created
            A 400 if user can''t be created
    """
    data = None
    error_msg = None
    
    try:
        data  = request.get_json()
        print(data)
        # data is gotten from the payload
    except:
        data = None
    if data is None:
        error_msg = "Wrong format"
    if error_msg is None and data.get("name", "") == "":
        error_msg = "Name missing"
    if error_msg is None:
        try:
            user = User()
            user.name = data.get("name")
            print(type(user.save()))
            user.new()
            user.save()
            return jsonify(user.to_json()), 201
        except Exception as e:
            error_msg = "Can't create User: {}".format(e)
    return jsonify({'error': error_msg}), 400

# Read from the DB n get a users info

@app_views.route("/api/<user_id>", methods=["GET"], strict_slashes=False)
def getUser(user_id):
    """ 
    GET the user based on the name
    
    Keyword arguments:
    name -- Name property to use to identify the user in the DB
    Return: The information of the user in JSON format like   this
            {
            id: 1,
            name: myName
            }
    """
#    if user_id is None or type(user_id) is not str:
#        abort(403)
    user = User.get(user_id)# implement from geoalert or airbnb4
    if user is None:
        abort(404)# initialize this at the top and message should b user not found
    return jsonify(user.to_json())

# Update a user reference based on the id

@app_views.route("/api/<user_id>", methods=["PUT"], strict_slashes=False)
def updateUser(user_id: str = None) -> str:
    """
    PUT
    Updates the user based on the user_id passed

    keyword arguments:
    user_id -- An identifier for the required user
    Return:    An updated user details
    """
    invalid = ["id"]
    if user_id is None or type(user_id) is not str:
        return jsonify({"error": "User_id value is expected"}), 404
    try:
        data = request.get_json()
    except:
        return jsonify('Wrong format')
    user = User.get(user_id)#Gets the user with that id
    if user is None:
        abort(404)
    if data.get('name') is not None:
        user.name = data.get("name")
    '''
    for k, v in data.items():
        if k is not in invalid:
                user.setattr(k, v)# sets the new attr
    '''
    user.save()
    return jsonify(user.to_json()), 200

# Deletes a user from the DB

@app_views.route("/api/<user_id>/", methods=["DELETE"], strict_slashes=False)
def deleteUser(user_id: str = None) -> str:
    """
    DELETE Removes a user from the database

    keyword arguments:
    user_id -- The user id of the user to delete
    Return: A 200 status code showing user has been deleted
    """
    if user_id is None or type(user_id) is not str:
        return jsonify("User id required and must be string"), 404
    user = User.get(user_id)
    if user is None:
        abort(404)
    user.remove()
    return jsonify({}), 200

app.register_blueprint(app_views)

if __name__ == "__main__":
    host = '0.0.0.0'
    port = 5000
    app.run(host, port, debug=1)
