from re import U
from flask import Blueprint, jsonify, abort, request
from ..models import Artist, Artwork, Artist_Account, Category, Collector, Collector_Account,  db, categories_table
import hashlib
import secrets

bp = Blueprint('artists', __name__, url_prefix='/artists')


@bp.route('', methods=['GET'])
def index():
    artist = Artist.query.all() 
    result = []
    for a in artist:
        result.append(a.serialize()) 
    return jsonify(result) 

@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    a = Artist.query.get_or_404(id)
    return jsonify(a.serialize())

