"""
Library


Can search for a librarian - Demo searching list
Can list all books - Demo tuple spread operator
Can borrow book - Demo check if in dict. Also how to update dict entry values (update stock in this case)
Can search for book - Similar to have to make a decision based off parameter. Use 2 dict
Can search for author
Demo make into methods


1. Dictionary 1 directional: How to get in other direction?
2. if hiding
3. Overriding variables
4. Scope
5. How to detect if dont find in dict
6. How to detect if dont find in list
"""


librarians = ['Peter Parker' , 'James Jones']


author_dict = {
    'Mark, David': ['How to code in python', 'How to code in C#'],
    'Peeters, Lore': ['Finance 101', 'Home baking in quarantine'],
    'Mark, Amedu': ['The end of the world', '#Instalife', 'Around the world'],
    'Le, Kelly' : ['Catan'],
    }

books_dict = {
    'How to code in python' : 1,
    'How to code in C#': 3,
    'Finance 101' : 7,
    'Home baking in quarantine' : 1,
    'The end of the world': 3,
    '#Instalife':1,
    'Around the world': 2,
    'Catan': 1,
    }


while(True):
    user_input = input('What do you want to do:\n')
    command_params = user_input.split(' ', 1) # Using max split parameter here so only get two items
    command = command_params[0]
    param = command_params[1]

    if command == 'lib':
        # Best way to check if item is in a list
        if param in librarians:
            print('{} is a librarian'.format(param))
        else:
            print('Unathorised')

    elif command == 'lib2':
        # other way to check if item in list but not recommended as above is so much simpler
        found = False
        for librarian in librarians:
            if librarian == param:
                found = True

        print(found)

    # have to do list all
    elif command == 'list':
        # has to be items. Doesnt work if just do "for author, books in author_dict"
        for author, books in author_dict.items():
            print('{} by {}'.format(books, author))

    elif command == 'borrow':
        # best way to check if something is a key in the dictionary
        if param in books_dict:
            stock = books_dict[param]
            if stock > 0:
                books_dict[param] == stock - 1
                print('borrowed {}'.format(param))
            else:
                print('{} is out of stock'.format(param))
        else:
            print('{} is not in the library'.format(param))

    elif command == 'search':
        if ',' in param:  # if , then we know its an author
            # Author search
            if author in author_dict:
                books = author_dict[param]
                print('The author has the following books: {}'.format(books))
            else:
                print('No  books by : {}'.format(books))
        else:
            # book search
            if param in books_dict:
                print("The book {} is in the library".format(param))
            else:
                print("The book {} is not found".format(param))
