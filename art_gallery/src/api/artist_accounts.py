from re import U
from flask import Blueprint, jsonify, abort, request
from ..models import Artist, Artwork, Artist_Account, Category, Collector, Collector_Account,  db, categories_table
import hashlib
import secrets

bp = Blueprint('artist_accounts', __name__, url_prefix='/artist_accounts')

def scramble(password: str):
    """Hash and salt the given password"""
    salt = secrets.token_hex(16)
    return hashlib.sha512((password + salt).encode('utf-8')).hexdigest()

# not working
@bp.route('/<int:id>', methods=['PATCH', 'PUT'])
def update(id: int):
    a = Artist_Account.query.get_or_404(id)
    if 'email' not in request.json or 'password' not in request.json:
        return abort(400)
    if 'email' not in request.json:
        if len(request.json['email']) < 3:
            return abort(400)
        a.email = request.json['email']

    if 'password' not in request.json:
        if len(request.json['password']) < 6:
          return abort(400)
        a.password = request.json['password']  
    
    try:
        db.session.commit()
        return jsonify(a.serialize())
    except:
        return jsonify(False)