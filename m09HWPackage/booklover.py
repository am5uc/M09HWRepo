import pandas as pd
import numpy as np

class BookLover:
    def __init__(self, name, email, fav_genre, num_books=None, book_list=None):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        if num_books is None:
            self.num_books = 0
        else:
            self.num_books = num_books
        if book_list is None:
            self.book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})
        else:
            self.book_list = book_list
       # self.book_list = pd.DataFrame({'book_name':[], 'book_rating':[]}) is None else book_list
    
    def add_book(self, book_name, rating):
        if book_name in self.book_list.book_name.values:
            print("Book Name already in list")
        else:
            new_book = pd.DataFrame({
                'book_name': [book_name], 
                'book_rating': [rating]
            })
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1
    
    def has_read(self, book_name):
        if book_name in self.book_list.book_name.values:
            return True
        else:
            return False
        
    def num_books_read(self):
        return self.num_books
    
    def fav_books(self):
        return self.book_list[self.book_list.book_rating > 3]
        
    
if __name__ == '__main__':
    
    test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
    test_object.add_book("War of the Worlds", 4)
    test_object.add_book("War of the Worlds2", 4)
    test_object.add_book("War of the Worlds3", 3)
    test_object.add_book("War of the Worlds2", 4)
    print(test_object.num_books_read())
    print(test_object.fav_books())
    print(test_object.has_read("War of the Worlds2"))
    print(test_object.has_read("Abhi"))
        # And so forth