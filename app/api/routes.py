from flask import Blueprint, request, jsonify, render_template
from helpers import token_required
from models import db, User, Whiskey, whiskey_schema, whiskeys_schema

api = Blueprint('api',__name__, url_prefix='/api')

@api.route('/whiskeys', methods = ['POST'])
@token_required
def create_whiskey(current_user_token):
    name = request.json['name']
    brand = request.json['brand']
    age = request.json['age']
    price = request.json['price']
    user_token = current_user_token.token

    print(f'BIG TESTER: {current_user_token.token}')

    whiskey = Whiskey(name, brand, age, price, user_token = user_token )

    db.session.add(whiskey)
    db.session.commit()

    response = whiskey_schema.dump(whiskey)
    return jsonify(response)