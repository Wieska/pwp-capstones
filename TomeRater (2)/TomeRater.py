# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 14:10:03 2018
Python 3.6
@author: Wieske
"""

class User(object):
    def __init__(self, name, email):
        #user object is created by User(name, email)
        #it automatically also adds in a dict of books that starts out empty
        self.name = name
        self.email = email
        self.books = {}
        
    def get_email(self):
        #returns the users' email
        return self.email

    def change_email(self, new_email, TomeRater):
        #updates email addres to new_email
        #I have repeatedly tried to update the User in TomeRater.users to have a key that would be the new
        #email address as well. It appears I can't call the TomeRater class in here. Or I cannot change
        #the key of the accompanying value from inside that value. 
        #That is why you now have to give in your TomeRater object as well.
        #This way it can point to the check_email() method inside the TomeRater class.
        #Ideally I would have liked to have done this: #TomeRater.users[new_email] = TomeRater.users.pop(self.email)
        #This is what happens in TomeRater.check_email()
        #I tried this: TomeRater.users.update({new_email: User(self.name, new_email, self.books)})
        #I tried this: TomeRater.add_user(self.name, new_email, self.books)
        #As it is now it works as I want it to. Except that you have to give in your TomeRater class object.
        if "@" in new_email:
            self.email = new_email
            TomeRater.check_email()
            print ("Your email address was updated. It is now {email}".format(email=self.email))
        else:
            print ("Please enter a valid emailaddress.")

    def __repr__(self):
        #returns string "User: name, email: emailaddres, books read: number of books read
        return ("User: {user}, email: {email}, books read: {books}".format(user=self.name, email=self.email, books=len(self.books)))

    def __eq__(self, other_user):
        if isinstance(other_user, self.__class__):
            return self.name == other_user.name and self.email == other_user.email
        else:
            return False
        
    def read_book(self, book, rating=None):
        self.books[book] = rating
        #adds {book:rating} to dictionary self.books
        #should also add book to TR.users {Book(): #users read}
    
    def get_average_rating(self):
        #Will calculate the average rating given by a user.
        number_of_books = len(self.books)
        sum_ratings =  0
        for book, rating in self.books.items():
            if type(rating) == int:
                sum_ratings += rating
        av = sum_ratings/number_of_books
        return av
    
class Book(object):
    def __init__(self, title, isbn):
        #a book object is created with Book(title, isbn)
        #this book should be added to books in TomeRater, which will happen when books
        # get added with the add_book_to_user method in TomeRater.
        self.title = title
        self.isbn = isbn
        #self.price = price
        self.ratings = []
    
    def __repr__(self):
        return "{title} with the following ISBN {isbn}".format(title=self.title, isbn=self.isbn)
        
    def __hash__(self):
        return hash((self.title, self.isbn))
    
    def get_title(self):
        #returns title of book
        return self.title
    
    def get_isbn(self):
        #returns ISBN of book
        return self.isbn
    
    '''def get_price(self):
        #returns price of book
        return self.price'''
    
    def set_isbn(self, new_isbn):
        #sets new isbn to be isbn number of the book.
        #Should also print message saying the book's ISBN was updated
        self.isbn = new_isbn
        return ("The ISBN number for {title} is updated to {isbn}".format(title=self.title, isbn=self.isbn))
    
    def add_rating(self, rating):
        #adds rating to list of self.ratings
        #min 0, max 4, otherwise should print "Invalid Rating"
        if rating >= 0 and rating <= 4:
            self.ratings += [rating]
        else:
            print("Invalid Rating")
            
    def __eq__(self, other_book):
        #A book object should be equal to another book
        # if they both have the same title & ISBN
        if isinstance(other_book, self.__class__):
            return self.title == other_book.title and self.isbn == other_book.isbn
        else:
            return False
            
    def get_average_rating(self):
        #This will return the average rating of the book.
        number_of_ratings = len(self.ratings)
        sum_ratings =  0
        if number_of_ratings == 0:
            return "Nothing rated"
        else:
            for rating in self.ratings:
                sum_ratings += rating
            return sum_ratings/number_of_ratings
    
class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author
        
    def get_author(self):
        #returns the author
        return self.author
        
    def __repr__(self):
        #returns string {title} by {author}
        return "{title} by {author}".format(title=self.title, author=self.author)
    
class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level
        
    def get_subject(self):
        #returns subject (str)
        return self.subject
    
    def get_level(self):
        #returns level (str)
        return self.level
    
    def __repr__(self):
        #returns {title}, a {level} manual on {subject}
        return "{title}, a {level} manual on {subject}".format(title=self.title, level=self.level, subject=self.subject)
    
    
class TomeRater(object):
    #Database containing two dictionaries. One books and one of users.
    def __init__(self):
        self.users = {} #users will store {email: User()}
        self.books = {} #books will store {book(): #users read}
    
    def __eq__(self, other_db):
        if isinstance(other_db, self.__class__):
            if self.users == other_db.users and self.books == other_db.books:
                print("There are two identical TomaRater databases in your system... Did you encounter a parallel universe?")
                return True
        else:
            return False
    
    def __repr__(self):
        #returns string "This database contains # users who have read a total of # unique books a total of # times.
        no_books = len(self.books)
        no_users = len(self.users)
        amount = 0
        for times_read in self.books.values():
            amount += times_read
        return ("This database contains {no_users} users who have read {no_unique_books} unique books a total of {amount} times.".format(no_users=no_users, no_unique_books=no_books, amount=amount))

    def create_book(self, title, isbn):
        return Book(title, isbn) #creates a book object
            
    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn) #creates a fiction object (book as parent)
        
    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn) #creates a non fiction object (book as parent)
    
    def check_email(self):
        #This method checks if there are items in self.users of whom the 
        #emailaddress in the key does not correspond 
        # with the emailaddress that is in the user object. 
        #And will adjust this when they don't match.
        #This check is performed/called when somebody changes their emailaddres.
        for key, value in self.users.items():
            if key != value.email:
                self.users[value.email] = self.users.pop(key)
                print("Updated user database")
                
    '''def check_isbn(self):
        #This method checks whether two books have the same ISBN.
        #It will perform this check when an ISBN has been set.
        isbn_check = []
        for book in self.books.keys():
            if book.get_isbn() not in isbn_check:
                isbn_check.append = book.get_isbn()
            else:
                return "This book {title} does not have an unique ISBN!!.".format(title = book.get_title())'''
                  
    
    def add_book_to_user(self, book, email, rating=None):
        #should add a book to self.books in Tomerater.
        #should add book to user in User
        if rating != None:
            book.add_rating(rating)        
        #try & except
        if email in self.users.keys():
            user = self.users[email]
            user.read_book(book, rating)
            if book in self.books:
                self.books[book] += 1
            else:
                self.books[book] = 1
        else:
            print("No user with email {email}!".format(email=email))
    
    def add_user(self, name, email, user_books=None):
        #creates a user object within self.users
        #adds this user object to TomeRater self.users
        self.users[email] = User(name, email)
        
        #User(name, email, books)
        #Adds book to booklist of user
        if user_books != None:
            for book in user_books:
                self.add_book_to_user(book, email)
    
       
    def print_catalog(self):
        #should print every item in self.books
        for item in self.books:
            print(item)
    
    def print_users(self):
        # should print all the users in self.users
        for email, user in self.users.items():
            print(user)
    
    def most_read_book(self):
        #returns book that was most read by users.
        most_read = None
        highest_value = 0
        for book in self.books.keys():
            if most_read == None:
                most_read = book
                highest_value = self.books[book]
            else:
                if highest_value < self.books[book]:
                    highest_value = self.books[book]
                    most_read = book
        return most_read

    def highest_rated_book(self):
        #returns book with highest average rating
        highest_rated = None
        highest_rating = 0
        for book in self.books.keys():            
            rating = book.get_average_rating()
            if highest_rated == None or type(highest_rated) == str:
                highest_rating = rating
                highest_rated = book               
            else:
                if highest_rating < rating:
                    highest_rating = rating
                    highest_rated = book
        return highest_rated
                
    def most_positive_user(self):
        # should return user with highest average rating
        highest_average = 0
        positive_user = None
        for email, user in self.users.items():
            if positive_user == None:
                highest_average = user.get_average_rating()
                positive_user = user
            else:
                if highest_average < user.get_average_rating():
                    highest_average = user.get_average_rating()
                    positive_user = user
        return positive_user
    
 
            
        