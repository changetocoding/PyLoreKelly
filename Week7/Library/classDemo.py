"""
Library


Can search for a librarian - Demo searching list
Can list all books - Demo tuple spread operator
Can borrow book - Demo check if in dict. Also how to update dict entry values (update stock in this case)
Can search for book by author or name - Similar to have to make a decision based off parameter. Use 2 dict



1. Dictionary 1 directional: How to get in other direction?
2. if hiding
3. Overriding variables
4. Scope
5. How to detect if dont find in dict
6. How to detect if dont find in list
7. Demo make into methods
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


# Best way to check if item is in a list
def check_librarian(name):
    if name in librarians:
        print('{} is a librarian'.format(name))
    else:
        print('Librarian not found')

# other way to check if item in list but not recommended as above is so much
def check_librarian_for():
    amedu = 'Peter Parker'
    found = False
    for librarian in librarians:
        clean_param = amedu.lower()
        if librarian.lower() == clean_param:
            found = True

    print(found)


while(True):
    user_input = input('What do you want to do in this format [Command Parameter]:\n')
    command_params = user_input.split(' ', 1) # Using max split parameter here so only get two items
    command = command_params[0]
    param = command_params[1]

    if command == 'lib':
        check_librarian(param)
    elif command == 'lib2':
        check_librarian_for()

check_librarian_for()

