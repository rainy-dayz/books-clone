from flask import Blueprint, request, jsonify
from app.models import Cart,db, Book, User
from flask_login import current_user, login_required
from app.forms.cart_form import CartForm

carts_routes = Blueprint('carts', __name__)


@carts_routes.route('/user_cart')
@login_required
def get_orders():
    # user_cart = Cart.query.filter_by(user_id=current_user.id).all()
    carts = Cart.query.filter_by(user_id=current_user.id).all()
    # print(carts)

    return [cart.to_dict() for cart in carts]


@carts_routes.route("/<int:userId>/<int:bookId>", methods=["POST"])
@login_required
def create_order(userId,bookId):
    form = CartForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        cart = Cart(
            user_id=userId,
            book_id=bookId,
            quantity=1
        )
        # print('backend-----------',channel)
        db.session.add(cart)
        db.session.commit()
        return cart.to_dict()
    return {'errors': 'error'}, 401

@carts_routes.route("/delete/<int:cartId>", methods=['GET','POST','DELETE'])
@login_required
def delete_post(cartId):
  cart_to_delete = Cart.query.get(cartId)
  db.session.delete(cart_to_delete)
  db.session.commit()
  return {'message':'deleted'}

@carts_routes.route('/edit/<int:cartId>', methods=['GET','POST','PUT'])
@login_required
def edit_channel(cartId):
    form = CartForm()
    cart = Cart.query.get(cartId)
    form['csrf_token'].data = request.cookies['csrf_token']
    cart.quantity = form.data['quantity']
    if int(form.data['quantity']) < 1:
        db.session.delete(cart)
        db.session.commit()
        return {'message':'removed from cart'}
    db.session.commit()
    return cart.to_dict()

@carts_routes.route('/<int:cartId>')
@login_required
def single_channel(cartId):
    cart = Cart.query.get(cartId)
    # channel=Channel.query.all()
    # print('backend chanel--------------', channel.to_dict())
    return cart.to_dict()

@carts_routes.route('/delete/cart')
def delete_whole_cart():
    carts = Cart.query.filter_by(user_id=current_user.id).all()
    db.session.delete(carts)
    db.session.commit()
    return {'message':'deleted'}
