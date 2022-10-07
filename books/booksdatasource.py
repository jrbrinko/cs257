#!/usr/bin/env python3
'''
    booksdatasource.py
    Jeff Ondich, 21 September 2022

    For use in the "books" assignment at the beginning of Carleton's
    CS 257 Software Design class, Fall 2022.
'''

import csv


class Author:
    def __init__(self, surname='', given_name='', birth_year=None, death_year=None):
        self.surname = surname
        self.given_name = given_name
        self.birth_year = birth_year
        self.death_year = death_year

    def __eq__(self, other):
        ''' For simplicity, we're going to assume that no two authors have the same name. '''
        return self.surname == other.surname and self.given_name == other.given_name
        
    def __str__(self):
        '''serves as author print function'''
        return (f"{self.given_name} {self.surname} ({self.birth_year}-{self.death_year})")

class Book:
    def __init__(self, title='', publication_year=None, authors=[]):
        ''' Note that the self.authors instance variable is a list of
            references to Author objects. '''
        self.title = title
        self.publication_year = publication_year
        self.authors = authors


    def __eq__(self, other):
        ''' We're going to make the excessively simplifying assumption that
            no two books have the same title, so "same title" is the same
            thing as "same book". '''
        return self.title == other.title

class BooksDataSource:

    def __init__(self,books_csv_file_name):
        ''' The books CSV file format looks like this:

                title,publication_year,author_description

            For example:

                All Clear,2010,Connie Willis (1945-)
                "Right Ho, Jeeves",1934,Pelham Grenville Wodehouse (1881-1975)

            This __init__ method parses the specified CSV file and creates
            suitable instance variables for the BooksDataSource object containing
            a collection of Author objects and a collection of Book objects.
        '''

        # All authors and books objects for instance of class
        self.allAuthors = []
        self.allBooks = []

        # Opens the CSV file and stores data
        with open(books_csv_file_name, newline='') as f:
            reader = csv.reader(f)
            data = list(reader)

        for d in data:
            unparsed_entry = d.pop(2) #removes the last unparsed 
            two_authors = unparsed_entry.split(' and ') #splitting multiple authors first, each author is then handled seperately
            newAuthors = [] 
            for a in two_authors: #assigning author constructor parameters
                parsed_entry = a.split(' (')
                name = parsed_entry[0].split(' ')
                years = parsed_entry[1].split('-')
                given_name = name[0]
                surname = name[1] 
                birth_year = years[0]
                death_year = years[1][:-1] 
            
                newAuthor = Author(surname, given_name, birth_year, death_year) #Constructing author(s) and book, adding to global lists
                newAuthors.append(newAuthor)
                if newAuthor not in self.allAuthors: 
                    self.allAuthors.append(newAuthor) 
            newBook = Book(d[0], int(d[1]), newAuthors)
            if newBook not in self.allBooks:
                self.allBooks.append(newBook) 


    def authors(self, search_text=None):
        ''' Returns a list of all the Author objects in this data source whose names contain
            (case-insensitively) the search text. If search_text is None, then this method
            returns all of the Author objects. In either case, the returned list is sorted
            by surname, breaking ties using given name (e.g. Ann Brontë comes before Charlotte Brontë).
        '''
        authorSearch = []
        if search_text is not None:
            for author in self.allAuthors: #checking for search matches
                if (search_text.lower() in author.surname.lower()) or (search_text.lower() in author.given_name.lower()):
                    authorSearch.append(author)
        else:
            authorSearch = self.allAuthors

        return sorted(authorSearch, key=lambda x:(x.surname, x.given_name)) #sorting output by surname

    def books(self, search_text=None, sort_by='title'):
        ''' Returns a list of all the Book objects in this data source whose
            titles contain (case-insensitively) search_text. If search_text is None,
            then this method returns all of the books objects.

            The list of books is sorted in an order depending on the sort_by parameter:

                'year' -- sorts by publication_year, breaking ties with (case-insenstive) title
                'title' -- sorts by (case-insensitive) title, breaking ties with publication_year
                default -- same as 'title' (that is, if sort_by is anything other than 'year'
                            or 'title', just do the same thing you would do for 'title')
        '''
        # All books that fit the constraint
        returnedBooks = [] 
        if (search_text == None):
            # No search text return all books
            returnedBooks = self.allBooks
        else:
            # Goes through all books and checks to see if the search text
            # is in it.
            for aBook in self.allBooks:
                if search_text.lower() in aBook.title.lower():
                    returnedBooks.append(aBook)

        # Returns the books by sort
        if (sort_by == 'year'):
            # Sorted by year 
            return sorted(returnedBooks, key=lambda x:(x.publication_year, x.title))
        else:
            # Sorted by title
            return sorted(returnedBooks, key=lambda x:(x.title, x.publication_year))

    def books_between_years(self, start_year=None, end_year=None):
        ''' Returns a list of all the Book objects in this data source whose publication
            years are between start_year and end_year, inclusive. The list is sorted
            by publication year, breaking ties by title (e.g. Neverwhere 1996 should
            come before Thief of Time 1996).

            If start_year is None, then any book published before or during end_year
            should be included. If end_year is None, then any book published after or
            during start_year should be included. If both are None, then all books
            should be included.
        '''
        if (start_year == 'None') or (start_year is None): #checking for None parameter
            start_year = 0 #assigning min year
        else:
            try:
                start_year = int(start_year)
            except:
                print("Use int type for start and end year. To indicate no start or end year, use None.")
                exit()
        if (end_year == 'None') or (end_year is None): #checking for None parameter
            end_year = 3000 #assigning max year
        else:
            try:
                end_year = int(end_year)
            except:
                print("Use int type for start and end year. To indicate no start or end year, use None.")
                exit() 

        # List of books in the range that are going to be returned.
        bookList = []
    
        # Goes through all books based on the publication year.
        for b in self.allBooks:
            if start_year <= b.publication_year <= end_year:
                bookList.append(b)

        # Returns sorted list based on publication year.
        return sorted(bookList, key= lambda x: (x.publication_year, x.title))

def main():
    pass

if __name__ == "__main__":
    main()