from app.models import db, User, Like,WishList,environment, SCHEMA,Book,Genre,Review,Cart,SubGenre
from sqlalchemy.sql import text
from datetime import datetime


# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(
        username='Demo', firstName='Demo', lastName='Lition',email='demo@aa.io', password='password')
    marnie = User(
        username='marnie', firstName='Marnie', lastName='Here', email='marnie@aa.io', password='password')
    rory = User(
        username='lone_centurion', firstName='Rory', lastName='Williams', email='rory@aa.io', password='password')
    donna = User(
        username='the_bride', firstName='Donna', lastName='Noble', email='donna@aa.io', password='password')
    amy = User(
        username='pandorica', firstName='Amy', lastName='Pond', email='amy@aa.io', password='password')
    rose = User(
        username='bad_wolf', firstName='Rose', lastName='Tyler', email='rose@aa.io', password='password')
    river = User(
        username='melody', firstName='River', lastName='Song', email='river@aa.io', password='password')
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
        name="JuJutsu Kaisen", author='Gege Akutami',price=8.99, description='A boy with already supernatural powers is thrust into the limelight when he becomes the perfect vessel for a powerful demon',
        genre_id=5,book_image="https://www.anime-planet.com/images/manga/covers/jujutsu-kaisen-24477.jpg",types=True,releaseDate=datetime(2023, 8, 8),subgenre_id=6)
    book2=Book(
        name="Project Hail Mary", author='Andy Weir',price=20.99, description='Humanities last hope is a Science Teacher with amnesia in space',
        genre_id=2,book_image="https://bookandfilmglobe.com/wp-content/uploads/2021/05/91Bd7P8UwxL.jpg",types=False,releaseDate=datetime(2023, 8, 5),subgenre_id=12)
    book3=Book(
        name="Pet", author='Akwaeke Emezi',price=10.99, description='The monsters have come back',
        genre_id=1,book_image="https://blackwells.co.uk/jacket/l/9780571355112.jpg",types=False,releaseDate=datetime(2023, 8, 8),subgenre_id=2)
    book4=Book(
        name="The Duchess Deal", author='Tessa Dare',price=5.99, description='Since his return from war, the Duke of Ashbury’s to-do list has been short and anything but sweet: brooding, glowering, menacing London ne’er-do-wells by night. Now there’s a new item on the list. He needs an heir—which means he needs a wife. When Emma Gladstone, a vicar’s daughter turned seamstress, appears in his library wearing a wedding gown, he decides on the spot that she’ll do.',
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
        name="Assassination Classroom", author='Yusei Matsui',price=5.99, description="The students in Class 3-E of Kunugigaoka Junior High have a new teacher: an alien octopus with bizarre powers and unlimited strength, who's just destroyed the moon and is threatening to destroy the earth - unless they can kill him first!",
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
        genre_id=1,book_image="https://m.media-amazon.com/images/I/51OazXen1ZL._SY346_.jpg",types=False,releaseDate=datetime(2023, 6, 7),subgenre_id=4)
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
    book31=Book(
        name="Foundryside", author='Robert Jackson Bennett',price=14.95, description='In a city that runs on industrialized magic, a secret war will be fought to overwrite reality itself',
        genre_id=1,book_image="https://i.pinimg.com/736x/b2/a0/56/b2a056897a5d7dbab7e233a36998f929.jpg",types=False,releaseDate=datetime(2018,8,21))
    book32=Book(
        name="A Dowry of Blood", author='S.T. Gibson',price=14.95, description="A lyrical and dreamy reimagining of Dracula's brides, A Dowry of Blood is a story of desire, obsession, and emancipation.",
        genre_id=1,book_image="https://booktriggerwarnings.com/images/thumb/7/78/A_Dowry_of_Blood_by_S.T._Gibson.jpg/200px-A_Dowry_of_Blood_by_S.T._Gibson.jpg",types=False,releaseDate=datetime(2021,4,20))
    book33=Book(
        name="Daughter of the Moon Goddess", author='Sue Lyn Tan',price=14.95, description="A captivating debut fantasy inspired by the legend of the Chinese moon goddess, Chang’e, in which a young woman’s quest to free her mother pits her against the most powerful immortal in the realm and sets her on a dangerous path - where choices come with deadly consequences, and she risks losing more than her heart.",
        genre_id=1,book_image="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1627686439l/57789637.jpg",types=False,releaseDate=datetime(2022,1,11))
    book34=Book(
        name="A Darker Shade of Magic", author='V.E. Schwab',price=14.95, description="Kell is one of the last Travelers - magicians with a rare, coveted ability to travel between parallel universes. As such, he can choose where he lands. There's Grey London, dirty and boring, without any magic, ruled by a mad King George. Then there's Red London, where life and magic are revered, and the Maresh Dynasty presides over a flourishing empire. There's White London, ruled by whoever has murdered their way to the throne. And once upon a time, there was Black London...but no one speaks of that now. ",
        genre_id=1,book_image="https://bookstacked.com/wp-content/uploads/2015/04/A-Darker-Shade-of-Magic-Cover.jpg",types=False,releaseDate=datetime(2020,2,15))
    book35=Book(
        name="For the Wolf", author='Hannah Whitten',price=14.95, description="A young woman who must be sacrificed to the legendary Wolf of the Wood to save her kingdom. But not all legends are true, and the Wolf isn't the only danger lurking in the Wilderwood.",
        genre_id=1,book_image="https://cdn.waterstones.com/bookjackets/large/9780/3565/9780356516363.jpg",types=False,releaseDate=datetime(2021,6,1))
    book36=Book(
        name="The Never Tilting World", author='Rin Chupeco',price=14.90, description="Generations of twin goddesses have long ruled Aeon - until one sister’s betrayal split their world in two. A Great Abyss now divides two realms: one cloaked in eternal night, the other scorched beneath an ever-burning sun. While one sister rules the frozen fortress of Aranth, her twin rules the sand-locked Golden City - each with a daughter by their side. Now those young goddesses must set out on separate, equally dangerous journeys in hopes of healing their broken world. No matter the sacrifice it demands.",
        genre_id=1,book_image="https://utopia-state-of-mind.com/wp-content/uploads/2019/10/the-never-tilting-world-by-rin-chupeco.jpg",types=False,releaseDate=datetime(2023, 8, 8))
    book37=Book(
        name="A Magic Steeped in Poison", author='Judy I. Lin',price=13.99, description="When Ning hears of a competition to find the kingdom's greatest shennong-shi - masters of the ancient and magical art of tea-making - she travels to the imperial city to compete. The winner will receive a favor from the princess, which may be Ning's only chance to save her sister's life. But between the backstabbing competitors, bloody court politics, and a mysterious (and handsome) boy with a shocking secret, Ning might actually be the one in more danger.",
        genre_id=1,book_image="https://mpd-biblio-covers.imgix.net/9781250767080.jpg",types=False,releaseDate=datetime(2022,10,15))
    book38=Book(
        name="Jade City", author='Fonda Lee',price=13.99, description="Jade is the lifeblood of the island of Kekon. It has been mined, traded, stolen, and killed for - and for centuries, honorable Green Bone warriors like the Kaul family have used it to enhance their magical abilities and defend the island from foreign invasion. Now, the war is over and a new generation of Kauls vies for control of Kekon's bustling capital city. They care about nothing but protecting their own, cornering the jade market, and defending the districts under their protection. Ancient tradition has little place in this rapidly changing nation. When a powerful new drug emerges that lets anyone - even foreigners - wield jade, the simmering tension between the Kauls and the rival Ayt family erupts into open violence. The outcome of this clan war will determine the fate of all Green Bones - and of Kekon itself.",
        genre_id=1,book_image="https://prodimage.images-bn.com/pimages/9780316440882_p0_v5_s1200x630.jpg",types=False,releaseDate=datetime(2017,11,7))
    book39=Book(
        name="Fourth Wing", author='Rebecca Yarros',price=15.99, description="Enter the brutal and elite world of a war college for dragon riders.Friends, enemies, lovers. Everyone at Basgiath War College has an agenda—because once you enter, there are only two ways out: graduate or die.",
        genre_id=1,book_image="https://media.s-bol.com/33GL175MwBjQ/8ljn7o/543x840.jpg",types=False,releaseDate=datetime(2023,8,17))
    book40=Book(
        name="Year of the Reaper", author='Makiia Lucier',price=14.95, description=" In the aftermath of a devastating plague, a young lord is determined to discover the truth behind a mysterious attempt to assassinate the young queen.",
        genre_id=1,book_image="http://makiialucier.com/wp-content/uploads/2021/04/413IO2chqZL._SX331_BO1204203200_.jpg",types=False,releaseDate=datetime(2021,11,9))
    book41=Book(
        name="Flame in the Mist", author='Renee Ahdieh',price=13.99, description="The daughter of a prominent samurai, Mariko has long known her place - she may be an accomplished alchemist whose cunning rivals that of her brother, Kenshin, but because she is not a boy, her future has always been out of her hands. At just 17 years old, Mariko is promised to Minamoto Raiden, the son of the emperor's favorite consort - a political marriage that will elevate her family's standing. But en route to the imperial city of Inako, Mariko narrowly escapes a bloody ambush by a dangerous gang of bandits known as the Black Clan, whom she learns has been hired to kill her before she reaches the palace.",
        genre_id=1,book_image="https://i.pinimg.com/originals/6d/aa/a1/6daaa1537ebd801158e608bd30ab0557.jpg",types=False,releaseDate=datetime(2021,11,9))
    book42=Book(
        name="Graceling", author='Kristin Cashore',price=13.18, description="Graceling tells the story of the vulnerable-yet-strong Katsa, who is smart and beautiful and lives in the Seven Kingdoms where selected people are born with a Grace, a special talent that can be anything at all. Katsa’s Grace is killing.",
        genre_id=1,book_image="https://1.bp.blogspot.com/-qPWAG2QFzsY/VWX-VJ-lpyI/AAAAAAAALTU/xFoLbPv3UFY/s1600/Graceling_Frontal.jpg",types=False,releaseDate=datetime(2023,1,10))
    book43=Book(
        name="The Sword of Kaigen", author='M.L. Wong',price=15.39, description="On a mountainside at the edge of the Kaigenese Empire live the most powerful warriors in the world, superhumans capable of raising the sea and wielding blades of ice. For hundreds of years, the fighters of the Kusanagi Peninsula have held the Empire's enemies at bay, earning their frozen spit of land the name 'The Sword of Kaigen'.",
        genre_id=1,book_image="https://www.forewordreviews.com/books/covers/the-sword-of-kaigen.jpg",types=False,releaseDate=datetime(2023, 8, 8))
    book44=Book(
        name="The Fifth Season", author='N.K. Jemisin',price=21.00, description="At the end of the world, a woman must hide her secret power and find her kidnapped daughter.",
        genre_id=1,book_image="https://nkjemisin.com/wp-content/uploads/2015/04/Jemisin_FifthSeason-TP.jpg",types=False,releaseDate=datetime(2015,8,4))
    book45=Book(
        name="The Wolf and the Woodsman", author='Ava Reid',price=17.99, description="A young pagan woman with hidden powers and a one-eyed captain of the Woodsmen form an unlikely alliance to thwart a tyrant. ",
        genre_id=1,book_image="https://www.dreyslibrary.com/wp-content/uploads/2021/05/The-Wolf-and-the-Woodsman-by-Ava-Reid-1356x2048.jpg",types=False,releaseDate=datetime(2021,6,8))
    book46=Book(
        name="The Starless Sea", author='Erin Morgenstern',price=15.86, description="A timeless love story set in a secret underground world - a place of pirates, painters, lovers, liars, and ships that sail upon a starless sea.",
        genre_id=1,book_image="https://dglibrary.org/wp-content/uploads/2020/03/the-starless-sea-2.jpg",types=False,releaseDate=datetime(2015,11,5))
    book47=Book(
        name="The Keeper of Night", author='Kylie Lee Baker',price=12.80, description="Half British Reaper, half Japanese Shinigami, Ren Scarborough has been collecting souls in the London streets for centuries. Expected to obey the harsh hierarchy of the Reapers who despise her, Ren conceals her emotions and avoids her tormentors as best she can. When her failure to control her Shinigami abilities drives Ren out of London, she flees to Japan to seek the acceptance she’s never gotten from her fellow Reapers. ",
        genre_id=1,book_image="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1613417856l/56030267.jpg",types=False,releaseDate=datetime(2021,11,16))
    book48=Book(
        name="Cemetary Boys", author='Aiden Thomas',price=13.95, description="A trans boy determined to prove his gender to his traditional Latinx family summons a ghost who refuses to leave",
        genre_id=1,book_image="https://www.juniorlibraryguild.com/images/9781250250469/CoverArt/9781250250469_zoom.jpg",types=False,releaseDate=datetime(2020,9,1))
    book49=Book(
        name="The Lies of Locke Lamora", author='Scott Lynch',price=18.59, description="An orphan’s life is harsh - and often short - in the mysterious island city of Camorr. But young Locke Lamora dodges death and slavery, becoming a thief under the tutelage of a gifted con artist. As leader of the band of light-fingered brothers known as the Gentleman Bastards, Locke is soon infamous, fooling even the underworld’s most feared ruler. But in the shadows lurks someone still more ambitious and deadly. Faced with a bloody coup that threatens to destroy everyone and everything that holds meaning in his mercenary life, Locke vows to beat the enemy at his own brutal game - or die trying. ",
        genre_id=1,book_image="https://onlinereadfreenovel.com/i2/scott-lynch/the_lies_of_locke_lamora.jpg",types=False,releaseDate=datetime(2019,12,10))
    book50=Book(
        name="Malice", author='John Gwynne',price=22.00, description="The Banished Lands has a violent past where armies of men and giants clashed in battle, but now giants are seen, the stones weep blood, and giant wyrms are stirring. Those who can still read the signs see a threat far greater than the ancient wars. For if the Black Sun gains ascendancy, mankind's hopes and dreams will fall to dust...and it can never be made whole again.",
        genre_id=1,book_image="https://images-na.ssl-images-amazon.com/images/I/81ABoIuRauL.jpg",types=False,releaseDate=datetime(2012,8,13))
    book51=Book(
        name="Mistborn", author='Brandon Sanderson',price=15.98, description="Kelsier 'snapped' and found in himself the powers of a Mistborn. A brilliant thief and natural leader, he turned his talents to the ultimate caper, with the Lord Ruler himself as the mark. Kelsier recruited the underworld's elite, the smartest and most trustworthy allomancers, each of whom shares one of his many powers, and all of whom relish a high-stakes challenge. Only then does he reveal his ultimate dream, not just the greatest heist in history, but the downfall of the divine despot. But even with the best criminal crew ever assembled, Kel's plan looks more like the ultimate long shot, until luck brings a ragged girl named Vin into his life. ",
        genre_id=1,book_image="https://images.macmillan.com/folio-assets/macmillan_us_frontbookcovers_1000H/9780765311788.jpg",types=False,releaseDate=datetime(2008,12,28))
    book52=Book(
        name="Assassin's Apprentice", author='Robin Hobb',price=16.00, description=" Young Fitz is the bastard son of the noble Prince Chivalry, raised in the shadow of the royal household by his father's gruff stableman. An outcast whose existence has forced his father to abdicate his claim on the throne, Fitz is ignored by all royalty except the devious King Shrewd, who has him secretly tutored in the arts of the assassin. For in the young man's blood is a heritage of magic, the talent called the Skill, as well as another, even more mysterious ability.",
        genre_id=1,book_image="https://thebookmark.co.uk/wp-content/uploads/2020/08/Cover-AssassinsApprentice.jpg",types=False,releaseDate=datetime(2012,3,2))
    book53=Book(
        name="Skip and Loafer", author='Misaki Takamatsu',price=12.99, description="Mitsumi is bound for high school in Tokyo! She's got book smarts, but this small-town girl is about to find out she's massively unprepared for the social norms of big city high schoolers.",
        genre_id=5,book_image="https://cdn.kobo.com/book-images/975ad6ab-941c-4fec-b557-7852e9f59da6/1200/1200/False/skip-and-loafer-vol-1.jpg",types=True,releaseDate=datetime(2021,12,3))
    book54=Book(
        name="All Systems Red", author='Martha Wells',price=14.39, description="In a corporate-dominated spacefaring future, planetary missions must be approved and supplied by the Company. Exploratory teams are accompanied by Company-supplied security androids, for their own safety. But in a society where contracts are awarded to the lowest bidder, safety isn't a primary concern. On a distant planet, a team of scientists are conducting surface tests, shadowed by their Company-supplied 'droid - a self-aware SecUnit that has hacked its own governor module, and refers to itself (though never out loud) as Murderbot. Scornful of humans, all it really wants is to be left alone long enough to figure out who it is. But when a neighboring mission goes dark, it's up to the scientists and their Murderbot to get to the truth.",
        genre_id=2,book_image="https://i.pinimg.com/originals/dc/5e/74/dc5e7418f5f8cf86b7a10e23f7aa5140.jpg",types=False,releaseDate=datetime(2017,10,30))
    book55=Book(
        name="The Infinity Courts", author='Akemi Dawn Bowman',price=12.60, description="Westworld meets Warcross in this high-stakes, dizzyingly smart sci-fi about a teen girl navigating an afterlife in which she must defeat an AI entity intent on destroying humanity,",
        genre_id=2,book_image="https://d28hgpri8am2if.cloudfront.net/book_images/onix/cvr9781534456495/the-infinity-courts-9781534456495_hr.jpg",types=False,releaseDate=datetime(2021,4,6))
    book56=Book(
        name="Hitchhiker's Guide to the Galaxy", author='Douglas Adams',price=11.81, description="Seconds before the Earth is demolished to make way for a galactic freeway, Arthur Dent is plucked off the planet by his friend Ford Prefect, a researcher for the revised edition of The Hitchhiker's Guide to the Galaxy who, for the last 15 years, has been posing as an out-of-work actor.",
        genre_id=2,book_image="https://static.tvtropes.org/pmwiki/pub/images/the_hitchhikers_guide_to_the_galaxy_collection.jpg",types=False,releaseDate=datetime(2005,4,18))
    book57=Book(
        name="Defekt", author='Nino Cipri',price=10.65, description="Derek is LitenVärld's most loyal employee. He lives and breathes the job, from the moment he wakes up in a converted shipping container at the edge of the parking lot to the second he clocks out of work 18 hours later. But after taking his first ever sick day, his manager calls that loyalty into question. An excellent employee like Derek, an employee made to work at LitenVärld, shouldn't need time off. To test his commitment to the job, Derek is assigned to a special inventory shift, hunting through the store to find defective products. Toy chests with pincers and eye stalks, ambulatory sleeper sofas, killer mutant toilets, that kind of thing. Helping him is the inventory team-four strangers who look and sound almost exactly like him. Are five Dereks better than one?",
        genre_id=2,book_image="https://crini.de/wp-content/uploads/2020/12/defekt_-nino-cipri.jpg",types=False,releaseDate=datetime(2022,3,1))
    book58=Book(
        name="The Long Way to a Small, Angry Planet", author='Backy Chambers',price=14.95, description="Follow a motley crew on an exciting journey through space—and one adventurous young explorer who discovers the meaning of family in the far reaches of the universe—in this light-hearted debut space opera from a rising sci-fi star.",
        genre_id=2,book_image="http://www.hodderscape.co.uk/wp-content/uploads/2015/02/20150213_long_way_1400.jpg",types=False,releaseDate=datetime(2017,10,2))
    book59=Book(
        name="Vicious", author='V.E. Schwab',price=15.16, description="Victor and Eli started out as college roommates—brilliant, arrogant, lonely boys who recognized the same sharpness and ambition in each other. In their senior year, a shared research interest in adrenaline, near-death experiences, and seemingly supernatural events reveals an intriguing possibility: that under the right conditions, someone could develop extraordinary abilities. But when their thesis moves from the academic to the experimental, things go horribly wrong.",
        genre_id=2,book_image="https://i1.wp.com/www.thenerddaily.com/wp-content/uploads/2019/01/Vicious-VE-Schwab.jpg",types=False,releaseDate=datetime(2022,2,15))
    book60=Book(
        name="Skyhunter", author='Marie Lu',price=16.90, description="A broken world. An overwhelming evil. A team of warriors ready to strike back.",
        genre_id=2,book_image="https://www.kaitgoodwin.com/books/wp-content/uploads/2020/06/skyhunter-cover.png",types=False,releaseDate=datetime(2020,9,29))
    book61=Book(
        name="Winter's Orbit", author='Everina Maxwell',price=13.69, description="A famously disappointing minor royal and the emperor's least favorite grandchild, Prince Kiem is summoned before the emperor and commanded to renew the empire's bonds with its newest vassal planet. The prince must marry Count Jainan, the recent widower of another royal prince of the empire""But Jainan suspects his late husband’s death was no accident. And Prince Kiem discovers Jainan is a suspect himself. But broken bonds between the empire and its vassal planets leaves the entire empire vulnerable, so together they must prove that their union is strong while uncovering a possible conspiracy.",
        genre_id=2,book_image="https://images.macmillan.com/folio-assets/macmillan_us_frontbookcovers_1000H/9781250758859.jpg",types=False,releaseDate=datetime(2021,2,2))
    book62=Book(
        name="The Darkness Outside Us", author='Eliot Schrefer',price=10.99, description="Two boys, alone in space. Sworn enemies sent on the same rescue mission.",
        genre_id=2,book_image="https://utopia-state-of-mind.com/wp-content/uploads/2021/06/The-Darkness-Outside-Us-by-Elio-Schrefer-1394x2048.jpg",types=False,releaseDate=datetime(2021,1,8))
    book63=Book(
        name="The Power", author='Naomi Alderman',price=12.99, description="Women suddenly develop the power of electricity, oh how the power shifts.",
        genre_id=2,book_image="https://pageandscreenblog.files.wordpress.com/2018/06/the-power.jpg",types=False,releaseDate=datetime(2021,1,7))
    book64=Book(
        name="Hell Followed with Us", author='Andew Joseph White',price=13.99, description="Sixteen-year-old trans boy Benji is on the run from the cult that raised him—the fundamentalist sect that unleashed Armageddon and decimated the world’s population. Desperately, he searches for a place where the cult can’t get their hands on him, or more importantly, on the bioweapon with which they infected him. But when cornered by monsters born from the destruction, Benji is rescued by a group of teens from the local Acheson LGBTQ+ Center, affectionately known as the ALC. The ALC’s leader, Nick, is gorgeous, autistic, and a deadly shot, and he knows Benji’s darkest secret: the cult’s bioweapon is mutating him into a monster deadly enough to wipe humanity from the earth once and for all.",
        genre_id=2,book_image="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1630498579i/57911600.jpg",types=False,releaseDate=datetime(2022,1,9))
    book65=Book(
        name="Illuminae", author='Amie Kaufman & Jay Kristoff',price=18.07, description="This morning, Kady thought breaking up with Ezra was the hardest thing she'd have to do. This afternoon, her planet was invaded.",
        genre_id=2,book_image="https://ashleighonline.com/wp-content/uploads/2016/12/9781780748375_11-800x1227.jpg",types=False,releaseDate=datetime(2016,10,29))
    book66=Book(
        name="The Loneliest Girl in the Universe", author='Lauren James',price=10.12, description="The daughter of two astronauts, Romy Silvers is no stranger to life in space. But she never knew how isolating the universe could be until her parents’ tragic deaths left her alone on the Infinity, a spaceship speeding away from Earth. ",
        genre_id=2,book_image="https://danaandthebooks.com/wp-content/uploads/2017/09/the_loneliest_girl.jpg",types=False,releaseDate=datetime(2018,7,3))
    book67=Book(
        name="Ready Player One", author='Ernest Cline',price=10.45, description="In the year 2045, reality is an ugly place. The only time Wade Watts really feels alive is when he’s jacked into the OASIS, a vast virtual world where most of humanity spends their days. When the eccentric creator of the OASIS dies, he leaves behind a series of fiendish puzzles, based on his obsession with the pop culture of decades past. Whoever is first to solve them will inherit his vast fortune—and control of the OASIS itself. Then Wade cracks the first clue. Suddenly he’s beset by rivals who’ll kill to take this prize. The race is on—and the only way to survive is to win.",
        genre_id=2,book_image="https://www.thegeekgeneration.com/wp-content/uploads/2012/09/Ready-Player-One-book-cover.jpg",types=False,releaseDate=datetime(2011,9,16))
    book68=Book(
        name="Frankenstein", author='Mary Shelley',price=14.95, description="When a man plays with science he creates a monster",
        genre_id=2,book_image="https://prodimage.images-bn.com/pimages/9781435160460_p0_v1_s1200x630.jpg",types=False,releaseDate=datetime(1818,1,1))
    book69=Book(
        name="The Three-Body Problem", author='Liu Cixin',price=16.10, description="Set against the backdrop of China's Cultural Revolution, a secret military project sends signals into space to establish contact with aliens. An alien civilization on the brink of destruction captures the signal and plans to invade Earth. Meanwhile, on Earth, different camps start forming, planning to either welcome the superior beings and help them take over a world seen as corrupt, or to fight against the invasion. The result is a science fiction masterpiece of enormous scope and vision.",
        genre_id=2,book_image="https://shereads.com/wp-content/uploads/2021/07/TheThreeBodyProblem_Cixin-Liu-800x1208.jpg",types=False,releaseDate=datetime(2014,11,11))
    book70=Book(
        name="The Martian", author='Andy Weir',price=15.00, description="Six days ago, astronaut Mark Watney became one of the first people to walk on Mars. Now, he's sure he'll be the first person to die there. After a dust storm nearly kills him and forces his crew to evacuate while thinking him dead, Mark finds himself stranded and completely alone with no way to even signal Earth that he’s alive - and even if he could get word out, his supplies would be gone long before a rescue could arrive.",
        genre_id=2,book_image="https://www.ryanbanderson.com/wp-content/uploads/2015/09/the-martian-cover.jpg",types=False,releaseDate=datetime(2020,1,1))
    book71=Book(
        name="Annihilation", author='Jeff VanderMeer',price=11.69, description="Area X has been cut off from the rest of the continent for decades. Nature has reclaimed the last vestiges of human civilization. The first expedition returned with reports of a pristine, Edenic landscape; all the members of the second expedition committed suicide; the third expedition died in a hail of gunfire as its members turned on one another; the members of the eleventh expedition returned as shadows of their former selves, and within months of their return, all had died of aggressive cancer. This is the twelfth expedition.",
        genre_id=2,book_image="https://elmodenafrontline.com/wp-content/uploads/2017/02/images-2-600x900.jpg",types=False,releaseDate=datetime(2014,2,6))
    book72=Book(
        name="1984", author='George Orwell',price=10.10, description="Winston Smith, the hero with no heroic qualities, longs only for truth and decency. But living in a social system in which privacy does not exist and where those with unorthodox ideas are brainwashed or put to death, he knows there is no hope for him. He knows even as he continues to pursue his forbidden love affair that eventually he will come to destruction.",
        genre_id=2,book_image="https://icommerceonweb.com/wp-content/uploads/2020/04/113423/1984-paperback-1983-by-george-orwell.jpg",types=False,releaseDate=datetime(2006,12,31))
    book73=Book(
        name="Station Eleven", author='Emily St. John',price=12.65, description="Kirsten Raymonde will never forget the night Arthur Leander, the famous Hollywood actor, had a heart attack on stage during a production of King Lear. That was the night when a devastating flu pandemic arrived in the city, and within weeks, civilization as we know it came to an end.",
        genre_id=2,book_image="http://erinmorgenstern.com/wp-content/uploads/2014/09/StationElevenNorthAmericaHiRes.jpg",types=False,releaseDate=datetime(2014,9,8))
    book74=Book(
        name="Kindred", author='Octavia Butler',price=19.74, description="Having just celebrated her 26th birthday in 1976 California, Dana, an African-American woman, is suddenly and inexplicably wrenched through time into antebellum Maryland. After saving a drowning White boy there, she finds herself staring into the barrel of a shotgun and is transported back to the present just in time to save her life. During numerous such time-defying episodes with the same young man, she realizes the challenge she's been given: to protect this young slaveholder until he can father her own great-grandmother. ",
        genre_id=2,book_image="http://www.bibdsl.co.uk/imagegallery2/bds/201413/9781472214812.JPG",types=False,releaseDate=datetime(2007,9,12))
    book75=Book(
        name="The Stars Undying", author='Emery Robin',price=18.99, description="Princess Altagracia has lost everything. After a bloody civil war, her twin sister has claimed not just the crown of their planet Szayet but the Pearl of its prophecy, a computer that contains the immortal soul of Szayet's god. Stripped of her birthright, Gracia flees the planet—just as Matheus Ceirran, Commander of the interstellar Empire of Ceiao, arrives in deadly pursuit with his volatile lieutenant, Anita. When Gracia and Ceirran's paths collide, Gracia sees an opportunity to win back her planet, her god, and her throne…if she can win the Commander and his right-hand officer over first.",
        genre_id=2,book_image="https://realmsofmymind.files.wordpress.com/2022/05/60382741._sy475_.jpg",types=False,releaseDate=datetime(2022,11,8))
    book76=Book(
        name="The Blood Tirals", author='N.E. Davenport',price=14.40, description="A young Black woman must survive deadly trials in a racist and misogynistic society to become an elite warrior",
        genre_id=2,book_image="https://blog.bookhype.com/wp-content/uploads/2021/07/blood-trials.jpg",types=False,releaseDate=datetime(2022,4,9))
    book77=Book(
        name="An Absolutely Remarkable Thing", author='Hank Green',price=16.20, description="A cinematic tale about a young woman who becomes an overnight celebrity before realizing she's part of something bigger, and stranger, than anyone could have possibly imagined.",
        genre_id=2,book_image="https://images.thenile.io/r1000/9781473224209.jpg",types=False,releaseDate=datetime(2018,9,25))
    book78=Book(
        name="A Memory Called Empire", author='Arkady Martine',price=13.35, description="Ambassador Mahit Dzmare arrives in the center of the multi-system Teixcalaanli Empire only to discover that her predecessor, the previous ambassador from their small but fiercely independent mining station, has died. But no one will admit that his death wasn't an accident - or that Mahit might be next to die, during a time of political instability in the highest echelons of the imperial court. Now, Mahit must discover who is behind the murder, rescue herself, and save her station from Teixcalaan's unceasing expansion - all while navigating an alien culture that is all too seductive, engaging in intrigues of her own, and hiding a deadly technological secret - one that might spell the end of her station and her way of life - or rescue it from annihilation.  ",
        genre_id=2,book_image="https://utopia-state-of-mind.com/wp-content/uploads/2021/02/A-Memory-Called-Empire-by-Arkady-Martine-768x1187.jpg",types=False,releaseDate=datetime(2018,2,16))
    book79=Book(
        name="D'Vaughn and Kris Plan a Wedding", author='Chencia C. Higgins',price=16.33, description="Instant I Do could be Kris Zavala’s big break. She’s right on the cusp of really making it as an influencer, so a stint on reality TV is the perfect chance to elevate her brand. And $100,000 wouldn’t hurt either. D’Vaughn Miller is just trying to break out of her shell. She’s sort of neglected to come out to her mom for years, so a big splashy fake wedding is just the excuse she needs. ",
        genre_id=3,book_image="https://m.media-amazon.com/images/I/51vWWcvyF6S.jpg",types=False,releaseDate=datetime(2022,12,30))
    book80=Book(
        name="King of Battle and Blood", author='Scarlett St. Clair',price=14.95, description="Their union is his revenge""Isolde de Lara considers her wedding day to be her death day. To end a years-long war, she is to marry vampire king Adrian Aleksandr Vasiliev, and kill him.",
        genre_id=3,book_image="https://winteriscoming.net/files/2021/08/KBB_High_Res.jpeg",types=False,releaseDate=datetime(2022,4,19))
    book81=Book(
        name="Serpent & Dove", author='Shelby Mahurin',price=12.99, description="wo years ago, Louise le Blanc fled her coven and took shelter in the city of Cesarine, forsaking all magic and living off whatever she could steal. There, witches like Lou are hunted. They are feared. And they are burned. As a huntsman of the Church, Reid Diggory has lived his life by one principle: Thou shalt not suffer a witch to live. But when Lou pulls a wicked stunt, the two are forced into an impossible situation—marriage. Lou, unable to ignore her growing feelings, yet powerless to change what she is, must make a choice. And love makes fools of us all.",
        genre_id=3,book_image="https://d15fwz9jg1iq5f.cloudfront.net/wp-content/uploads/2019/01/31163629/Mahurin_Serpent-and-Dove.jpg",types=False,releaseDate=datetime(2018,4,16))
    book82=Book(
        name="Hani and Ishu's Guide to Fake Dating", author='Adiba Jaigirdar',price=14.42, description="Hani and Ishu couldn't be less alike - and they definitely don't like each other. But when fates collide and they pretend to date each other, things start to get messy...",
        genre_id=3,book_image="https://doodlesandbooks.files.wordpress.com/2021/01/hani-and-ishu.jpg",types=False,releaseDate=datetime(2021,5,27))
    book83=Book(
        name="Spoiler Alert", author='Olivia Dade',price=15.95, description="This delightfully fun romantic comedy set in the world of fanfiction, in which a devoted fan goes on an unexpected date with her celebrity crush, who’s secretly posting fanfiction of his own. ",
        genre_id=3,book_image="https://blog-assets.mugglenet.com/wp-content/uploads/2021/01/50496918-800x1205.jpg",types=False,releaseDate=datetime(2020,10,6))
    book84=Book(
        name="Dial A for Aunties", author='Jesse Q. Sutanto',price=13.99, description="What happens when you mix one (accidental) murder with two thousand wedding guests, and then toss in a possible curse on three generations of an immigrant Chinese-Indonesian family? You get four meddling Asian aunties coming to the rescue! ",
        genre_id=3,book_image="https://www.crumbledpages.com/wp-content/uploads/2021/07/Dial-A-for-Aunties-book-cover-1356x2048.jpg",types=False,releaseDate=datetime(2021,4,27))
    book85=Book(
        name="Ensnared by the Werewolf", author='Lillian Lark',price=8.99, description="A heartbroken witch, a cursed werewolf, and a fated encounter under the full moon.",
        genre_id=3,book_image="https://anybookpdf.com/wp-content/uploads/2022/10/Ensnared-By-The-Werewolf-Book-PDF-download-for-free.jpg",types=False,releaseDate=datetime(2022,2,14))
    book86=Book(
        name="The Shadows Between Us", author='Tricia Lenenseller',price=10.99, description="Alessandra is tired of being overlooked, but she has a plan to gain power: 1. Woo the Shadow King. 2. Marry him. 3.Kill him and take his kingdom for herself.",
        genre_id=3,book_image="https://theloyalbook.com/wp-content/uploads/2020/04/tsbu-678x1024.jpg",types=False,releaseDate=datetime(2020,2,25))
    book87=Book(
        name="The Beautiful Ones", author='Silvia Moreno-Garcia',price=18.99, description="They are the Beautiful Ones, Loisail’s most notable socialites, and this spring is Nina’s chance to join their ranks, courtesy of her well-connected cousin and his calculating wife. But the Grand Season has just begun, and already Nina’s debut has gone disastrously awry. She has always struggled to control her telekinesis- neighbors call her the Witch of Oldhouse - and the haphazard manifestations of her powers make her the subject of malicious gossip. When entertainer Hector Auvray arrives to town, Nina is dazzled. A telekinetic like her, he has traveled the world performing his talents for admiring audiences. He sees Nina not as a witch, but ripe with potential to master her power under his tutelage. With Hector’s help, Nina’s talent blossoms, as does her love for him. But great romances are for fairytales, and Hector is hiding a truth from Nina - and himself - that threatens to end their courtship before it truly begins.",
        genre_id=3,book_image="https://silviamoreno-garcia.com/wp-content/uploads/2017/08/9781250099068-526x800.jpg",types=False,releaseDate=datetime(2021,4,20))
    book88=Book(
        name="The Wisteria Society of Lady Scoundrels", author='India Holton',price=11.79, description="A prim and proper lady thief must save her aunt from a crazed pirate and his dangerously charming henchman in this fantastical historical romance.",
        genre_id=3,book_image="https://cdn.kobo.com/book-images/40ba5a3d-cb0c-4fa6-9a26-9ab0170dc88f/1200/1200/False/the-wisteria-society-of-lady-scoundrels.jpg",types=False,releaseDate=datetime(2021,1,15))
    book89=Book(
        name="You've Reached Sam", author='Dustin Thao',price=17.18, description="Seventeen-year-old Julie Clarke has her future all planned out — move out of her small town with her boyfriend Sam, attend college in the city; spend a summer in Japan. But then Sam dies. And everything changes. Heartbroken, Julie skips his funeral, throws out his belongings, and tries everything to forget him. But a message Sam left behind in her yearbook forces memories to return. Desperate to hear him one more time, Julie calls Sam's cell phone just to listen to his voice mail recording. And Sam picks up the phone.",
        genre_id=3,book_image="https://cdn.kobo.com/book-images/b6be0c5b-dced-47dd-a184-c1057291c5ae/1200/1200/False/you-ve-reached-sam.jpg",types=False,releaseDate=datetime(2021,11,9))
    book90=Book(
        name="Good Omens", author='Neil Gaiman & Terry Pratchett',price=16.99, description="According to The Nice and Accurate Prophecies of Agnes Nutter, Witch (the world's only completely accurate book of prophecies, written in 1655, before she exploded), the world will end on a Saturday. Next Saturday, in fact. Just before dinner. So the armies of Good and Evil are amassing, Atlantis is rising, frogs are falling, tempers are flaring. Everything appears to be going according to Divine Plan. Except a somewhat fussy angel and a fast-living demon - both of whom have lived amongst Earth's mortals since The Beginning and have grown rather fond of the lifestyle - are not actually looking forward to the coming Rapture.",
        genre_id=3,book_image="https://2.bp.blogspot.com/-uKSg20Ykrcg/T79c0IniMHI/AAAAAAAAAFg/PscXo3xnx-U/s1600/goodomens.jpg",types=False,releaseDate=datetime(1990,4,20))
    book91=Book(
        name="The Night Circus", author='Erin Morgenstern',price=17.58, description='The circus arrives without warning. No announcements precede it. It is simply there, when yesterday it was not. Within the black-and-white striped canvas tents is an utterly unique experience full of breathtaking amazements.',
        genre_id=3,book_image="https://www.wisewomencanada.com/wp-content/uploads/2013/08/book-night-circus3.jpg",types=False,releaseDate=datetime(2011,9,13))
    book92=Book(
        name="Bringing Down the Duke", author='Evie Dunmore',price=11.26, description="A fiercely independent vicar's daughter takes on a powerful duke in a fiery love story that threatens to upend the British social order.",
        genre_id=3,book_image="https://www.eleanorlynn.com/wp-content/uploads/2021/01/A1e0fcGuGIL-1-1365x2048.jpg",types=False,releaseDate=datetime(2019,9,3))
    book93=Book(
        name="These Violent Delights", author='Chloe Gong',price=20.19, description="A blood feud between two gangs runs the streets red, leaving the city helpless in the grip of chaos. At the heart of it all is 18-year-old Juliette Cai, a former flapper who has returned to assume her role as the proud heir of the Scarlet Gang - a network of criminals far above the law. Their only rivals in power are the White Flowers, who have fought the Scarlets for generations. And behind every move is their heir, Roma Montagov, Juliette's first love...and first betrayal.",
        genre_id=3,book_image="https://images-na.ssl-images-amazon.com/images/I/81GRh64nRgL.jpg",types=False,releaseDate=datetime(2021,1,26))
    book94=Book(
        name="Fat Chance, Charlie Vega", author='Crystal Maldanado',price=12.99, description="Coming of age as a Fat brown girl in a white Connecticut suburb is hard. Harder when your whole life is on fire, though.",
        genre_id=3,book_image="https://blackwells.co.uk/jacket/l/9780823447176.jpg",types=False,releaseDate=datetime(2021,2,1))
    book95=Book(
        name="Always Be My Duchess", author='Amalie Howard',price=16.99, description="Pretty Woman meets the Bridgertons",
        genre_id=3,book_image="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1637261445l/59530699.jpg",types=False,releaseDate=datetime(2022,7,6))
    book96=Book(
        name="I'll be the One", author='Lyla Lee',price=12.99, description="Skye Shin has heard it all. Fat girls shouldn’t dance. Wear bright colors. Shouldn’t call attention to themselves. But Skye dreams of joining the glittering world of K-Pop, and to do that, she’s about to break all the rules that society, the media, and even her own mother, have set for girls like her. She’ll challenge thousands of other performers in an internationally televised competition looking for the next K-pop star, and she’ll do it better than anyone else.",
        genre_id=3,book_image="https://pingwings.ca/wp-content/uploads/2020/02/ill-be-the-one-1-scaled.jpg",types=False,releaseDate=datetime(2020,1,16))
    book97=Book(
        name="Heartstopper", author='Alice Oseman',price=18.99, description="Follows the story of Charlie Spring and Nick Nelson – two British schoolboys who attend the fictional Truham Grammar School – as they meet and fall in love.",
        genre_id=3,book_image="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1567860835l/50160417.jpg",types=False,releaseDate=datetime(2020,2,14))
    book98=Book(
        name="The Kiss Quotient", author='Helen Hoang',price=18.99, description="Stella Lane thinks math is the only thing that unites the universe. She comes up with algorithms to predict customer purchases - a job that has given her more money than she knows what to do with as well as way less experience in the dating department than the average 30-year-old. It doesn't help that she has Asperger's and that French kissing reminds her of a shark getting its teeth cleaned by pilot fish. She decides that she needs lots of practice - with a professional - which is why she hires escort Michael Phan. ",
        genre_id=3,book_image="https://goodbooksandgoodwine.com/wp-content/uploads/2018/07/The-Kiss-Quotient-Helen-Hoang-Book-Cover.jpg",types=False,releaseDate=datetime(2018,6,5))
    book99=Book(
        name="Ana Maria and the Fox", author='Liana De le Rosa',price=15.99, description="A forbidden love between a Mexican heiress and a shrewd British politician makes for a tantalizing Victorian season.",
        genre_id=3,book_image="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1660147213l/61423847.jpg",types=False,releaseDate=datetime(2023, 8, 8))
    book100=Book(
        name="In a Holidaze", author='Christina Lauren',price=15.99, description="It’s the most wonderful time of the year...but not for Maelyn Jones. She’s living with her parents, hates her going-nowhere job, and has just made a romantic error of epic proportions. The next thing she knows, tires screech and metal collides, everything goes black. But when Mae gasps awake...she’s on an airplane bound for Utah, where she begins the same holiday all over again. With one hilarious disaster after another sending her back to the plane, Mae must figure out how to break free of the strange time loop - and finally get her true love under the mistletoe.",
        genre_id=3,book_image="https://d28hgpri8am2if.cloudfront.net/book_images/onix/cvr9781982123949/in-a-holidaze-9781982123949_xlg.jpg",types=False,releaseDate=datetime(2020,10,4))
    book101=Book(
        name="The Wall of Winnepeg and Me", author='Mariana Zapata',price=14.95, description="Vanessa Mazur refuses to feel bad for quitting—she knows she’s doing the right thing. But when Aiden Graves shows up at her door begging her to come back, she’s beyond shocked. Mr. Walled-Off Emotions is actually letting his guard down for once. And she’s even more dumbstruck when he explains that her job description is about to become even more outrageous: something that takes the “personal” in personal assistant to a whole new level.",
        genre_id=3,book_image="https://m.media-amazon.com/images/I/51YPwummdgL._SY346_.jpg",types=False,releaseDate=datetime(2018,6,2))
    book102=Book(
        name="The Love Hypothesis", author='Ali Hazelwood',price=19.99, description="When a fake relationship between scientists meets the irresistible force of attraction, it throws one woman's carefully calculated theories on love into chaos.",
        genre_id=3,book_image="http://starcrossedbookblog.com/wp-content/uploads/2022/01/love-hypothesis.jpg",types=False,releaseDate=datetime(2021,9,14))
    book103=Book(
        name="A Lady for a Duke", author='Alexis Hall',price=14.95, description="When Viola Carroll was presumed dead at Waterloo she took the opportunity to live, at last, as herself. But freedom does not come without a price, and Viola paid for hers with the loss of her wealth, her title, and her closest companion, Justin de Vere, the Duke of Gracewood.",
        genre_id=3,book_image="https://image.ebooks.com/cover/210222566.jpg",types=False,releaseDate=datetime(2023, 8, 8))
    book104=Book(
        name="Lost in the Never Woods", author='Aiden Thomas',price=18.99, description="When children start to go missing in the local woods, a teen girl must face her fears and a past she can't remember to rescue them",
        genre_id=4,book_image="https://images.macmillan.com/folio-assets/macmillan_us_frontbookcovers_1000H/9781250313980.jpg",types=False,releaseDate=datetime(2021,4,23))
    book105=Book(
        name="The Guest List", author='Lucy Foley',price=16.99, description="A wedding celebration turns dark and deadly",
        genre_id=4,book_image="https://thebookishlibra.com/wp-content/uploads/2020/06/guest-list-678x1030.jpg",types=False,releaseDate=datetime(2020,2,2))
    book106=Book(
        name="The Passengers", author='John Marrs',price=16.99, description="You’re riding in your self-driving car when suddenly the doors lock, the route changes and you have lost all control. Then, a mysterious voice tells you, “You are going to die.”",
        genre_id=4,book_image="https://img.ebook-hunter.org/img/The%20Passengers%20by%20John%20Marrs.jpg",types=False,releaseDate=datetime(2019,8,16))
    book107=Book(
        name="Even If We Break", author='Marieke Nijkamp',price=12.99, description="A group of friends goes to a cabin to play a murder mystery game...only to have the game turned against them.",
        genre_id=4,book_image="https://diversebooks.org/wp-content/uploads/2020/08/9781492636113-300RGB-768x1187.jpg",types=False,releaseDate=datetime(2020,9,15))
    book108=Book(
        name="Sadie", author='Courtney Summers',price=13.99, description="A missing girl on a journey of revenge and a Serial-like podcast following the clues she's left behind.",
        genre_id=4,book_image="https://i.pinimg.com/originals/a9/7e/38/a97e38b0cc87f3f8503a9ca0653bf2ae.jpg",types=False,releaseDate=datetime(2018,9,4))
    book109=Book(
        name="Dead Silence", author='S.A. Barnes',price=14.99, description="A woman and her crew board a decades-lost luxury cruiser and find the wreckage of a nightmare that hasn't yet ended.",
        genre_id=4,book_image="https://prodimage.images-bn.com/pimages/9781250778550_p0_v1_s1200x630.jpg",types=False,releaseDate=datetime(2022,2,8))
    book110=Book(
        name="The Wicker King", author='K. Ancrum',price=18.99, description="August is a misfit with a pyro streak, and Jack is a golden boy on the varsity rugby team - but their intense friendship goes way back. Jack begins to see increasingly vivid hallucinations that take the form of an elaborate fantasy kingdom creeping into the edges of the real world. With their parents' unreliable behavior, August decides to help Jack the way he always has - on his own. He accepts the visions as reality, even when Jack leads them on a quest to fulfill a dark prophecy.",
        genre_id=4,book_image="https://cdn.waterstones.com/bookjackets/large/9781/2501/9781250101556.jpg",types=False,releaseDate=datetime(2021,1,26))
    book111=Book(
        name="The Dark Descent of Elizabeth Frankenstein", author='Kiersten White',price=12.99, description="Elizabeth Lavenza hasn't had a proper meal in weeks. Her thin arms are covered with bruises from her 'caregiver,' and she is on the verge of being thrown into the streets...until she is brought to the home of Victor Frankenstein, an unsmiling, solitary boy who has everything - except a friend. What at first was a dream quickly turns into a nightmare",
        genre_id=4,book_image="https://thats-normal.com/wp-content/uploads/2018/10/darkdescentcover-682x1024.jpg",types=False,releaseDate=datetime(2018,6,2))
    book112=Book(
        name="Stalking Jack the Ripper", author='Kerri Maniscalco',price=14.99, description="Seventeen-year-old Audrey Rose Wadsworth was born a lord's daughter, with a life of wealth and privilege stretched out before her. But between the social teas and silk dress fittings, she leads a forbidden secret life. Against her stern father's wishes and society's expectations, Audrey often slips away to her uncle's laboratory to study the gruesome practice of forensic medicine. When her work on a string of savagely killed corpses drags Audrey into the investigation of a serial murderer, her search for answers brings her close to her own sheltered world.",
        genre_id=4,book_image="https://4.bp.blogspot.com/-YQFCYs8WzBU/V_qYNMJd2dI/AAAAAAAAhYo/tLh77DbHPwQ_3jwHQR4QSdpwwLwvtRpXQCLcB/s1600/StalkingJacktheRipper_Cover.jpg",types=False,releaseDate=datetime(2016,9,20))
    book113=Book(
        name="What the Dead Know", author='Nghi Vo',price=12.99, description="A woman posing as a medium who can channel the spirit world comes face to face with the truth",
        genre_id=4,book_image="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1665768248i/62991434.jpg",types=False,releaseDate=datetime(2022,12,3))
    book114=Book(
        name="Magic for Liars", author='Sarah Gailey',price=13.99, description="When a gruesome murder is discovered at the Osthorne Academy of Young Mages, where her estranged twin sister teaches theoretical magic, reluctant detective Ivy Gamble is pulled into the world of untold power and dangerous secrets. She will have to find a murderer and reclaim her sister - without losing herself.   ",
        genre_id=4,book_image="https://i.pinimg.com/originals/94/ff/b9/94ffb9f890db82481f329c1c5f2025dc.jpg",types=False,releaseDate=datetime(2019,1,4))
    book115=Book(
        name="The 7 1/2 Deaths of Evelyn Hugo", author='Stuart Turton',price=12.99, description="An addictive mystery that follows one man's race to find a killer, with an astonishing time-turning twist that means nothing and no one are quite what they seem.",
        genre_id=4,book_image="https://images-na.ssl-images-amazon.com/images/I/51UbZamYsxL.jpg",types=False,releaseDate=datetime(2019,2,16))
    book116=Book(
        name="THe Taking of Jake Livingston", author='Ryan Douglas',price=14.95, description="Get Out meets Holly Jackson in this YA social thriller where survival is not a guarantee.",
        genre_id=4,book_image="https://picture.readfrom.net/img/ryan-douglass/the_taking_of_jake_livingston.jpg",types=False,releaseDate=datetime(2021,7,13))
    book117=Book(
        name="The Only Good Indians", author='Stephen Graham Jones',price=12.99, description="This story follows the lives of four American-Indian men and their families, all haunted by a disturbing, deadly event that took place in their youth. Years later, they find themselves tracked by an entity bent on revenge, totally helpless as the culture and traditions they left behind catch up to them in a violent, vengeful way.",
        genre_id=4,book_image="https://theloyalbook.com/wp-content/uploads/2020/08/togi.jpg",types=False,releaseDate=datetime(2020,7,14))
    book118=Book(
        name="Into the Drowning Deep", author='Mira Grant',price=14.95, description="Seven years ago the Atargatis set off on a voyage to the Mariana Trench to film a mockumentary bringing to life ancient sea creatures of legend. It was lost at sea with all hands. Some have called it a hoax; others have called it a tragedy. Now a new crew has been assembled. But this time they're not out to entertain. Some seek to validate their life's work. Some seek the greatest hunt of all. Some seek the truth. But for the ambitious young scientist Victoria Stewart, this is a voyage to uncover the fate of the sister she lost.",
        genre_id=4,book_image="https://prodimage.images-bn.com/pimages/9780316379373_p0_v1_s1200x630.jpg",types=False,releaseDate=datetime(2017,2,7))
    book119=Book(
        name="The Inheritance Games", author='Jennifer Lynn Barnes',price=12.99, description="Avery Grambs has a plan for a better future: Survive high school, win a scholarship, and get out. But her fortunes change in an instant when billionaire Tobias Hawthorne dies and leaves Avery virtually his entire fortune. The catch? Avery has no idea why - or even who Tobias Hawthorne is. ",
        genre_id=4,book_image="https://www.sperling.it/content/uploads/2021/06/978882007130HIG.JPG",types=False,releaseDate=datetime(2020,9,1))
    book120=Book(
        name="The Twisted Ones", author='T. Kingfisher',price=13.31, description="When a young woman clears out her deceased grandmother’s home in rural North Carolina, she finds long-hidden secrets about a strange colony of beings in the woods",
        genre_id=4,book_image="https://d28hgpri8am2if.cloudfront.net/book_images/onix/cvr9781534429567/the-twisted-ones-9781534429567_hr.jpg",types=False,releaseDate=datetime(2019,10,9))
    book121=Book(
        name="Silver Under Nightfall", author='Rin Chupeco',price=14.99, description="Remy Pendergast is many things: the only son of the Duke of Valenbonne (though his father might wish otherwise), an elite bounty hunter of rogue vampires, and an outcast among his fellow Reapers. As he prepares to investigate a new vampire breed he meets an unlikely pair that will change everything",
        genre_id=4,book_image="https://d28hgpri8am2if.cloudfront.net/book_images/onix/cvr9781982195717/silver-under-nightfall-9781982195717_xlg.jpg",types=False,releaseDate=datetime(2023, 8, 8))
    book122=Book(
        name="The Shuddering", author='Ania Ahiborn',price=9.99, description="They only come when it snows, and nobody ever gets away. A group of close friends gathers at a secluded cabin in the wintry mountains of Colorado for a final holiday hurrah. Instead, it may be their last stand. First a massive blizzard leaves them marooned. Then the more chilling realization: Something is lurking in the woods, watching them, waiting....",
        genre_id=4,book_image="https://prodimage.images-bn.com/pimages/9781611099676_p0_v2_s1200x630.jpg",types=False,releaseDate=datetime(2013,1,18))
    book123=Book(
        name="A Lesson in Vengence", author='Victoria Lee',price=13.99, description="A dark, twisty thriller about a centuries-old, ivy-covered boarding school haunted by its history of witchcraft and two girls dangerously close to digging up the past. ",
        genre_id=4,book_image="https://images-na.ssl-images-amazon.com/images/I/81EoR4LVTnL.jpg",types=False,releaseDate=datetime(2021,8,3))
    book124=Book(
        name="Gone Girl", author='Gillian Flynn',price=12.99, description="On a warm summer morning in North Carthage, Missouri, it is Nick and Amy Dunne’s fifth wedding anniversary. Presents are being wrapped and reservations are being made when Nick’s clever and beautiful wife disappears. Husband-of-the-Year Nick isn’t doing himself any favors with cringe-worthy daydreams about the slope and shape of his wife’s head, but passages from Amy's diary reveal the alpha-girl perfectionist could have put anyone dangerously on edge. Under mounting pressure from the police and the media—as well as Amy’s fiercely doting parents—the town golden boy parades an endless series of lies, deceits, and inappropriate behavior. Nick is oddly evasive, and he’s definitely bitter—but is he really a killer? ",
        genre_id=4,book_image="https://images6.fanpop.com/image/photos/37400000/Gone-Girl-by-Gillian-Flynn-gone-girl-37441442-1181-1810.jpg",types=False,releaseDate=datetime(2012,6,5))
    book125=Book(
        name="The Girl with the Dragon Tattoo", author='Steig Larsson',price=12.99, description="Combine the chilly Swedish backdrop and moody psychodrama of a Bergman movie with the grisly pyrotechnics of a serial-killer thriller, then add an angry punk heroine and a down-on-his-luck investigative journalist.",
        genre_id=4,book_image="https://www.bookgeeks.in/wp-content/uploads/2017/04/the-girl-with-the-dragon-tattoo.jpg",types=False,releaseDate=datetime(2008,1,16))
    book126=Book(
        name="The Good Son", author='You-Jeong Jeong',price=15.99, description="Who can you trust if you can't trust yourself? Early one morning, twenty-six-year-old Yu-jin wakes up to a strange metallic smell, and a phone call from his brother asking if everything's all right at home–he missed a call from their mother in the middle of the night. Yu-jin soon discovers her murdered body, lying in a pool of blood at the bottom of the stairs of their stylish Seoul duplex. He can't remember much about the night before; having suffered from seizures for most of his life, Yu-jin often has trouble with his memory. All he has is a faint impression of his mother calling his name. But was she calling for help? Or begging for her life? ",
        genre_id=4,book_image="https://prodimage.images-bn.com/pimages/9780143131953_p0_v5_s1200x630.jpg",types=False,releaseDate=datetime(2018,6,5))
    book127=Book(
        name="Spy X Family", author='Tatsuya Endo',price=7.68, description="An action-packed comedy about a fake family that includes a spy, an assassin and a telepath!",
        genre_id=5,book_image="https://www.manga-news.com/public/images/vols/spy-x-family-1-jp.jpg",types=True,releaseDate=datetime(2019,6,2))
    book128=Book(
        name="One Punch Man", author='ONE',price=9.98, description="Life gets pretty boring when you can beat the snot out of any villain with just one punch.",
        genre_id=5,book_image="https://d28hgpri8am2if.cloudfront.net/book_images/onix/cvr9781421585642/one-punch-man-vol-1-9781421585642_hr.jpg",types=True,releaseDate=datetime(2017,2,6))
    book129=Book(
        name="Can't Stop Cursing You", author='Kensuke Koba',price=6.99, description="Those who make contracts with devils gain the power to curse others to death. Their mortal enemy: the Curse Detective Kiyoharu Saeyama, who uses traces of the curses left on their victims to uncover the identities of these sick killers. Let this deadly, paranormal game of psychological warfare begin!",
        genre_id=5,book_image="https://animeuknews.net/app/uploads/2021/06/Cant-Stop-Cursing-You-volume-1-cover.jpeg",types=True,releaseDate=datetime(2023, 8, 8))
    book130=Book(
        name="Full Metal Alchemist", author='Hiromu Arakawa',price=8.77, description="Alchemy: the mystical power to alter the natural world; something between magic, art, and science. When two brothers, Edward and Alphonse Elric, dabbled in this power to grant their dearest wish, one of them lost an arm and a leg...and the other became nothing but a soul locked into a body of living steel. Now Edward is a agent of the government, a slave of the military-alchemical complex, using his unique powers to obey orders...even to kill. Except his powers aren't unique. The world has been ravaged by the abuse of alchemy. And in the pursuit of the ultimate alchemical treasure, the Philosopher's Stone, their enemies are even more ruthless than they are...",
        genre_id=5,book_image="https://d28hgpri8am2if.cloudfront.net/book_images/cvr9781591169208_9781591169208_hr.jpg",types=True,releaseDate=datetime(2016,3,5))
    book131=Book(
        name="Black Clover", author='Yuki Tabata',price=9.99, description="Young Asta was born with no magic ability in a world where magic is everything. In order to prove his strength and keep a promise with his friend, Asta dreams of becoming the greatest mage in the land, the Wizard King!",
        genre_id=5,book_image="https://freshcomics.s3.amazonaws.com/issue_covers/APR162102.jpg",types=True,releaseDate=datetime(2020,6,12))
    book132=Book(
        name="Zom 100: Bucket List of the Dead", author='Haro Aso',price=7.99, description="In a trash-filled apartment, 24-year-old Akira Tendo watches a zombie movie with lifeless, envious eyes. After spending three hard years at an exploitative corporation in Japan, his spirit is broken. He can’t even muster the courage to confess his feelings to his beautiful co-worker Ohtori. Then one morning, he stumbles upon his landlord eating lunch—which happens to be another tenant! The whole city’s swarming with zombies, and even though he’s running for his life, Akira has never felt more alive!",
        genre_id=5,book_image="https://cdn11.bigcommerce.com/s-9xdcxxuu0e/images/stencil/640w/products/13958/17006/3d3167e50ff9f03704e1a1682ce45a861ce31b42__02396.1624529015.jpg",types=True,releaseDate=datetime(2021,9,7))
    book133=Book(
        name="Sailor Moon", author='Naoko Takeuchi',price=9.99, description="Teenager Usagi is not the best athlete, she’s never gotten good grades, and, well, she’s a bit of a crybaby. But when she meets a talking cat, she begins a journey that will teach her she has a well of great strength just beneath the surface and the heart to inspire and stand up for her friends as Sailor Moon! ",
        genre_id=5,book_image="https://i0.wp.com/aiptcomics.com/wp-content/uploads/2018/12/egsegsg.jpg",types=True,releaseDate=datetime(1990,2,3))
    book134=Book(
        name="One Piece", author='Eiichiro Oda',price=10.99, description="As a child, Monkey D. Luffy was inspired to become a pirate by listening to the tales of the buccaneer 'Red-Haired' Shanks. But his life changed when Luffy accidentally ate the Gum-Gum Devil Fruit and gained the power to stretch like rubber...at the cost of never being able to swim again! Years later, still vowing to become the king of the pirates, Luffy sets out on his adventure...one guy alone in a rowboat, in search of the legendary 'One Piece,' said to be the greatest treasure in the world...",
        genre_id=5,book_image="https://d28hgpri8am2if.cloudfront.net/book_images/cvr9781569319017_9781569319017_hr.jpg",types=True,releaseDate=datetime(2002,5,1))
    book135=Book(
        name="Mashle: Magic and Muscles", author='Hajime Komoto.',price=9.99, description="When you are the only person alive without magic you might just have to make your own to get by, MUSCLE MAGIC!",
        genre_id=5,book_image="https://www.manga-news.com/public/images/vols/mashle-1-kaze.jpg",types=True,releaseDate=datetime(2022,3,5))
    book136=Book(
        name="Horimiya", author='Hiroki Adachi',price=9.35, description="A sweet tale of school life begins!!At school, Kyouko Hori is known for being smart, attractive, and popular. On the other hand, her classmate, the boring, gloomy Izumi Miyamura tends to get painted as a 'loser fanboy.' But when a liberally pierced and tattooed (not to mention downright gorgeous) Miyamura appears unexpectedly on the doorstep of secretly plain-Jane homebody Hori, these two similarly dissimilar teenagers discover that there are multiple sides to every story...and person!",
        genre_id=5,book_image="https://girlsincapes.com/wp-content/uploads/2015/11/HERO_Horimiya_TP_V1.jpg",types=True,releaseDate=datetime(2019,6,4))
    book137=Book(
        name="Hunter X Hunter", author='Yoshihiro Togashi',price=9.99, description="Having survived the terrors of the high seas, Gon and his companions now have to prove their worth in a variety of tests in order to find the elusive Exam Hall. And once they get there, will they ever leave alive...?",
        genre_id=5,book_image="https://d28hgpri8am2if.cloudfront.net/book_images/onix/cvr9781591167532/hunter-x-hunter-vol-1-9781591167532_hr.jpg",types=True,releaseDate=datetime(2015,6,4))
    book138=Book(
        name="Princess Jellyfish", author='Akiko Higashimura',price=8.99, description="Tsukimi Kurashita has a strange fascination with jellyfish. She’s loved them from a young age and has carried that love with her to her new life in the big city of Tokyo. There, she resides in Amamizukan, a safe-haven for girl geeks who regularly gush over a range of things from trains to Japanese dolls. However, a chance meeting at a pet shop has Tsukimi crossing paths with one of the things that the residents of Amamizukan have been desperately trying to avoid—a beautiful and fashionable woman!",
        genre_id=5,book_image="https://i.thenile.io/r1000/9781632362285.jpg",types=True,releaseDate=datetime(2005,6,7))
    book139=Book(
        name="Sasaki and Miyano", author='Sho Harusono',price=10.99, description="It all started like a typical old-school boys’ love plotline-bad-boy senior meets adorably awkward underclassman, one of them falls in love, and so on and so forth. But although Miyano is a self-proclaimed boys’ love expert, he hasn’t quite realized…he’s in one himself. Which means it’s up to Sasaki to make sure their story has a happily ever after…!",
        genre_id=5,book_image="https://www.nautiljon.com/images/hotlink/manga_volumes/11/46/sasaki_to_miyano_vol_1_-_edition_us947464.jpg",types=True,releaseDate=datetime(2018,9,7))
    book140=Book(
        name="Naruto", author='Masashi Kishimoto',price=9.99, description="Twelve years ago the Village Hidden in the Leaves was attacked by a fearsome threat. A nine-tailed fox spirit claimed the life of the village leader, the Hokage, and many others. Today, the village is at peace and a troublemaking kid named Naruto is struggling to graduate from Ninja Academy. His goal may be to become the next Hokage, but his true destiny will be much more complicated. The adventure begins now!",
        genre_id=5,book_image="https://ybovbco8hhye.cdn.shift8web.ca/wp-content/uploads/2021/07/naruto-volume-1.jpg",types=True,releaseDate=datetime(2000,6,1))
    book141=Book(
        name="Bleach", author='Tite Kubo.',price=8.76, description="Ichigo Kurosaki has always been able to see ghosts, but this ability doesn't change his life nearly as much as his close encounter with Rukia Kuchiki, a Soul Reaper and member of the mysterious Soul Society. While fighting a Hollow, an evil spirit that preys on humans who display psychic energy, Rukia attempts to lend Ichigo some of her powers so that he can save his family; but much to her surprise, Ichigo absorbs every last drop of her energy. Now a full-fledged Soul Reaper himself, Ichigo quickly learns that the world he inhabits is one full of dangerous spirits and, along with Rukia--who is slowly regaining her powers--it's Ichigo's job to protect the innocent from Hollows and help the spirits themselves find peace.",
        genre_id=5,book_image="https://st1.myideasoft.com/shop/cd/03/myassets/products/343/71ykjjljtml.jpg",types=True,releaseDate=datetime(2000,3,4))
    book142=Book(
        name="Soul Eater", author='Atsushi Ohkubo',price=6.99, description="Maka is a weapon meister, determined to turn her partner, a living scythe named Soul Eater, into a powerful death scythe - the ultimate weapon of Death himself! Charged with the task of collecting and devouring the tainted souls of ninety-nine humans and one witch, Maka and her fellow meisters strive to master their weapons as they face off against the bizarre and dangerous minions of the underworld. But the meisters' own personal quirks may prove a bigger obstacle than any sultry enchantress!",
        genre_id=5,book_image="https://www.manga-news.com/public/images/vols/soul-eater-1-ed-anniversaire-kurokawa.jpg",types=True,releaseDate=datetime(2005,6,4))
    book143=Book(
        name="Death Note", author='Tsugumi Ohba',price=5.99, description="Light tests the boundaries of the Death Note's powers as L and the police begin to close in. Luckily Light's father is the head of the Japanese National Police Agency and leaves vital information about the case lying around the house. With access to his father's files, Light can keep one step ahead of the authorities. But who is the strange man following him, and how can Light guard against enemies whose names he doesn't know?",
        genre_id=5,book_image="https://d28hgpri8am2if.cloudfront.net/book_images/onix/cvr9781421501680/death-note-vol-1-9781421501680_hr.jpg",types=True,releaseDate=datetime(2006,7,9))
    book144=Book(
        name="My Hero Academia", author='Kohei Horikoshi',price=9.99, description="Middle school student Izuku Midoriya wants to be a hero more than anything, but he hasn’t got an ounce of power in him. With no chance of ever getting into the prestigious U.A. High School for budding heroes, his life is looking more and more like a dead end. Then an encounter with All Might, the greatest hero of them all, gives him a chance to change his destiny…",
        genre_id=5,book_image="http://www.nerdspan.com/wp-content/uploads/2015/08/my-hero-academia.jpg",types=True,releaseDate=datetime(2010,7,6))
    book145=Book(
        name="Attack on Titan", author='Hajime Isayama',price=10.11, description="In this post-apocalytpic sci-fi story, humanity has been devastated by the bizarre, giant humanoids known as the Titans. Little is known about where they came from or why they are bent on consuming mankind. Seemingly unintelligent, they have roamed the world for years, killing everyone they see. For the past century, what's left of man has hidden in a giant, three-walled city. People believe their 100-meter-high walls will protect them from the Titans, but the sudden appearance of an immense Titan is about to change everything.",
        genre_id=5,book_image="https://www.carlsen.de/sites/default/files/produkt/cover/attack-on-titan-1.jpg",types=True,releaseDate=datetime(2015,9,7))
    book146=Book(
        name="The Promised Neverland", author='Kaiu Shirai',price=11.99, description="Emma, Norman and Ray are the brightest kids at the Grace Field House orphanage. And under the care of the woman they refer to as “Mom,” all the kids have enjoyed a comfortable life. Good food, clean clothes and the perfect environment to learn—what more could an orphan ask for? One day, though, Emma and Norman uncover the dark truth of the outside world they are forbidden from seeing.",
        genre_id=5,book_image="https://i.pinimg.com/474x/8d/ca/e2/8dcae2c38802871fce37d5c1a5a16cdb.jpg",types=True,releaseDate=datetime(2018,6,4))
    book147=Book(
        name="Yona of the Dawn", author='Mizuho Kusanagi',price=7.99, description="Yona reels from the shock of witnessing a loved one’s murder and having to fight for her life. With Hak’s help, she flees the palace and struggles to survive while evading her enemy’s forces. But where will this displaced princess go when all the paths before her are uncertain?",
        genre_id=5,book_image="https://m.media-amazon.com/images/I/61mov5O6GtL._SY346_.jpg",types=True,releaseDate=datetime(2010,6,4))
    book148=Book(
        name="Ouran High School Host Club", author='Bisco Hatori',price=8.99, description="One day, Haruhi, a scholarship student at exclusive Ouran High School, breaks an $80,000 vase that belongs to the 'Host Club', a mysterious campus group consisting of six super-rich (and gorgeous) guys. To pay back the damages, she is forced to work for the club, and it's there that she discovers just how wealthy the boys are and how different they are from everybody else.",
        genre_id=5,book_image="https://www.absoluteanime.com/ouran_high_school_host_club/index.jpg",types=True,releaseDate=datetime(2004,9,7))
    book149=Book(
        name="Chainsaw Man", author='Tatsuki Fujimoto',price=10.10, description="Denji’s a poor young man who’ll do anything for money, even hunting down devils with his pet devil Pochita. He’s a simple man with simple dreams, drowning under a mountain of debt. But his sad life gets turned upside down one day when he’s betrayed by someone he trusts. Now with the power of a devil inside him, Denji’s become a whole new man—Chainsaw Man!",
        genre_id=5,book_image="https://lesinstantsvolesalavie.files.wordpress.com/2020/02/chainswanman.jpg",types=True,releaseDate=datetime(2018,9,3))
    book150=Book(
        name="Fairy Tail", author='Hiro Mashima',price=10.69, description="THE WICKED SIDE OF WIZARDRY ? Cute girl wizard Lucy wants to join the Fairy Tail, a club for the most powerful wizards. But instead, her ambitions land her in the clutches of a gang of unsavory pirates le by a devious magician. Her only hope is Natsu, a strange boy she happens to meet on her travels. Natsu's not your typical hero - he gets motion sickness, eats like a pig, and his best friend is a talking cat. With friends like this, is Lucy better off with her enemies?",
        genre_id=5,book_image="https://prodimage.images-bn.com/pimages/9781612622767_p0_v1_s1200x630.jpg",types=True,releaseDate=datetime(2006,4,7))
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
        comment="Awful!!",rating=1,user_id=2, book_id=115,created_at=datetime(2015, 10, 25),user_username='marnie'
    )
    review8=Review(
        comment="Such an original book!",rating=4,user_id=3, book_id=84,created_at=datetime(2020, 10, 25),user_username='lone_centurion'
    )
    review9=Review(
        comment="Great premise bad execution.",rating=2,user_id=3, book_id=91,created_at=datetime(2021, 10, 25),user_username='lone_centurion'
    )
    review10=Review(
        comment="The book is so much better than the movie!",rating=4,user_id=2, book_id=67,created_at=datetime(2020, 10, 25),user_username='marnie'
    )
    review11=Review(
        comment="Loved the girl power!!",rating=5,user_id=4, book_id=6,created_at=datetime(2022, 10, 25),user_username='the_bride'
    )
    review12=Review(
        comment="This was fun!",rating=4,user_id=5, book_id=7,created_at=datetime(2021, 6, 25),user_username='pandorica'
    )
    review13=Review(
        comment="Romance was great and the humor was top tier.",rating=5,user_id=6, book_id=8,created_at=datetime(2021, 10, 25),user_username='bad_wolf'
    )
    review14=Review(
        comment="It was definitely a book that i read. it was too drawn out though",rating=3,user_id=4, book_id=16,created_at=datetime(2021, 11, 2),user_username='the_bride'
    )
    review15=Review(
        comment="Loved this series so much, they really grow up so much!!",rating=4,user_id=3, book_id=10,created_at=datetime(2022, 6, 15),user_username='lone_centurion'
    )
    review16=Review(
        comment="Too violent and dark for me",rating=1,user_id=2, book_id=11,created_at=datetime(2020, 6, 3),user_username='marnie'
    )
    review17=Review(
        comment="These kids are all kinds of tramatized! Book was still great!",rating=4,user_id=7, book_id=12,created_at=datetime(2022, 7, 25),user_username='melody'
    )
    review18=Review(
        comment="Now this is the kind of crazy revenge i can get behind!",rating=5,user_id=7, book_id=13,created_at=datetime(2021, 10, 15),user_username='melody'
    )
    review19=Review(
        comment="Moved really slow, not very interesting.",rating=2,user_id=3, book_id=14,created_at=datetime(2022, 3, 25),user_username='lone_centurion'
    )
    review20=Review(
        comment="A heist, sounds right up my alley!",rating=4,user_id=3, book_id=15,created_at=datetime(2019, 10, 1),user_username='lone_centurion'
    )
    review21=Review(
        comment="Really adorable!",rating=4,user_id=4, book_id=17,
        created_at=datetime(2017, 10, 1),user_username='the_bride'
    )
    review22=Review(
        comment="Definitely violent, and the main character was kinda annoying",rating=2,user_id=3, book_id=18,
        created_at=datetime(2023, 6, 15),user_username='lone_centurion'
    )
    review23=Review(
        comment="FLY!!",rating=5,user_id=7, book_id=19,
        created_at=datetime(2020, 7, 1),user_username='melody'
    )
    review24=Review(
        comment="The writing was really hard to get into",rating=1,user_id=6, book_id=20,
        created_at=datetime(2019, 10, 1),user_username='bad_wolf'
    )
    review25=Review(
        comment="Extremely violent adn traumatic!",rating=5,user_id=7, book_id=21,
        created_at=datetime(2019,5, 12),user_username='melody'
    )
    review26=Review(
        comment="The representation was good but wasn't the best plot wise.",rating=3,user_id=5, book_id=22,
        created_at=datetime(2022, 3, 1),user_username='pandorica'
    )
    review27=Review(
        comment="Amazing, I would do anything for Splendid Speckled Mosscap!",rating=5,user_id=5, book_id=23,
        created_at=datetime(2022, 12, 1),user_username='pandorica'
    )
    review28=Review(
        comment="Not my cup of tea",rating=1,user_id=4, book_id=24,
        created_at=datetime(2021, 10, 1),user_username='the_bride'
    )
    review29=Review(
        comment="Simply Great!",rating=4,user_id=2, book_id=25,
        created_at=datetime(2019, 11, 11),user_username='marnie'
    )
    review30=Review(
        comment="When  those toxic relationships won't end!! Even in death!!",rating=4,user_id=6, book_id=26,
        created_at=datetime(2023, 3, 15),user_username='bad_wolf'
    )
    review31=Review(
        comment="This is Carrie but bettter!! If i could give more than 5 stars i would!!",rating=5,user_id=7, book_id=27,
        created_at=datetime(2022, 11, 8),user_username='melody'
    )
    review32=Review(
        comment="Loved it, I was on the edge of my seat!!",rating=5,user_id=1, book_id=28,
        created_at=datetime(2022, 10, 1),user_username='Demo'
    )
    review33=Review(
        comment="Has been done better than this.",rating=2,user_id=3, book_id=29,
        created_at=datetime(2019, 10, 1),user_username='lone_centurion'
    )
    review34=Review(
        comment="This is what Harry Potter wanted to be",rating=5,user_id=5, book_id=30,
        created_at=datetime(2021, 12, 18),user_username='pandorica'
    )
    review35=Review(
        comment="Hated it!!!",rating=1,user_id=4, book_id=31,
        created_at=datetime(2019, 10, 1),user_username='the_bride'
    )
    review36=Review(
        comment="love a good revenge story!",rating=4,user_id=6, book_id=32,
        created_at=datetime(2022, 10, 1),user_username='bad_wolf'
    )
    review37=Review(
        comment="Plot was lacking",rating=3,user_id=2, book_id=33,
        created_at=datetime(2019, 10, 1),user_username='marnie'
    )
    review38=Review(
        comment="This could have been done better",rating=3,user_id=3, book_id=34,
        created_at=datetime(2022, 10, 1),user_username='lone_centurion'
    )
    review39=Review(
        comment="I mean am i the only one who found this relationship toxic??",rating=1,user_id=4, book_id=35,
        created_at=datetime(2023, 10, 1),user_username='the_bride'
    )
    review40=Review(
        comment="Honestly, loved her descent into madness",rating=5,user_id=7, book_id=36,
        created_at=datetime(2019, 10, 1),user_username='melody'
    )
    review41=Review(
        comment="Meh...",rating=2,user_id=2, book_id=37,
        created_at=datetime(2022,11,20),user_username='marnie'
    )
    review42=Review(
        comment="The pacing was a little off but otherwise good",rating=3,user_id=3, book_id=38,
        created_at=datetime(2021,11,9),user_username='lone_centurion'
    )
    review43=Review(
        comment="Overhyped",rating=3,user_id=6, book_id=39,
        created_at=datetime(2023,8,18),user_username='bad_wolf'
    )
    review44=Review(
        comment="The embodiement of riding a rollercoaster",rating=5,user_id=5, book_id=40,
        created_at=datetime(2021,12,6),user_username='pandorica'
    )
    review45=Review(
        comment="Forgettable",rating=3,user_id=4, book_id=41,
        created_at=datetime(2022,4,16),user_username='the_bride'
    )
    review46=Review(
        comment="The FMC was a badass!!",rating=5,user_id=7, book_id=42,
        created_at=datetime(2023,4,5),user_username='melody'
    )
    review47=Review(
        comment="AWESOME!!",rating=5,user_id=3, book_id=43,
        created_at=datetime(2023,8,7),user_username='lone_centurion'
    )
    review48=Review(
        comment="Liked the premise, but pacing probs",rating=3,user_id=2, book_id=44,
        created_at=datetime(2017,8,9),user_username='marnie'
    )
    review49=Review(
        comment="Nope Nope Nope",rating=1,user_id=1, book_id=45,
        created_at=datetime(2022,9,4),user_username='Demo'
    )
    review50=Review(
        comment="Nope Nope Nope",rating=1,user_id=1, book_id=46,
        created_at=datetime(2022,9,4),user_username='Demo'
    )
    review51=Review(
        comment="I mean reapers and revenge what more could a girl ask for!!",rating=5,user_id=7, book_id=47,
        created_at=datetime(2022,1,5),user_username='melody'
    )
    review52=Review(
        comment="So original and amazing!",rating=5,user_id=5, book_id=48,
        created_at=datetime(2022,5,4),user_username='pandorica'
    )
    review53=Review(
        comment="Tried to branch out and hated it",rating=2,user_id=4, book_id=49,
        created_at=datetime(2021,6,4),user_username='the_bride'
    )
    review54=Review(
        comment="Loved the badass characters",rating=4,user_id=6, book_id=50,
        created_at=datetime(2014,6,4),user_username='bad_wolf'
    )
    review55=Review(
        comment="Was great until it wasn't...",rating=3,user_id=2, book_id=51,
        created_at=datetime(2015,9,4),user_username='marnie'
    )
    review56=Review(
        comment="I fell like i have a type and this is it!!",rating=4,user_id=7, book_id=52,
        created_at=datetime(2020,8,7),user_username='melody'
    )
    review57=Review(
        comment="Adorable!! Lovely slice of life!!",rating=4,user_id=4, book_id=53,
        created_at=datetime(2023,6,8),user_username='the_bride'
    )
    review58=Review(
        comment="Love a sassy/unhinged AI",rating=4,user_id=3, book_id=54,
        created_at=datetime(2018,6,4),user_username='lone_centurion'
    )
    review59=Review(
        comment="AI really do be popping off.",rating=4,user_id=1, book_id=55,
        created_at=datetime(2022,9,4),user_username='Demo'
    )
    review60=Review(
        comment="I mean its a classic, you can't hate a classic",rating=5,user_id=3, book_id=56,
        created_at=datetime(2019,6,7),user_username='lone_centurion'
    )
    review61=Review(
        comment="Love a sassy/unhinged AI",rating=4,user_id=3, book_id=65,
        created_at=datetime(2022,6,4),user_username='lone_centurion'
    )
    review62=Review(
        comment="I have three whole friends... but all of them are you. You bet i love me like a friend.",rating=5,user_id=7, book_id=57,
        created_at=datetime(2022,6,4),user_username='melody'
    )
    review63=Review(
        comment="Mid if i had to rate it",rating=3,user_id=6, book_id=58,
        created_at=datetime(2022,8,1),user_username='bad_wolf'
    )
    review64=Review(
        comment="Really Good",rating=4,user_id=4, book_id=59,
        created_at=datetime(2022,3,7),user_username='the_bride'
    )
    review65=Review(
        comment="Hated every second of it",rating=1,user_id=5, book_id=60,
        created_at=datetime(2022,2,7),user_username='pandorica'
    )
    review66=Review(
        comment="Wasn't horrible but nothing special either",rating=3,user_id=2, book_id=61,
        created_at=datetime(2021,6,7),user_username='marnie'
    )
    review67=Review(
        comment="Weird but in a good way",rating=4,user_id=7, book_id=62,
        created_at=datetime(2022,9,7),user_username='melody'
    )
    review68=Review(
        comment="Loved it!!!",rating=4,user_id=6, book_id=63,
        created_at=datetime(2022,6,7),user_username='bad_wolf'
    )
    review69=Review(
        comment="Dark and creepy in all the right ways",rating=4,user_id=3, book_id=64,
        created_at=datetime(2022,1,8),user_username='lone_centurion'
    )
    review70=Review(
        comment="Not my fav",rating=3,user_id=4, book_id=66,
        created_at=datetime(2019,6,5),user_username='the_bride'
    )
    review71=Review(
        comment="Met Expectations",rating=3,user_id=4, book_id=68,
        created_at=datetime(2022,6,5),user_username='the_bride'
    )
    review72=Review(
            comment="Blew me out of the water",rating=5,user_id=1, book_id=69,
            created_at=datetime(2021,4,5),user_username='Demo'
        )
    review73=Review(
            comment="Needed polishing up",rating=2,user_id=2, book_id=70,
            created_at=datetime(2023,4,19),user_username='marnie'
        )
    review74=Review(
            comment="Hated every second of it",rating=1,user_id=3, book_id=71,
            created_at=datetime(2021,6,25),user_username='lone_centurion'
        )
    review75=Review(
            comment="Amazing!!",rating=4,user_id=5, book_id=72,
            created_at=datetime(2022,7,5),user_username='pandorica'
        )
    review76=Review(
            comment="Pretty great",rating=4,user_id=7, book_id=73,
            created_at=datetime(2021,8,5),user_username='melody'
        )
    review77=Review(
            comment="Seen it a hundred times wanted something more",rating=3,user_id=6, book_id=74,
            created_at=datetime(2022,9,13),user_username='bad_wolf'
        )
    review78=Review(
            comment="To die for",rating=5,user_id=1, book_id=75,
            created_at=datetime(2022,11,5),user_username='Demo'
        )
    review79=Review(
            comment="i need more books like this",rating=4,user_id=2, book_id=76,
            created_at=datetime(2022,4,15),user_username='marnie'
        )
    review80=Review(
            comment="Are you surereading thin isn't considered torture??",rating=1,user_id=4, book_id=78,
            created_at=datetime(2022,8,17),user_username='the_bride'
        )
    review81=Review(
            comment="i need more books like this",rating=4,user_id=2, book_id=77,
            created_at=datetime(2022,4,15),user_username='marnie'
        )
    review82=Review(
        comment="The pacing was a little off but otherwise good",rating=3,user_id=3, book_id=78,
        created_at=datetime(2021,11,9),user_username='lone_centurion'
    )
    review83=Review(
        comment="Met Expectations",rating=3,user_id=4, book_id=79,
        created_at=datetime(2022,6,5),user_username='the_bride'
    )
    review84=Review(
            comment="Blew me out of the water",rating=5,user_id=1, book_id=80,
            created_at=datetime(2021,4,5),user_username='Demo'
        )
    review85=Review(
            comment="Needed polishing up",rating=2,user_id=2, book_id=81,
            created_at=datetime(2023,4,19),user_username='marnie'
        )
    review86=Review(
            comment="Hated every second of it",rating=1,user_id=3, book_id=82,
            created_at=datetime(2021,6,25),user_username='lone_centurion'
        )
    review87=Review(
            comment="Amazing!!",rating=4,user_id=5, book_id=83,
            created_at=datetime(2022,7,5),user_username='pandorica'
        )
    review88=Review(
            comment="Pretty great",rating=4,user_id=7, book_id=89,
            created_at=datetime(2021,8,5),user_username='melody'
        )
    review89=Review(
            comment="Seen it a hundred times wanted something more",rating=3,user_id=6, book_id=85,
            created_at=datetime(2022,9,13),user_username='bad_wolf'
        )
    review90=Review(
            comment="To die for",rating=5,user_id=1, book_id=86,
            created_at=datetime(2022,11,5),user_username='Demo'
        )
    review91=Review(
            comment="i need more books like this",rating=4,user_id=2, book_id=87,
            created_at=datetime(2022,4,15),user_username='marnie'
        )
    review92=Review(
            comment="Are you surereading thin isn't considered torture??",rating=1,user_id=4, book_id=88,
            created_at=datetime(2022,8,17),user_username='the_bride'
        )
    review93=Review(
            comment="Loved them!!",rating=4,user_id=1, book_id=90,
            created_at=datetime(2022,9,4),user_username='Demo'
        )
    review94=Review(
            comment="Loved the badass characters",rating=4,user_id=6, book_id=95,
            created_at=datetime(2014,6,4),user_username='bad_wolf'
        )
    review95=Review(
            comment="Nope Nope Nope",rating=1,user_id=1, book_id=92,
            created_at=datetime(2022,9,4),user_username='Demo'
        )
    review96=Review(
            comment="The pacing was a little off but otherwise good",rating=3,user_id=3, book_id=93,
            created_at=datetime(2021,11,9),user_username='lone_centurion'
        )
    review97=Review(
            comment="The pacing was a little off but otherwise good",rating=3,user_id=3, book_id=94,
            created_at=datetime(2021,11,9),user_username='lone_centurion'
        )
    review98=Review(
        comment="Amazing!!",rating=4,user_id=5, book_id=96,
        created_at=datetime(2022,7,5),user_username='pandorica'
    )
    review99=Review(
        comment="Pretty great",rating=4,user_id=7, book_id=97,
        created_at=datetime(2021,8,5),user_username='melody'
    )
    review100=Review(
        comment="Gret representation.",rating=4,user_id=1, book_id=98,
        created_at=datetime(2022,9,4),user_username='Demo'
    )
    review101=Review(
        comment="Loved the badass characters",rating=4,user_id=6, book_id=99,
        created_at=datetime(2014,6,4),user_username='bad_wolf'
    )
    review102=Review(
        comment="Nope Nope Nope",rating=1,user_id=1, book_id=100,
        created_at=datetime(2022,9,4),user_username='Demo'
    )
    review103=Review(
        comment="Met Expectations",rating=3,user_id=4, book_id=104,
        created_at=datetime(2022,6,5),user_username='the_bride'
    )
    review104=Review(
            comment="Blew me out of the water",rating=5,user_id=1, book_id=102,
            created_at=datetime(2021,4,5),user_username='Demo'
        )
    review105=Review(
            comment="Needed polishing up",rating=2,user_id=2, book_id=103,
            created_at=datetime(2023,4,19),user_username='marnie'
        )
    review106=Review(
            comment="Hated every second of it",rating=1,user_id=3, book_id=101,
            created_at=datetime(2021,6,25),user_username='lone_centurion'
        )
    review107=Review(
            comment="Amazing!!",rating=4,user_id=5, book_id=105,
            created_at=datetime(2022,7,5),user_username='pandorica'
        )
    review108=Review(
        comment="Met Expectations",rating=3,user_id=4, book_id=106,
        created_at=datetime(2022,6,5),user_username='the_bride'
    )
    review109=Review(
        comment="Blew me out of the water",rating=5,user_id=1, book_id=107,
        created_at=datetime(2021,4,5),user_username='Demo'
    )
    review110=Review(
        comment="Amazing!!",rating=4,user_id=5, book_id=108,
        created_at=datetime(2022,7,5),user_username='pandorica'
    )
    review111=Review(
        comment="Pretty great",rating=4,user_id=7, book_id=109,
        created_at=datetime(2021,8,5),user_username='melody'
    )
    review112=Review(
        comment="To die for",rating=5,user_id=1, book_id=110,
        created_at=datetime(2022,11,5),user_username='Demo'
    )
    review113=Review(
        comment="Nope Nope Nope",rating=1,user_id=1, book_id=111,
        created_at=datetime(2022,9,4),user_username='Demo'
    )
    review114=Review(
        comment="Met Expectations",rating=3,user_id=4, book_id=112,
        created_at=datetime(2022,6,5),user_username='the_bride'
    )
    review115=Review(
        comment="Met Expectations",rating=3,user_id=4, book_id=113,
        created_at=datetime(2022,6,5),user_username='the_bride'
    )
    review116=Review(
            comment="Blew me out of the water",rating=5,user_id=1, book_id=114,
            created_at=datetime(2021,4,5),user_username='Demo'
        )
    review117=Review(
            comment="Needed polishing up",rating=2,user_id=2, book_id=119,
            created_at=datetime(2023,4,19),user_username='marnie'
        )
    review118=Review(
            comment="Hated every second of it",rating=1,user_id=3, book_id=116,
            created_at=datetime(2021,6,25),user_username='lone_centurion'
        )
    review119=Review(
            comment="Amazing!!",rating=4,user_id=5, book_id=117,
            created_at=datetime(2022,7,5),user_username='pandorica'
        )
    review120=Review(
            comment="Pretty great",rating=4,user_id=7, book_id=118,
            created_at=datetime(2021,8,5),user_username='melody'
        )
    review121=Review(
            comment="Seen it a hundred times wanted something more",rating=3,user_id=6, book_id=120,
            created_at=datetime(2022,9,13),user_username='bad_wolf'
        )
    review122=Review(
            comment="To die for",rating=5,user_id=1, book_id=121,
            created_at=datetime(2022,11,5),user_username='Demo'
        )
    review123=Review(
            comment="i need more books like this",rating=4,user_id=2, book_id=122,
            created_at=datetime(2022,4,15),user_username='marnie'
        )
    review124=Review(
        comment="Met Expectations",rating=3,user_id=4, book_id=123,
        created_at=datetime(2022,6,5),user_username='the_bride'
    )
    review125=Review(
            comment="Blew me out of the water",rating=5,user_id=1, book_id=124,
            created_at=datetime(2021,4,5),user_username='Demo'
        )
    review126=Review(
            comment="Blew me out of the water",rating=5,user_id=1, book_id=131,
            created_at=datetime(2021,4,5),user_username='Demo'
        )
    review127=Review(
            comment="Needed polishing up",rating=2,user_id=2, book_id=126,
            created_at=datetime(2023,4,19),user_username='marnie'
        )
    review128=Review(
            comment="Hated every second of it",rating=1,user_id=3, book_id=128,
            created_at=datetime(2021,6,25),user_username='lone_centurion'
        )
    review129=Review(
            comment="Amazing!!",rating=4,user_id=5, book_id=125,
            created_at=datetime(2022,7,5),user_username='pandorica'
        )
    review130=Review(
            comment="Pretty great",rating=4,user_id=7, book_id=130,
            created_at=datetime(2021,8,5),user_username='melody'
        )
    review131=Review(
            comment="Seen it a hundred times wanted something more",rating=3,user_id=6, book_id=127,
            created_at=datetime(2022,9,13),user_username='bad_wolf'
        )
    review132=Review(
            comment="To die for",rating=5,user_id=1, book_id=129,
            created_at=datetime(2022,11,5),user_username='Demo'
        )
    review133=Review(
        comment="Nope Nope Nope",rating=1,user_id=1, book_id=132,
        created_at=datetime(2022,9,4),user_username='Demo'
    )
    review134=Review(
        comment="The pacing was a little off but otherwise good",rating=3,user_id=3, book_id=133,
        created_at=datetime(2021,11,9),user_username='lone_centurion'
    )
    review135=Review(
            comment="To die for",rating=5,user_id=1, book_id=134,
            created_at=datetime(2022,11,5),user_username='Demo'
        )
    review136=Review(
            comment="i need more books like this",rating=4,user_id=2, book_id=135,
            created_at=datetime(2022,4,15),user_username='marnie'
        )
    review137=Review(
        comment="Met Expectations",rating=3,user_id=4, book_id=141,
        created_at=datetime(2022,6,5),user_username='the_bride'
    )
    review138=Review(
            comment="Blew me out of the water",rating=5,user_id=1, book_id=145,
            created_at=datetime(2021,4,5),user_username='Demo'
        )
    review139=Review(
            comment="Blew me out of the water",rating=5,user_id=1, book_id=146,
            created_at=datetime(2021,4,5),user_username='Demo'
        )
    review140=Review(
            comment="Needed polishing up",rating=2,user_id=2, book_id=140,
            created_at=datetime(2023,4,19),user_username='marnie'
        )
    review141=Review(
            comment="Hated every second of it",rating=1,user_id=3, book_id=136,
            created_at=datetime(2021,6,25),user_username='lone_centurion'
        )
    review142=Review(
            comment="Amazing!!",rating=4,user_id=5, book_id=137,
            created_at=datetime(2022,7,5),user_username='pandorica'
        )
    review143=Review(
            comment="Pretty great",rating=4,user_id=7, book_id=143,
            created_at=datetime(2021,8,5),user_username='melody'
        )
    review144=Review(
            comment="Seen it a hundred times wanted something more",rating=3,user_id=6, book_id=142,
            created_at=datetime(2022,9,13),user_username='bad_wolf'
        )
    review145=Review(
            comment="To die for",rating=5,user_id=1, book_id=138,
            created_at=datetime(2022,11,5),user_username='Demo'
        )
    review146=Review(
        comment="Nope Nope Nope",rating=1,user_id=1, book_id=144,
        created_at=datetime(2022,9,4),user_username='Demo'
    )
    review147=Review(
        comment="The pacing was a little off but otherwise good",rating=3,user_id=3, book_id=139,
        created_at=datetime(2021,11,9),user_username='lone_centurion'
    )
    review148=Review(
        comment="The FMC was a badass!!",rating=5,user_id=7, book_id=147,
        created_at=datetime(2023,4,5),user_username='melody'
    )
    review149=Review(
        comment="AWESOME!!",rating=5,user_id=3, book_id=148,
        created_at=datetime(2023,8,7),user_username='lone_centurion'
    )
    review150=Review(
        comment="Liked the premise, but pacing probs",rating=3,user_id=2, book_id=149,
        created_at=datetime(2017,8,9),user_username='marnie'
    )
    review151=Review(
        comment="Nope Nope Nope",rating=1,user_id=1, book_id=150,
        created_at=datetime(2022,9,4),user_username='Demo'
    )

    db.session.add(demo)
    db.session.add(marnie)
    db.session.add(rory)
    db.session.add(donna)
    db.session.add(amy)
    db.session.add(rose)
    db.session.add(river)
    db.session.add_all([genre1,genre2,genre3,genre4,genre5])
    db.session.add_all([subgenre1,subgenre2,subgenre3,subgenre4,subgenre5,subgenre6,subgenre7,subgenre8,subgenre9,subgenre10,
                        subgenre11,subgenre12,subgenre13,subgenre14,subgenre15,subgenre16,subgenre17,subgenre18,subgenre19,subgenre20])
    db.session.add_all([book1,book2,book3,book4,book5,book6,book7,book8,book9,book10,
                        book11,book12,book13,book14,book15,book16,book17,book18,book19,book20,
                        book21,book22,book23,book24,book25,book26,book27,book28,book29,book30,
                        book31,book32,book33,book34,book35,book36,book37,book38,book39,book40,
                        book41,book42,book43,book44,book45,book46,book47,book48,book49,book50,
                        book51,book52,book53,book54,book55,book56,book57,book58,book59,book60,
                        book61,book62,book63,book64,book65,book66,book67,book68,book69,book70,
                        book71,book72,book73,book74,book75,book76,book77,book78,book79,book80,
                        book81,book82,book83,book84,book85,book86,book87,book88,book89,book90,
                        book91,book92,book93,book94,book95,book96,book97,book98,book99,book100,
                        book101,book102,book103,book104,book105,book106,book107,book108,book109,book110,
                        book111,book112,book113,book114,book115,book116,book117,book118,book119,book120,
                        book121,book122,book123,book124,book125,book126,book127,book128,book129,book130,
                        book131,book132,book133,book134,book135,book136,book137,book138,book139,book140,
                        book141,book142,book143,book144,book145,book146,book147,book148,book149,book150])
    db.session.add_all([review1,review2,review3,review4,review5,review6,review7,review8,review9,review10,
                        review11,review12,review13,review14,review15,review16,review17,review18,review19,review20,
                        review21,review22,review23,review24,review25,review26,review27,review28,review29,review30,
                        review31,review32,review33,review34,review35,review36,review37,review38,review39,review40,
                        review41,review42,review43,review44,review45,review46,review47,review48,review49,review50,
                        review51,review52,review53,review54,review55,review56,review57,review58,review59,review60,
                        review61,review62,review63,review64,review65,review66,review67,review68,review69,review70,
                        review71,review72,review73,review74,review75,review76,review77,review78,review79,review80,
                        review81,review82,review83,review84,review85,review86,review87,review88,review89,review90,
                        review91,review92,review93,review94,review95,review96,review97,review98,review99,review100,
                        review101,review102,review103,review104,review105,review106,review107,review108,review109,review110,
                        review111,review112,review113,review114,review115,review116,review117,review118,review119,review120,
                        review121,review122,review123,review124,review125,review126,review127,review128,review129,review130,
                        review131,review132,review133,review134,review135,review136,review137,review138,review139,review140,
                        review141,review142,review143,review144,review145,review146,review147,review148,review149,review150, review151])
    db.session.add_all([ wishlist1,wishlist2]) 
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
