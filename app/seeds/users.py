from app.models import db, User, environment, SCHEMA,Book,Genre,Review
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(
        username='Demo', first_name='Demo', last_name='Lition',email='demo@aa.io', password='password')
    marnie = User(
        username='marnie', first_name='Marnie', last_name='Here', email='marnie@aa.io', password='password')
    bobbie = User(
        username='bobbie', first_name='Bobbie', last_name='Chef', email='bobbie@aa.io', password='password')
    genre1=Genre(name="Fantasy")
    genre2=Genre(name="SciFi")
    genre3=Genre(name="Romance")
    genre4=Genre(name="Thriller")
    genre5=Genre(name="Manga")
    book1=Book(
        name="JuJutsu Laisen Vol.1", author='Gege Akutami',price=8.99, description='A boy with already supernatural powers is thrust into the limelight when he becomes the perfect vessel for a powerful demon',
        genre_id=5,book_image="https://www.anime-planet.com/images/manga/covers/jujutsu-kaisen-24477.jpg")
    book2=Book(
        name="Project Hail Mary", author='Andy Weir',price=20.99, description='Humanities last hope is a Science Teacher with amnesia in space',
        genre_id=2,book_image="https://bookandfilmglobe.com/wp-content/uploads/2021/05/91Bd7P8UwxL.jpg")
    book3=Book(
        name="Pet", author='Akwaeke Emezi',price=10.99, description='The monsters have come back',
        genre_id=1,book_image="https://blackwells.co.uk/jacket/l/9780571355112.jpg")
    book4=Book(
        name="The Duchess Deal", author='Tessa Dare',price=5.99, description='A marriage of convenience will may turn into more',
        genre_id=3,book_image="https://booktrib.com/wp-content/uploads/2017/07/The-Duchess-Deal.jpg")
    book5=Book(
        name="Monday's Not Coming", author='Tiffany D. Jackson',price=15.99, description='Her best friend is missing and no one seems to care',
        genre_id=4,book_image="https://d1ldy8a769gy68.cloudfront.net/300/978/006/242/267/5/9780062422675.jpg")
    book6=Book(
        name="The Wild Ones", author='Nafiza Azad',price=13.99, description='A group of girls with magic power must save their creator before all is lost',
        genre_id=1,book_image="https://d28hgpri8am2if.cloudfront.net/book_images/onix/cvr9781534484962/the-wild-ones-9781534484962_xlg.jpg")
    book7=Book(
        name="Finna", author='Nino Cipri',price=8.99, description='When an elderly customer at a big box furniture store slips through a portal to another dimension, it’s up to two minimum-wage employees to track her across the multiverse and protect their company’s bottom line.',
        genre_id=2,book_image="https://media.s-bol.com/Jqvk9BoDGQOg/525x840.jpg")
    book8=Book(
        name="That Time I Got Drunk and Saved a Demon", author='Kimberly Lemming',price=10.99, description="After saving a demon Cinn's whole world is turned upside down and she must now embark on a quest that will change everything",
        genre_id=3,book_image="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1627439923i/58648147.jpg")
    book9=Book(
        name="Ace of Spades", author='Faridah Àbíké-Íyímídé',price=20.99, description='Gossip Girl meets Get Out',
        genre_id=4,book_image="https://images2.minutemediacdn.com/image/fetch/w_2000,h_2000,c_fit/https://culturess.com/files/image-exchange/2017/07/ie_67345.jpeg")
    book10=Book(
        name="Assassination Classroom, Vol.1", author='Yūsei Matsui',price=5.99, description="The students in Class 3-E of Kunugigaoka Junior High have a new teacher: an alien octopus with bizarre powers and unlimited strength, who's just destroyed the moon and is threatening to destroy the earth - unless they can kill him first!",
        genre_id=5,book_image="http://www.capsulecomputers.com.au/wp-content/uploads/2015/01/assassination-classroom-volume-1-cover.png")
    book11=Book(
        name="Down Among the Sticks and Bones", author='Seanan McGuire',price=14.99, description='What would happen is alice had fallen not into wonderland, but somewhere much darker ',
        genre_id=4,book_image="https://images-na.ssl-images-amazon.com/images/I/A1DfuuJpEjL.jpg")
    review1=Review(
        comment="Mid",rating=3.5,user_id=1, book_id=1
    )
    review2=Review(
        comment="Best SciFi book ever.",rating=5,user_id=2, book_id=2
    )
    review3=Review(
        comment="This is the best",rating=5,user_id=2, book_id=3
    )
    review4=Review(
        comment="Romace was supre cute",rating=4.5,user_id=1, book_id=4
    )
    review5=Review(
        comment="This book was so dark and the twists were amazing! Kept me on the edge of my seat",rating=4,user_id=1, book_id=5
    )
    review6=Review(
        comment="This book was amazing!",rating=5,user_id=2, book_id=1
    )
    db.session.add(demo)
    db.session.add(marnie)
    db.session.add(bobbie)
    db.session.add_all([genre1,genre2,genre3,genre4,genre5])
    db.session.add_all([book1,book2,book3,book4,book5,book6,book7,book8,book9,book10,book11])
    db.session.add_all([review1,review2,review3,review4,review5,review6])
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.reviews RESTART IDENTITY CASCADE;")
        db.session.execute(f"TRUNCATE table {SCHEMA}.genres RESTART IDENTITY CASCADE;")
        db.session.execute(f"TRUNCATE table {SCHEMA}.books RESTART IDENTITY CASCADE;")
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM reviews"))
        db.session.execute(text("DELETE FROM genres"))
        db.session.execute(text("DELETE FROM books"))
        db.session.execute(text("DELETE FROM users"))

    db.session.commit()
