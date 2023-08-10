from flask import Blueprint
from app.models import Book, db
from flask_login import current_user, login_required


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
