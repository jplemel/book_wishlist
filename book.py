class Book:

    ''' Represents one book in a user's list of books'''

    NO_ID = -1

    def __init__(self, title, author, read=False, read_date=None, id=NO_ID):
        '''Default book is unread, has no read_date, and has no ID'''
        self.title = title
        self.author = author
        self.read = read
        self.read_date = read_date
        self.id=id


    def set_id(self, id):
        self.id = id

    def __repr__(self): #JEN

        if not self.read:
            return repr(self.id, self.title, self.author, self.read)
        else:
            return repr(self.id, self.title, self.author, self.read, self.read_date)


    def __str__(self):
        read_str = 'no'
        if self.read:
            read_str = 'yes'

        id_str = self.id
        if id == -1:
            id_str = '(no id)'

        if self.read:
            template = 'id: {} Title: {} Author: {} Read: {}, Read Date: {}'
            return template.format(id_str, self.title, self.author, read_str, self.read_date)
        else:
            template = 'id: {} Title: {} Author: {} Read: {}'
            return template.format(id_str, self.title, self.author, read_str)


    def __eq__(self, other):
        return self.title == other.title and self.author == other.author and self.read == other.read and self.id==other.id and self.read_date == other.read_date
