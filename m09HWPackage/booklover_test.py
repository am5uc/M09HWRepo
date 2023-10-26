import pandas as pd
import numpy as np
import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("War of the Worlds", 4)
        assert test_object.has_read("War of the Worlds"), "Not been read"
        assert test_object.num_books_read() == 1, "Number of Books is incorrect"
        
    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("War of the Worlds", 4)
        test_object.add_book("War of the Worlds", 4)
        assert test_object.num_books_read() == 1, "Same book entered twice"
        
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("War of the Worlds", 4)
        assert test_object.has_read("War of the Worlds"), "Not been read"
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("War of the Worlds", 4)
        assert test_object.has_read("War of the Worlds2") == False, "Not in list"
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("War of the Worlds", 4)
        test_object.add_book("War of the Worlds2", 4)
        test_object.add_book("War of the Worlds3", 3)
        assert test_object.num_books_read() == 3, "Number of books calculation incorrect"
        
    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("War of the Worlds", 4)
        test_object.add_book("War of the Worlds2", 4)
        test_object.add_book("War of the Worlds3", 3)
        assert (test_object.fav_books().book_rating > 3).all() , "Incorrect Favorite books"

                
if __name__ == '__main__':
    
    unittest.main(verbosity=3)
    blts = BookLoverTestSuite()
    blts.test_1_add_book()
    blts.test_2_add_book()
    blts.test_3_has_read()
    blts.test_4_has_read()
    blts.test_5_num_books_read()
    blts.test_6_fav_books()