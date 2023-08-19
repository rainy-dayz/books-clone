from app.models import db, User, Like,WishList,environment, SCHEMA,Book,Genre,Review,Cart,SubGenre
from sqlalchemy.sql import text
from datetime import datetime


# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(
        username='Demo', firstName='Demo', lastName='Lition',email='demo@aa.io', password='password')
    marnie = User(
        username='marnie', firstName='Marnie', lastName='Here', email='marnie@aa.io', password='password')
    bobbie = User(
        username='bobbie', firstName='Bobbie', lastName='Chef', email='bobbie@aa.io', password='password')
    genre1=Genre(name="Fantasy")
    genre2=Genre(name="SciFi")
    genre3=Genre(name="Romance")
    genre4=Genre(name="Thriller")
    genre5=Genre(name="Manga")
    subgenre1=SubGenre(name="Historical")
    subgenre2=SubGenre(name="Magical Realism")
    subgenre3=SubGenre(name="Magic School")
    subgenre4=SubGenre(name="Cozy Fantasy")
    subgenre5=SubGenre(name="Heist")
    subgenre6=SubGenre(name="Shonen")
    subgenre7=SubGenre(name="Shojo")
    subgenre8=SubGenre(name="Comedy")
    subgenre9=SubGenre(name="Sports")
    subgenre10=SubGenre(name="Dystopian?Apocolyptic")
    subgenre11=SubGenre(name="Robots/AI")
    subgenre12=SubGenre(name="Aliens")
    subgenre13=SubGenre(name="Time Travel/Multiverse")
    subgenre14=SubGenre(name="Historical")
    subgenre15=SubGenre(name="Contemporary")
    subgenre16=SubGenre(name="Rom-Com")
    subgenre17=SubGenre(name="Fantasy/SciFi")
    subgenre18=SubGenre(name="Fantasy")
    subgenre19=SubGenre(name="Horror")
    subgenre20=SubGenre(name="Mystery")
    book1=Book(
        name="JuJutsu Kaisen Vol.1", author='Gege Akutami',price=8.99, description='A boy with already supernatural powers is thrust into the limelight when he becomes the perfect vessel for a powerful demon',
        genre_id=5,book_image="https://www.anime-planet.com/images/manga/covers/jujutsu-kaisen-24477.jpg",types=True,releaseDate=datetime(2023, 8, 8),subgenre_id=6)
    book2=Book(
        name="Project Hail Mary", author='Andy Weir',price=20.99, description='Humanities last hope is a Science Teacher with amnesia in space',
        genre_id=2,book_image="https://bookandfilmglobe.com/wp-content/uploads/2021/05/91Bd7P8UwxL.jpg",types=False,releaseDate=datetime(2023, 8, 5),subgenre_id=12)
    book3=Book(
        name="Pet", author='Akwaeke Emezi',price=10.99, description='The monsters have come back',
        genre_id=1,book_image="https://blackwells.co.uk/jacket/l/9780571355112.jpg",types=False,releaseDate=datetime(2023, 8, 8),subgenre_id=2)
    book4=Book(
        name="The Duchess Deal", author='Tessa Dare',price=5.99, description='A marriage of convenience will may turn into more',
        genre_id=3,book_image="https://booktrib.com/wp-content/uploads/2017/07/The-Duchess-Deal.jpg",types=False,releaseDate=datetime(2023, 8, 6),subgenre_id=14)
    book5=Book(
        name="Monday's Not Coming", author='Tiffany D. Jackson',price=15.99, description='Her best friend is missing and no one seems to care',
        genre_id=4,book_image="https://d1ldy8a769gy68.cloudfront.net/300/978/006/242/267/5/9780062422675.jpg",types=False,releaseDate=datetime(2023, 8, 2),subgenre_id=20)
    book6=Book(
        name="The Wild Ones", author='Nafiza Azad',price=13.99, description='A group of girls with magic power must save their creator before all is lost',
        genre_id=1,book_image="https://d28hgpri8am2if.cloudfront.net/book_images/onix/cvr9781534484962/the-wild-ones-9781534484962_xlg.jpg",types=False,releaseDate=datetime(2023, 8, 8),subgenre_id=2)
    book7=Book(
        name="Finna", author='Nino Cipri',price=8.99, description='When an elderly customer at a big box furniture store slips through a portal to another dimension, it’s up to two minimum-wage employees to track her across the multiverse and protect their company’s bottom line.',
        genre_id=2,book_image="https://media.s-bol.com/Jqvk9BoDGQOg/525x840.jpg",types=False,releaseDate=datetime(2023, 10, 8),subgenre_id=13)
    book8=Book(
        name="That Time I Got Drunk and Saved a Demon", author='Kimberly Lemming',price=10.99, description="After saving a demon Cinn's whole world is turned upside down and she must now embark on a quest that will change everything",
        genre_id=3,book_image="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1627439923i/58648147.jpg",types=False,releaseDate=datetime(2023, 8, 8),subgenre_id=17)
    book9=Book(
        name="Ace of Spades", author='Faridah Abike-Iyimide',price=20.99, description='Gossip Girl meets Get Out',
        genre_id=4,book_image="https://images2.minutemediacdn.com/image/fetch/w_2000,h_2000,c_fit/https://culturess.com/files/image-exchange/2017/07/ie_67345.jpeg",types=False,releaseDate=datetime(2023, 5, 8),subgenre_id=20)
    book10=Book(
        name="Assassination Classroom, Vol.1", author='Yusei Matsui',price=5.99, description="The students in Class 3-E of Kunugigaoka Junior High have a new teacher: an alien octopus with bizarre powers and unlimited strength, who's just destroyed the moon and is threatening to destroy the earth - unless they can kill him first!",
        genre_id=5,book_image="http://www.capsulecomputers.com.au/wp-content/uploads/2015/01/assassination-classroom-volume-1-cover.png",types=True,releaseDate=datetime(2023, 10, 7),subgenre_id=8)
    book11=Book(
        name="Down Among the Sticks and Bones", author='Seanan McGuire',price=14.99, description='What would happen is alice had fallen not into wonderland, but somewhere much darker',
        genre_id=4,book_image="https://images-na.ssl-images-amazon.com/images/I/A1DfuuJpEjL.jpg",types=False,releaseDate=datetime(2023, 10, 8),subgenre_id=18)
    book12=Book(
        name="Every heart a Doorway", author='Seanan McGuire',price=14.99, description='What happens to the children that came back from their adventures in wonderland',
        genre_id=4,book_image="https://www.blackgate.com/wp-content/uploads/2017/05/Every-Heart-a-Doorway_Seanan-McGuire.jpg",types=False,releaseDate=datetime(2023, 10, 8),subgenre_id=18)
    book13=Book(
        name="The Bone Witch", author='Rin Chupeco',price=11.99, description="Tea can raise the dead, but resurrection comes at a price. When Tea accidentally resurrects her brother from the dead, she learns she is different from the other witches in her family. Her gift for necromancy means that she's a bone witch, a title that makes her feared and ostracized by her community.",
        genre_id=1,book_image="https://i.pinimg.com/originals/f6/53/b7/f653b79712f80898e257f1f66ac06923.jpg",types=False,releaseDate=datetime(2020, 2, 6),subgenre_id=3)
    book14=Book(
        name="Legends & Lattes", author='Travis Baldree',price=9.99, description='The battle-weary orc aims to start fresh, opening the first ever coffee shop in the city of Thune. But old and new rivals stand in the way of success — not to mention the fact that no one has the faintest idea what coffee actually is.',
        genre_id=1,book_image="https://m.media-amazon.com/images/I/51OazXen1ZL._SY346_.jpg",types=False,releaseDate=datetime(202, 6, 7),subgenre_id=4)
    book15=Book(
        name="Six of Crows", author='Leigh Bardugo',price=14.95, description="A convict with a thirst for revenge. A sharpshooter who can't walk away from a wager. A runaway with a privileged past. A spy known as the Wraith. A Heartrender using her magic to survive the slums. A thief with a gift for unlikely escapes. Six dangerous outcasts. One impossible heist. Kaz's crew is the only thing that might stand between the world and destruction - if they don't kill each other first.",
        genre_id=1,book_image="https://thebookishlibra.com/wp-content/uploads/2017/06/six-of-crows.jpg",types=False,releaseDate=datetime(2015, 9, 25),subgenre_id=5)
    book16=Book(
        name="The Guilded Wolves", author='Roshani Chokshi',price=13.99, description="To find the ancient artifact the Order seeks, Séverin will need help from a band of experts: an engineer with a debt to pay; a historian who can't yet go home; a dancer with a sinister past; and a brother in all but blood who might care too much. Together, they'll have to use their wits and knowledge to hunt the artifact through the dark and glittering heart of Paris. What they find might change the world, but only if they can stay alive.",
        genre_id=1,book_image="https://media.npr.org/assets/bakertaylor/covers/t/the-gilded-wolves/9781250144546_custom-ce38bc9584f5780361ff03eec2c97854c49650da-s300.jpg",types=False,releaseDate=datetime(2023, 10, 8),subgenre_id=5)
    book17=Book(
        name="Fruit's Basket", author='Natsuki Takaya ',price=6.99, description="After a family tragedy turns her life upside down, plucky high schooler Tohru Honda takes matters into her own hands and moves out...into a tent! Unfortunately for her, she pitches her new home on private land belonging to the mysterious Sohma clan, and it isn't long before the owners discover her secret. But, as Tohru quickly finds out when the family offers to take her in, the Sohmas have a secret of their own--when touched by the opposite sex, they turn into the animals of the Chinese Zodiac!",
        genre_id=5,book_image="https://images-na.ssl-images-amazon.com/images/I/41flDadak8L.jpg",types=True,releaseDate=datetime(2016, 6, 28),subgenre_id=7)
    book18=Book(
        name="Demon Slayer", author='Koyoharu Gotouge',price=6.49, description='After his sister is turned into a demon Tanjiro must become a demon slayter to protect her, while he hunts for a cure.',
        genre_id=5,book_image="https://pictures.abebooks.com/isbn/9781974700523-us.jpg",types=True,releaseDate=datetime(2023, 10, 8),subgenre_id=6)
    book19=Book(
        name="Haikyuu!!", author='Haruichi Furudate',price=10.99, description="Shoyo Hinata is out to prove that in volleyball you don't need to be tall to fly!",
        genre_id=5,book_image="https://m.media-amazon.com/images/I/8125DI58M+L.jpg",types=True,releaseDate=datetime(2016, 7, 5),subgenre_id=9)
    book20=Book(
        name="This is How you Lose a Time War", author='Amal El-Mohtar',price=12.99, description='omantic novel spanning time and space about two time-traveling rivals who fall in love and must change the past to ensure their future',
        genre_id=2,book_image="https://miro.medium.com/max/3376/1*Lq6IjJBbSxvTn1jJY7U1Zg.jpeg",types=False,releaseDate=datetime(2019, 7, 16),subgenre_id=13)
    book21=Book(
        name="The Poppy War", author='R.F. Kuang',price=14.99, description='When Rin passes the entrance exams to the most elite military school in the Empire, she sets off a chain reaction that will change everything',
        genre_id=1,book_image="https://images.booksense.com/images/569/662/9780062662569.jpg",types=False,releaseDate=datetime(2018, 5, 1),subgenre_id=1)
    book22=Book(
        name="Eat Your Heart Out", author='Kelly DeVos',price=14.99, description="In the next few hours, one of three things will happen: 1. We'll be rescued (unlikely), 2.We'll freeze to death (maybe), 3. We'll be eaten by thin and athletic zombies (odds: excellent)",
        genre_id=2,book_image="https://stockeduponstarbooks.files.wordpress.com/2021/06/eat-your-heart-out-book-cover.jpg",types=False,releaseDate=datetime(2021, 6, 8),subgenre_id=10)
    book23=Book(
        name="Psalm of the Wild-Built", author='Becky Chambers',price=7.99, description='A Tea Monk meets a robot and talk about the universe',
        genre_id=2,book_image="https://blackwells.co.uk/jacket/l/9781250236210.jpg",types=False,releaseDate=datetime(2021, 7, 13),subgenre_id=11)
    book24=Book(
        name="Beach Read", author='Emily Henry',price=14.99, description='A romance writer who no longer believes in love and a literary writer stuck in a rut engage in a summer-long challenge that may just upend everything they believe about happily ever afters.',
        genre_id=3,book_image="https://s3.amazonaws.com/betches/app/uploads/2020/01/14163202/9781984806734.jpg",types=False,releaseDate=datetime(2020, 5, 19),subgenre_id=15)
    book25=Book(
        name="Get a Life, Chloe Brown", author='Talia Hibbert',price=14.99, description="A woman who’s tired of being “boring” recruits her mysterious, sexy neighbor to help her experience new things.",
        genre_id=3,book_image="https://i.pinimg.com/736x/cd/5b/45/cd5b45bfa8007d0d06f9925e65c58ae4.jpg",types=False,releaseDate=datetime(2019, 11, 5),subgenre_id=16)
    book26=Book(
        name="Heart, Haunt, Havoc", author='Freydis Moon',price=13.99, description="When lonely transgender exorcist, Colin Hart, finds himself challenged by an unruly haunted house in Gideon, Colorado, he’s kept awake by ghosts, demons, ghouls, and the handsome nonbinary owner of the house, Bishop Martínez.",
        genre_id=4,book_image="https://m.media-amazon.com/images/I/41NDcxAaN9L._SY346_.jpg",types=False,releaseDate=datetime(2023, 1, 8),subgenre_id=19)
    book27=Book(
        name="The Weight of Blood", author='Tiffany D. Jackson',price=12.99, description='When Springville residents—at least the ones still alive—are questioned about what happened on prom night, they all have the same explanation . . . Maddy did it.',
        genre_id=4,book_image="https://img1.wsimg.com/isteam/ip/1929e432-2d9e-4d82-b4c4-81f5d4ca704f/ols/711liwd6s4L.jpg",types=False,releaseDate=datetime(2022, 10, 8),subgenre_id=19)
    book28=Book(
        name="The Red Palace", author='June Hur',price=14.99, description='A palace nurse must solve a string of murders and what connects them before time runs out',
        genre_id=4,book_image="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1616437004i/56978115.jpg",types=False,releaseDate=datetime(2022, 1, 25),subgenre_id=20)
    book29=Book(
        name="Red, White & Royal Blue", author='Casey McQuiston',price=14.99, description="What happens when America's First Son falls in love with the Prince of Wales?",
        genre_id=3,book_image="https://prodimage.images-bn.com/pimages/9781250316776_p0_v6_s1200x630.jpg",types=False,releaseDate=datetime(2019, 5, 14),subgenre_id=16)
    book30=Book(
        name="A Deadly Education", author='Naomi Novik',price=14.99, description='A school for the magically gifted where failure means certain death (for real) — until one girl, El, begins to unlock its many secrets.',
        genre_id=1,book_image="https://utopia-state-of-mind.com/wp-content/uploads/2020/10/A-Deadly-Education-683x1024.jpg",types=False,releaseDate=datetime(2020, 10, 8),subgenre_id=3)
    wishlist1=WishList(
        user_id=1,book_id=1
    )
    wishlist2=WishList(
        user_id=1,book_id=3
    )
    review1=Review(
        comment="Mid at best i mean come on",rating=3,user_id=1, book_id=1,created_at=datetime(2010, 10, 5),user_username='Demo'
    )
    review2=Review(
        comment="Best SciFi book ever.",rating=5,user_id=2, book_id=2,created_at=datetime(2021, 9, 6),user_username='marnie'
    )
    review3=Review(
        comment="This is the best!!!!",rating=5,user_id=2, book_id=3,created_at=datetime(2015, 11, 5),user_username='marnie'
    )
    review4=Review(
        comment="Romace was super cute",rating=4,user_id=1, book_id=4,created_at=datetime(2020, 7, 15),user_username='Demo'
    )
    review5=Review(
        comment="This book was so dark and the twists were amazing! Kept me on the edge of my seat",rating=4,user_id=1, book_id=5,created_at=datetime(2022, 11, 15),user_username='Demo'
    )
    review6=Review(
        comment="This book was amazing!",rating=5,user_id=2, book_id=9,created_at=datetime(2015, 10, 25),user_username='marnie'
    )
    review7=Review(
        comment="This book was amazing!",rating=5,user_id=2, book_id=1,created_at=datetime(2015, 10, 25),user_username='marnie'
    )
    # like1=Like(
    #     user_id=2,review_id=1
    # )
    # like2=Like(
    #     user_id=1,review_id=2
    # )
    # like3=Like(
    #     user_id=3,review_id=2
    # )
    # like4=Like(
    #     user_id=3,review_id=1
    # )
    # like5=Like(
    #     user_id=1,review_id=3
    # )

    db.session.add(demo)
    db.session.add(marnie)
    db.session.add(bobbie)
    db.session.add_all([genre1,genre2,genre3,genre4,genre5])
    db.session.add_all([subgenre1,subgenre2,subgenre3,subgenre4,subgenre5,subgenre6,subgenre7,subgenre8,subgenre9,subgenre10,
                        subgenre11,subgenre12,subgenre13,subgenre14,subgenre15,subgenre16,subgenre17,subgenre18,subgenre19,subgenre20])
    db.session.add_all([book1,book2,book3,book4,book5,book6,book7,book8,book9,book10,
                        book11,book12,book13,book14,book15,book16,book17,book18,book19,book20,
                        book21,book22,book23,book24,book25,book26,book27,book28,book29,book30])
    db.session.add_all([review1,review2,review3,review4,review5,review6,review7])
    db.session.add_all([ wishlist1,wishlist2])
    # db.session.add_all([ like1,like2,like3,like4,like5])
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.carts RESTART IDENTITY CASCADE;")
        db.session.execute(f"TRUNCATE table {SCHEMA}.wishlist RESTART IDENTITY CASCADE;")
        db.session.execute(f"TRUNCATE table {SCHEMA}.likes RESTART IDENTITY CASCADE;")
        db.session.execute(f"TRUNCATE table {SCHEMA}.reviews RESTART IDENTITY CASCADE;")
        db.session.execute(f"TRUNCATE table {SCHEMA}.subgenres RESTART IDENTITY CASCADE;")
        db.session.execute(f"TRUNCATE table {SCHEMA}.genres RESTART IDENTITY CASCADE;")
        db.session.execute(f"TRUNCATE table {SCHEMA}.books RESTART IDENTITY CASCADE;")
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM carts"))
        db.session.execute(text("DELETE FROM wishlist"))
        db.session.execute(text("DELETE FROM likes"))
        db.session.execute(text("DELETE FROM reviews"))
        db.session.execute(text("DELETE FROM subgenres"))
        db.session.execute(text("DELETE FROM genres"))
        db.session.execute(text("DELETE FROM books"))
        db.session.execute(text("DELETE FROM users"))

    db.session.commit()
