'''
   books.py
   Amir Al-Sehikh and James Brink
   27 September 2022
'''
import booksdatasource
import sys

def usage_statement():
    #prints usage statement
    print('SYNOPSIS')
    print('\t\t python3 booky.py [-b | -a | -y | -h [S1] [S2]')
    print('\n')
    print('DESCRIPTION')
    print('\t\t This program allows users to search a database of books. Users specify whether to search by book title, author title, or year  range. The program will return a list of the books and authors that match the search.')
    
    print('\n')
    print('\t -b --book \tGiven a search string S1, print a list of books whose titles contain S1 sorted by title or year. S is case insensitive (i.e. -b fire). S2 indicates sort type. Default sort type is by title.')

    print('\n')
    print('\t-a --author \tSearches book authors containing string S. Returns a list sorted alphabetically by author surname (i.e. -a smith).')

    print('\n')
    print('\ty --year \tGiven a range of years S1 to S2, prints the list of books published between years S1 to S2 (i.e. -y 1960 2000). Unspecified years default to None. Use -y None 2000 to search for all books before the year 2000')

    print('\n')
    print('\t-h --help\tGives the list of usage commands.')

def display_author(data_source):
    #display function associated with -a --author
    authorList = []
    if(len(sys.argv) == 2): #no search term
        authorList = data_source.authors()
    elif(len(sys.argv) == 3): #search term specified
        authorList = data_source.authors(sys.argv[2])
    else:
        print(usage_statement()) #help function otherwise

    for author in authorList: #print formatted string
         print(f'{author.given_name:10} {author.surname:10}')

def display_books(data_source):
    #display function associated with -b --book
    if(len(sys.argv) == 2): #no search term or sort specified
        bookList = data_source.books()
    elif(len(sys.argv) == 3): #search term specified
        bookList = data_source.books(sys.argv[2])
    elif(len(sys.argv) == 4): #search term and sort by specified
        bookList = data_source.books(sys.argv[2], sys.argv[3])
    for book in bookList:
        authorString = ''
        authorString += book.authors[0].str() 
        if len(book.authors) > 1: #appending second author name if necessary
            authorString += ' and ' + book.authors[1].str()

        print(f'{book.title:50} {book.publication_year:15} By: {authorString:10}') #print formatted string
   
def display_years(data_source):
    # display function for years
    # input: a booksdatasource file
    if(len(sys.argv) == 2): # no beginning and end year -> all books
        bookList = data_source.books_between_years()
    if(len(sys.argv) == 3): # beginning but no end year -> all books from a
        bookList = data_source.books_between_years(sys.argv[2])
    if(len(sys.argv) == 4): # books from A to B
        bookList = data_source.books_between_years(sys.argv[2], sys.argv[3])
    
    # Goes through books to print all strings
    for book in bookList:
        authorString = ''
        authorString += book.authors[0].str()
        if len(book.authors) > 1:
            authorString += ' and ' + book.authors[1].str()

        # prints books
        print(f'{book.title:50} {book.publication_year:15} By: {authorString:10}')
def main():

    # Creates instance of booksdatasource object =
    b = booksdatasource.BooksDataSource('books1.csv')
   
    # Checks the number of arguments.
    if 2 <= len(sys.argv) <= 4:

        # 'Books' argument
        if (sys.argv[1] in ['-b','--books']):
            display_books(b)
        
        # 'Author' argument
        elif (sys.argv[1] in ['-a', '--author']):
            display_author(b)

        # 'Year' argument
        elif (sys.argv[1] in ['-y', '--year']):
            display_years(b)
        
        # 'Help' argument
        else :
            print(usage_statement())

    # In case of invalid number of arguments
    else:
      print(usage_statement())

if __name__ == "__main__":
    main()