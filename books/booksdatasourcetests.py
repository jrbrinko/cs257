'''
   booksdatasourcetest.py
   Amir Al-Sehikh and James Brink
   23 September 2022
'''

from booksdatasource import Author, Book, BooksDataSource
import unittest

class BooksDataSourceTester(unittest.TestCase):
    def setUp(self):
        self.data_source = BooksDataSource('books1.csv')

    def tearDown(self):
        pass

    def test_unique_author(self):
        authors = self.data_source.authors('Pratchett')
        self.assertTrue(len(authors) == 1)
        self.assertTrue(authors[0] == Author('Pratchett', 'Terry'))

    def test_unique_books(self):
        books = self.data_source.books('Emma')
        self.assertTrue(len(books) == 1)
        self.assertTrue(books[0] == Book('Emma'))

    def test_all_books(self):
        self.data_source = BooksDataSource('tinybooks.csv')
        books = self.data_source.books()
        self.assertTrue(len(books) == 4)
        self.assertTrue(books[0] == Book('Emma'))
        self.assertTrue(books[1] == Book('Good Omens'))
        self.assertTrue(books[2] == Book('Neverwhere'))
    
    def test_all_authors(self):
        tiny_data_source = BooksDataSource('tinybooks.csv')
        authors = tiny_data_source.authors()
        self.assertTrue(len(authors) == 4)
        self.assertTrue(authors[1] == Author('Gaiman', 'Neil'))
        self.assertTrue(authors[0] == Author('Austen', 'Jane'))
        self.assertTrue(authors[2] == Author('Melville', 'Herman'))
    
    def test_author_tiebreak(self):
        authors = self.data_source.authors('bront')
        self.assertTrue(authors[0] == Author('Brontë', 'Ann'))
        self.assertTrue(authors[1] == Author('Brontë', 'Charlotte'))
        self.assertTrue(authors[2]== Author('Brontë', 'Emily'))

    def test_no_author(self):
        authors = self.data_source.authors('zzzzzzzzz')
        self.assertTrue(len(authors) == 0)

    def test_no_books(self):
        books = self.data_source.books('zzzzzzzzz')
        self.assertTrue(len(books) == 0)

    def test_author_sort(self):
        tiny_data_source = BooksDataSource('tinybooks.csv')
        authors = tiny_data_source.authors()
        self.assertTrue(len(authors) == 4)
        self.assertTrue(authors[0] == Author('Austen','Jane'))
    
    def test_book_sort_title(self):
        tiny_data_source = BooksDataSource('tinybooks.csv')
        books = tiny_data_source.books()
        self.assertTrue(len(books) == 4)
        self.assertTrue(books[0] == Book('Emma'))

    def test_book_sort_year_tiebreak(self):
        books = self.data_source.books('None', 'year')
        self.assertTrue(len(books) == 3)
        self.assertTrue(books[0] == Book('Emma'))

    def test_book_sort_year_tiebreak(self):
        tiebreak_data_source = BooksDataSource('tiebreak.csv')
        books = tiebreak_data_source.books(None, 'year')
        self.assertTrue(books[4] == Book('All Clear'))
        self.assertTrue(books[5] == Book('Blackout'))
        
    def test_book_sort_year(self):
        tiny_data_source = BooksDataSource('tinybooks.csv')
        books = tiny_data_source.books()
        self.assertTrue(len(books) == 4)
        self.assertTrue(books[0] == Book('Emma'))

    def test_year_search(self):
        tiny_data_source = BooksDataSource('tinybooks.csv')
        books = tiny_data_source.books_between_years('None', 1900)
        self.assertTrue(len(books) == 2)
        self.assertTrue(books[0] == Book(("Emma")))

    def test_year_search_no_params(self):
        tiny_data_source = BooksDataSource('tinybooks.csv')
        books = tiny_data_source.books_between_years()
        self.assertTrue(len(books) == 4)
         
    def test_year_between_two_params(self):
        tiny_data_source = BooksDataSource('tinybooks.csv')
        books_between = tiny_data_source.books_between_years(1847, 1996)
        self.assertTrue(books_between[0] == Book('Omoo'))
        
    def test_year_between_no_books(self):
        tiny_data_source = BooksDataSource('tinybooks.csv')
        books_between = tiny_data_source.books_between_years(3000, 4000)
        self.assertTrue(len(books_between) == 0)

if __name__ == '__main__':
    unittest.main()

