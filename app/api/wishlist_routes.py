from flask import Blueprint, request, jsonify
from app.models import Cart,db, Book, User,WishList
from flask_login import current_user, login_required
from app.forms.wishlist_form import WishForm


wishlists_routes = Blueprint('wishlists', __name__)


@wishlists_routes.route('/wishlist')
@login_required
def wishlist():
     wishlists = WishList.query.filter_by(user_id=current_user.id).all()
     return [wish.to_dict() for wish in wishlists]


@wishlists_routes.route('/<int:userId>/<int:bookId>', methods=['POST'])
@login_required
def create_WishList(userId,bookId):
    form = WishForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        wishlist = WishList(
            user_id=userId,
            book_id=bookId,
        )
        db.session.add(wishlist)
        db.session.commit()
        return wishlist.to_dict()
    return {'errors': 'error'}, 401



@wishlists_routes.route("/delete/<int:wishlistId>", methods=['GET','POST','DELETE'])
@login_required
def delete_post(wishlistId):
  wish_to_delete = WishList.query.get(wishlistId)
  db.session.delete(wish_to_delete)
  db.session.commit()
  return {'message':'deleted'}

# @wishlists_routes.route('/edit/<int:wishlistId>', methods=['GET','POST','PUT'])
# @login_required
# def edit_wish(wishlistId):
#     form = WishForm()
#     wishlist = WishList.query.get(wishlistId)
#     form['csrf_token'].data = request.cookies['csrf_token']
#     wishlist.name = form.data['name']

#     db.session.commit()
#     return wishlist.to_dict()


# @wishlists_routes.route('/<int:wishlistId>')
# @login_required
# def single_wishlist(wishlistId):
#     wishlist = WishList.query.get(wishlistId)
#     return wishlist.to_dict()
