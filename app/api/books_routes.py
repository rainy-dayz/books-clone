from flask import Blueprint, request, jsonify
from app.models import Book, db
from flask_login import current_user, login_required
from app.forms.book_form import BookForm

books_routes = Blueprint('books', __name__)


@books_routes.route('/')
def get_all_books():
    books = Book.query.all()
    return [boo.to_dict() for boo in books]


@books_routes.route('/<int:id>')
def get_book(id):
    book = Book.query.get(id)
    print('----------------------------------------------',book)
    return book.to_dict()

@books_routes.route('/update/<int:bookId>', methods=['GET','POST','PUT'])
def update_book(bookId):
    form = BookForm()
    book = Book.query.get(bookId)
    form['csrf_token'].data = request.cookies['csrf_token']
    book.types= form.data['types']
    db.session.commit()
    return book.to_dict()
    return {'errors': 'error'}, 401

@books_routes.route('/filter/price')
def filter_books():
    books=Book.query.order_by(Book.price).all()

    return [boo.to_dict() for boo in books]
