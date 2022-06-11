from re import U
from flask import Blueprint, jsonify, abort, request
from ..models import Artist, Artwork, Artist_Account, Category, Collector, Collector_Account,  db, categories_table
import hashlib
import secrets

bp = Blueprint('artworks', __name__, url_prefix='/artworks')

@bp.route('', methods=['GET']) 
def index():
    artworks = Artwork.query.all() 
    result = []
    for a in artworks:
        result.append(a.serialize())
    return jsonify(result)

@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    a = Artwork.query.get_or_404(id)
    return jsonify(a.serialize())