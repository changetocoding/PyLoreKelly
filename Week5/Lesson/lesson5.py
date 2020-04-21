class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def change_name(self, new_name): # note that the first argument is self
        self.name = new_name # access the class attribute with the self keyword


class House:
    flowers = 0

    def __init__(self, postcode):
        self.postcode = postcode

    def add_flowers(self):
        self.flowers = self.flowers + 1


class PhoneBook:
    def add_user(self, name, number):
        # do something
        self.name = name

    def query_name(self, name):
        #...
        return ''


    def query_number(self, no):
        #...
        return ''



#person1 _> Peson('d', 29)
#person3


person1 = Person('David', 29)
person2 = Person('Lore', 28)

person3 = person1
person1.name = 'Tom'

davids_key = House('E1')
lores_key = davids_key
davids_key.add_flowers()


davids_key = House('E2')
lores_key.add_flowers()

print(davids_key.flowers)
