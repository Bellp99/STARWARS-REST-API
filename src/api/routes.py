"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Person, User_Person_Favorite, Favorites
from api.utils import generate_sitemap, APIException
from flask_cors import CORS

api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200


@api.route('/people', methods=['GET'])
def get_people():

    #query the database to get all the starwars characters
    all_people = Person.query.all()

    # take into consideration that there may be none records
    if all_people is None:
        return jsonify('Sorry! No star Wars characters found!'), 404
    else:
        all_people = list(map(lambda x: x.serialize(), all_people))
        return jsonify(all_people), 200

@api.route('/people/<int:person_id>', methods=['GET'])
def get_single_person(person_id):

    #query the database to get a specific starwars character by id
    single_person = db.session.get(Person, person_id)

    if single_person is None:
        raise APIException(f'Person ID {person_id} was not found!', status_code=404)
    
    single_person = single_person.serialize()
    return jsonify(single_person), 200

@api.route('/favorites', methods=['GET'])
def get_favorites():
    pass