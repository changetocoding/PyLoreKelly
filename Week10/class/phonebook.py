def load_data():
    # Reads from file
    print('loaded')


class PhoneBook:

    def __init__(self):
        self.dict = {};

    def add(self, name, no):
        self.dict[name] = no

    def query(self, name):
        return self.dict[name]

# Load data
load_data()

phone_book = PhoneBook()

