#!/usr/bin/env python3
''' An api capable of all CRUD operations'''
# Import neccessary modules
from datetime import datetime
from flask import Flask, jsonify, request, Blueprint, abort
from flask_cors import CORS

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from . import users# import User, Base

# Creating the flask app
app = Flask(__name__)
app_views = Blueprint("app_views", __name__, url_prefix="")
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Setting up a database engine
engine = create_engine("sqlite:///HNGxTWO.db")  # can be edited to use another database
users.Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

# Route to ensure the server is running
@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    return jsonify({"status": "OK"})

# Error Handlers
@app.errorhandler(415)
def not_supported(error):
    return jsonify({'error': 'Unsupported media type'}), 415
@app.errorhandler(405)
def not_allowed(error):
    return jsonify({'error': 'Request method not allowed'}), 405
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(401)
def not_authorized(error):
    return jsonify({"error": "Unauthorized"}), 401

@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad Request Type"}), 400

# CRUD Operations
# Checker
@app_views.route('/api', methods=['GET'], strict_slashes=True)
def allUsers():
    '''Gets all users in the database'''
    session = Session()
    users_all = users.User.all(session)
    all_users = [user.to_json() for user in users_all]
    return jsonify(all_users)

# CREATE a new User
@app_views.route('/api', methods=["POST"], strict_slashes=False)
def new_user():
    '''Creates a new user object'''
    try:
        data = request.get_json()
    except:
        abort(415)
    if not data:
        return jsonify({'error': 'Wrong format'}), 400
    if not data.get("name"):
        return jsonify({'error': 'Name missing'}), 400

    try:
        session = Session()
        #check if there is a user with same name
        duplicate = users.User.get(session, data["name"])
        print(duplicate)
        if duplicate is None:
            user = users.User(name=data["name"])
            user.save(session)
            return jsonify(user.to_json()), 201
        else:
            print('ddid not get here')
            return jsonify({"error": "User already exists"}), 400
    except Exception as e:
        return jsonify({'error': f"Can\'t create User: {e}"}), 400

# READ gets details of a user
@app_views.route("/api/<string:user_id>", methods=["GET"], strict_slashes=False)
def get_user(user_id: str) -> str:
    ''' Gets a user object based on user id'''
    if isinstance(user_id, int) or user_id is None or not user_id:
        abort(405)
    else:
        session = Session()
        if user := users.User.get(session, user_id):
            return jsonify(user.to_json())
        else:
            return jsonify({'error': 'User not found'}), 404

# UPDATE updates the details of a user
@app_views.route("/api/<string:user_id>", methods=["PUT"], strict_slashes=False)
def update_user(user_id: str) -> str:
    ''' Updates a user obj based on the user id'''
    if user_id is None or isinstance(user_id, int) or not user_id:
        abort(405)
    session = Session()
    user = users.User.get(session, user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    data = request.get_json()
    if not data:
        return jsonify({'error': 'Wrong format'}), 400

    if 'name' in data:
        duplicate = users.User.get(session, data['name'])
        if duplicate is None:
            user.name = data['name']
            user.save(session)
            return jsonify(user.to_json()), 200
        else:
            return jsonify({"error": "Name already exists"}), 400

# DELETE Removes a user from the database
@app_views.route("/api/<string:user_id>", methods=["DELETE"], strict_slashes=False)
def delete_user(user_id: str) -> str:
    ''' Deletes a user from the database'''
    if user_id is None or isinstance(user_id, int) or not user_id:                                                                    abort(405)
    session = Session()
    user = users.User.get(session, user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    user.delete(session)
    return jsonify({}), 204

app.register_blueprint(app_views)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

