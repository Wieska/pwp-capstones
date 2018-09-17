from TomeRater import *

Tome_Rater = TomeRater()
#Tom_Rat = TomeRater()
#Tom_Rat2 = TomeRater()
#Create some books:

book1 = Tome_Rater.create_book("Society of Mind", 12345678, 12)
novel1 = Tome_Rater.create_novel("Alice In Wonderland", "Lewis Carroll", 12345, 5)
novel1.set_isbn(9781536831139, Tome_Rater)
nonfiction1 = Tome_Rater.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929452, 9)
nonfiction2 = Tome_Rater.create_non_fiction("Computing Machinery and Intelligence", "AI", "advanced", 11111938, 2)
novel2 = Tome_Rater.create_novel("The Diamond Age", "Neal Stephenson", 10101010, 45)
novel3 = Tome_Rater.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001000, 8)

#book4 = Tom_Rat.create_book("Society of Mind", 12345678)
#book5 = Tom_Rat2.create_book("Society of Mind", 12345678)
#book5 = Tome_Rater.create_book("If only you knew", 12345678)

#Tom_Rat.add_user("Alan Turing", "alan@turing.com")
#Tom_Rat2.add_user("Alan Turing", "alan@turing.com")
#Tom_Rat.add_book_to_user(book4, "alan@turing.com", 1)
#Tom_Rat2.add_book_to_user(book4, "alan@turing.com", 1)

#print(Tom_Rat == Tom_Rat2)
#print("anything?")
#Create users:
Tome_Rater.add_user("Alan Turing", "alan@turing.com")
Tome_Rater.add_user("David Marr", "david@computation.org")

#Add a user with three books already read:
Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu", user_books=[book1, novel1, nonfiction1])

#Add books to a user one by one, with ratings:
Tome_Rater.add_book_to_user(book1, "alan@turing.com", 1)
Tome_Rater.add_book_to_user(novel1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction2, "alan@turing.com", 4)
Tome_Rater.add_book_to_user(novel3, "alan@turing.com", 1)

Tome_Rater.add_book_to_user(novel2, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "david@computation.org", 4)

Tome_Rater.add_user("Wieske", "wies@me.nl", user_books=[book1, novel2, nonfiction2])
#Uncomment these to test your functions:
#Tome_Rater.print_catalog()
#Tome_Rater.print_users()
#print(Tome_Rater.users.pop("wies@me.nl"))
#print("After popping")
#Tome_Rater.print_users()
#print("Most positive user:")
#print(Tome_Rater.most_positive_user())
print("Highest rated book:")
print(Tome_Rater.highest_rated_book())
print("Most read book:")
print(Tome_Rater.most_read_book())

Tome_Rater.print_users()
Tome_Rater.users["marvin@mit.edu"].change_email("marvin@EDX.org",Tome_Rater)
#print(Tome_Rater.users["marvin@mit.edu"])
#print(Tome_Rater.users["marvin@EDX.org"])
print("hoi")

#Tome_Rater.users["wies@u.nl"] = Tome_Rater.users.pop("wies@me.nl")
#Tome_Rater.users["you@you.nl"] = User("you", "you@you.nl")
#Tome_Rater.print_users()
#Tome_Rater.users.update({"mom@home.nl": User("mom", "mom@home.nl")})
#print(Tome_Rater)
#Tome_Rater.print_users()
#print(Tome_Rater.users["marvin@mit.edu"])
#print(Tome_Rater.users["marvin@EDX.org"])