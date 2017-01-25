
import os
from book import Book
import json
import fileio
import datetime

DATA_DIR = 'data'
BOOKS_FILE_NAME = os.path.join(DATA_DIR, 'wishlist.txt')
COUNTER_FILE_NAME = os.path.join(DATA_DIR, 'counter.txt')

separator = '^^^'  # a string probably not in any valid data relating to a book

book_list = []
counter = 0

def setup():
    ''' Read book info from file, if file exists. '''

    global counter

    # if there is no file we get None returned

    book_data = fileio.read_from_file(BOOKS_FILE_NAME)

    if book_data is not None:

        make_book_list(book_data)

    count_data = fileio.read_from_file(COUNTER_FILE_NAME)

    # if we cannot cast book data to int then set it to 0
    if count_data is not None:
        try:
            counter = int(count_data)

        except ValueError:

            counter = 0

    else:
        counter = len(book_list)


def shutdown():
    '''Save all data to a file - one for books, one for the current counter value, for persistent storage'''

    output_data = make_output_data()

    # write data
    fileio.write_to_file(DATA_DIR, BOOKS_FILE_NAME, output_data)

    fileio.write_to_file(DATA_DIR, COUNTER_FILE_NAME, str(counter))


def get_books(**kwargs):
    ''' Return books from data store. With no arguments, returns everything. '''

    global book_list

    if len(kwargs) == 0:
        return book_list

    if 'read' in kwargs:
        read_books = [ book for book in book_list if book.read == kwargs['read'] ]
        return read_books



def add_book(book):
    ''' Add to db, set id value, return Book'''

    global book_list

    book.id = generate_id()
    book_list.append(book)

def delete_book(book_id): #(JEN)
    '''Remove unread book from db'''
    global book_list

    for book in book_list:

        if book.id == book_id:
            book_list.remove(book)


def generate_id():
    global counter
    counter += 1
    return counter


def set_read(book_id, read):
    '''Update book with given book_id to read. Return True if book is found in DB and update is made, False otherwise.'''

    global book_list

    for book in book_list:

        if book.id == book_id:

            book.read = True

            # https://docs.python.org/3/library/datetime.html#date-objects
            # date format 'YYYY-MM-DD'
            book.read_date = datetime.date.today().__str__()

            return True

    return False # return False if book id is not found

def set_delete(book_id, read):#(JEN)
    '''Delete book with given book_id. Return True if book is found in DB and update is made, False otherwise'''
    global book_list

    for book in book_list:

        if book.id == book_id:
            delete_book(book_id)
            return True

    return False # returns False if book id is not found

def edit_book(book_id):#(JEN)
    '''Update the book's author/title with the given book_id. Return true if book is found in DB and update is made, False otherwise.'''

    global book_list

    for book in book_list:

        if book.id == book_id:
            return True

    return False # return False if book id is not found


def make_changes(book, book_id):

    global book_list

    book.id = book_id
    delete_book(book_id) #delete the old record
    book_list.insert((book_id - 1),book) #update the record with .insert(puts it at this position, this is what you're inserting)


def make_book_list(json_string_from_file):
    ''' turn the string from the file into a list of Book objects'''

    global book_list

    books_str = json.loads(json_string_from_file)

    for data in books_str:
        book = Book(data["title"], data["author"], data["read"] == 'True', int(data["id"]))
        book_list.append(book)


def make_output_data():
    ''' create a json containing all data on books, for writing to output file'''

    global book_list

    output_data = []

    # example json data [{"title": book.title, "author": book.author, "read": book.read. "id": book.id}, ...]
    for book in book_list:
        output = {"title": book.title, "author": book.author, "read": str(book.read), "id": str(book.id)}
        output_data.append(output)

    all_books_string = json.dumps(output_data)

    return all_books_string
