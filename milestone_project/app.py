from utils import database

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

"""


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        pass



# def prompt_add_book() ask for author and book name
# def list_book() ask for books in our list
# def prompt_read_book() ask for book name and change it to "read" in list
# def prompt_list_book() ask for book name and remove book from list


