#Main program

import ui, datastore
from book import Book


def handle_choice(choice):

    if choice == '1':
        show_unread()

    elif choice == '2':
        show_read()

    elif choice == '3':
        book_read()

    elif choice == '4':
        new_book()

    elif choice == '5': #to delete book from wishlist (JEN)
        delete_unread()

    elif choice == '6': #to edit title/author (JEN)
        edit_book() #TODO make this happen

    elif choice == 'q':
        quit()

    else:
        ui.message('Please enter a valid selection')



def show_unread():
    '''Fetch and show all unread books'''
    unread = datastore.get_books(read=False)
    ui.show_list(unread)


def show_read():
    '''Fetch and show all read books'''
    read = datastore.get_books(read=True)
    ui.show_list(read)


def book_read():
    ''' Get choice from user, edit datastore, display success/error'''
    book_id = ui.ask_for_book_id()
    if datastore.set_read(book_id, True):
        ui.message('Successfully updated')
    else:
        ui.message('Book id not found in database')


def new_book():
    '''Get info from user, add new book'''
    new_book = ui.get_new_book_info()
    datastore.add_book(new_book)
    ui.message('Book added: ' + str(new_book))


def delete_unread(): #(JEN)
    '''Get choice from user, edit datastore, display success/error'''
    book_id = ui.ask_for_book_id()

    if datastore.set_delete(book_id,True):
        ui.message('Successfully removed book')
        datastore.delete_book(book_id)

    else:
        ui.message('Book id not found in database')


def edit_book(): #(JEN)
    '''Get choice from user, edit datastore, display success/error'''
    book_id = ui.ask_for_book_id()

    if datastore.edit_book(book_id,True):
        new_book = ui.get_new_book_info()
        datastore.make_changes(new_book,book_id)
        ui.message('Successfully updated')
    else:
        ui.message('Book id not found in database')

def quit():
    '''Perform shutdown tasks'''
    datastore.shutdown()
    ui.message('Bye!')


def main():

    datastore.setup()

    quit = 'q'
    choice = None

    while choice != quit:
        choice = ui.display_menu_get_choice()
        handle_choice(choice)


if __name__ == '__main__':
    main()
