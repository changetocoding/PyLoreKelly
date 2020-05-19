# Objects II: Grouping together things
# phonebook
# multiple list
# Class
# Dictionary


# 1 Grouping together logic: Class handles mouse input, keyboard input
# 2. Grouping related data
# 3. Composition small classes doing small things make a big application just like a house



# What if want to add more details like postcode, surname, email address





class PhonebookEntry:
    def __init__(self, name, no, postcode, address_line):
        self.name = name
        self.no = no
        self.postcode = postcode
        self.address_line = address_line

    def get_address(self):
        return self.address_line + '\n' + self.postcode

entry1 = PhonebookEntry('paul',8888,'SE1', '1 Wood st' )
entry2 = PhonebookEntry('james',999,'E1', '20 fox road' )


class Dict:

    def __init__(self, dict):
        self.elements = []
        for i in range (20):
            self.elements.append(None)

    def add(self, key, value):
        key_as_no = ord(key[-1])
        index = key_as_no % len(self.elements)

        if(self.elements[index] == None):
            self.elements[index] = []

        self.elements[index].append((key, value))


    def get(self, key):
        key_as_no = ord(key[-1])
        index = key_as_no % len(self.elements)
        items = self.elements[index];
        if(len(items) == 0):
            return None
        if(len(items) == 1):
            return items[0][1]

        for dict_key, value in items:
            if(dict_key == key):
                return item

        return None


my_dict = Dict()
my_dict.add('james', 9999)
my_dict.add('paul', 1111)
my_dict.add('michelle', 4444)
my_dict.add('peter', 4444)

print(my_dict.get('james')) # 9999