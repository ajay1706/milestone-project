"""
Concerned with Storing & retrieving books from a list.
 """

books = []

def add_book(name,author):
    books.append({'name':name,
                  'author':author,
                  'read':False})