class Dict:

    def __init__(self):
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