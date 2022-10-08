'''
   books.py
   Revised by Amir Al-Sehikh and James Brink
   27 September 2022
'''
import booksdatasource
import sys


def usage_statement():
    #prints usage statement
    usage_txt = open('usage.txt', 'r')
    usage_contents = usage_txt.read()
    print(usage_contents)

def display_author(data_source):
    #display function associated with -a --author
    author_list = []
    if(len(sys.argv) == 2): #no search term
        author_list = data_source.authors()
    elif(len(sys.argv) == 3): #search term specified
        author_list = data_source.authors(sys.argv[2])
    else:
        print(usage_statement()) #help function otherwise

    for author in author_list: #print formatted string
         print(f'{author.given_name:10} {author.surname:10}')

def display_books(data_source):
    #display function associated with -b --book
    if(len(sys.argv) == 2): #no search term or sort specified
        book_list = data_source.books()
    elif(len(sys.argv) == 3): #search term specified
        book_list = data_source.books(sys.argv[2])
    elif(len(sys.argv) == 4): #search term and sort by specified
        book_list = data_source.books(sys.argv[2], sys.argv[3])
    for book in book_list:
        author_string = ''
        author_string += book.authors[0].__str__() 
        if len(book.authors) > 1: #appending second author name if necessary
            author_string += ' and ' + book.authors[1].__str__()

        print(f'{book.title:50} {book.publication_year:15} By: {author_string:10}') #print formatted string

def display_years(data_source):
    # display function for years
    # input: a booksdatasource file
    if(len(sys.argv) == 2): # no beginning and end year -> all books
        book_list = data_source.books_between_years()
    if(len(sys.argv) == 3): # beginning but no end year -> all books from a
        book_list = data_source.books_between_years(sys.argv[2])
    if(len(sys.argv) == 4): # books from A to B
        book_list = data_source.books_between_years(sys.argv[2], sys.argv[3])
    
    # Goes through books to print all strings
    for book in book_list:
        author_string = ''
        author_string += book.authors[0].__str__()
        if len(book.authors) > 1:
            author_string += ' and ' + book.authors[1].__str__()

        # prints books
        print(f'{book.title:50} {book.publication_year:15} By: {author_string:10}')

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
            usage_statement()

    # In case of invalid number of arguments
    else:
        usage_statement()

if __name__ == "__main__":
    main()