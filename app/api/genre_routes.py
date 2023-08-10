from flask import Blueprint, jsonify
# from flask_login import current_user, login_required

from app.models import Genre, db

genres_routes = Blueprint('genres', __name__)


@genres_routes.route('/')
def get_all_genres():
    genres = Genre.query.all()
    return [genre.to_dict() for genre in genres]


@genres_routes.route('/<int:id>')
def get_single_genre(id):
    genre = Genre.query.get(id)
    return genre.to_dict()
