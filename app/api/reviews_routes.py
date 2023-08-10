from flask import Blueprint, request, jsonify
from app.models import Cart,db, Book, User,Review
from flask_login import current_user, login_required
from app.forms.review_form import ReviewForm

reviews_routes = Blueprint('reviews', __name__)


@reviews_routes.route('/<int:bookId>')

def get_reviews(bookId):
    reviews = Review.query.filter(Review.book_id ==bookId)

    return [review.to_dict() for review in reviews]


@reviews_routes.route("/<int:userId>/<int:bookId>", methods=["POST"])
# @login_required
def create_review(userId,bookId):
    form = ReviewForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        review = Review(
            comment=form.data['comment'],
            rating= form.data['rating'],
            user_id=userId,
            book_id=bookId,

        )

        db.session.add(review)
        db.session.commit()
        return review.to_dict()
    return {'errors': 'error'}, 401

@reviews_routes.route("/delete/<int:reviewId>", methods=['GET','POST','DELETE'])
# @login_required
def delete_post(reviewId):
  review_to_delete = Review.query.get(reviewId)
  db.session.delete(review_to_delete)
  db.session.commit()
  return {'message':'deleted'}

@reviews_routes.route('/edit/<int:reviewId>', methods=['PUT'])
# @login_required
def edit_review(reviewId):
    form = ReviewForm()
    review=Review.query.get(reviewId)
    form['csrf_token'].data = request.cookies['csrf_token']

    review.comment=form.data['comment']
    review.rating=form.data['rating']

    db.session.commit()
    return review.to_dict()
@reviews_routes.route('/<int:reviewId>')

def single_review(reviewId):
    review = Review.query.get(reviewId)
    # channel=Channel.query.all()
    # print('backend chanel--------------', channel.to_dict())
    return review.to_dict()
