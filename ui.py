from book import Book


def display_menu_get_choice():

    '''Display choices for user, return users' selection'''

    print('''
        1. Show unread books (wishlist)
        2. Show books that have been read
        3. Mark a book as read
        4. Add book to wishlist
        5. Delete book from wishlist
        6. Edit Book Title/Author
        q. Quit
    ''')

    choice = input('Enter your selection: ')

    return choice


def show_list(books):
    ''' Format and display a list of book objects'''



    if len(books) == 0:
        print ('* No books *')
        return

    books.sort(key = lambda book: book.author) #this sorts the books by author before printing

    for book in books:
        print(book)


    print('* {} book(s) *'.format(len(books)))

    #failed attempts at sorting
    #books.sort(key = book.author)
    #print(sorted(books, key = lambda book: book.author))


def ask_for_book_id():

    ''' Ask user for book id, validate to ensure it is a positive integer '''

    while True:
        try:
            id = int(input('Enter book id:'))
            if id >= 0:
                return id
            else:
                print('Please enter a positive number ')
        except ValueError:
            print('Please enter an integer number')


def get_new_book_info():

    ''' Get title and author of new book from user '''

    title = input('Enter title: ')
    author = input('Enter author: ')
    return Book(title, author)


def message(msg):
    '''Display a message to the user'''
    print(msg)
