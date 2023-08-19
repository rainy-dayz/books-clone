from flask import Blueprint, request, jsonify
from app.models import Cart,db, Book, User,WishList,Like
from flask_login import current_user, login_required
from .auth_routes import authenticate

# from app.forms.wishlist_form import WishForm


likes_routes = Blueprint('likes', __name__)


@likes_routes.route('/<int:reviewId>')
# @login_required
def all_likes(reviewId):
     likes = Like.query.filter_by(review_id=reviewId).all()
     return [like.to_dict() for like in likes]


@likes_routes.route('/<int:reviewId>/new', methods=['POST'])
@login_required
def like(reviewId):
    auth = authenticate()

    like = Like(user_id=auth['id'], review_id=reviewId)
    db.session.add(like)
    db.session.commit()
    return like.to_dict()




@likes_routes.route('/delete/<int:likeId>',methods=['DELETE'])
@login_required
def delete_like(likeId):
    like_to_delete = Like.query.get(likeId)

    db.session.delete(like_to_delete)
    db.session.commit()
    return {"message": "Successfully deleted"}
