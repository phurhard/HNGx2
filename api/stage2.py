#!/usr/bin/env python3
"""HNG stage 2 task
    Building a simple REST API capable of CRUD
    Operations on a persons ressource.
    DB of choice is mySQL
"""
# importing important/ required modules
from flask import Flask, make_response, jsonify, request, Blueprint
from flask_cors import (CORS, cross_origin)

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

# start of CRUD Operations

# Create a new persons instance

@app_views.route('/api/', methods=["POST"], strict_slashes=False)
def newUser():
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
            user.save()
            return jsonify(user.to_json()), 201
        except Exception as e:
            error_msg = "Can't create User: {}".format(e)
    return jsonify({'error': error_msg}), 400

# Read from the DB n get a users info

@app_views.route("/api/", methods=["GET"], strict_slashes=False)
def getUser():
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
    user = User.get(name)# implement from geoalert or airbnb4
    if user is None:
        abort(404)# initialize this at the top and message should b user not found
    return jsonify(user.to_json())

# Update a user reference based on the id
            
app.register_blueprint(app_views)