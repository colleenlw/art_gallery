from re import U
from flask import Blueprint, jsonify, abort, request
from ..models import Artist, Artwork, Artist_Account, Category, Collector, Collector_Account,  db, categories_table
import hashlib
import secrets

bp = Blueprint('collector_accounts', __name__, url_prefix='/collector_accounts')