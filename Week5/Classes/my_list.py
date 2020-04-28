class MyList:
    def __init__(self):
        self.items = []

    def append(self, item):
        self.items.append(item)

    def remove_odd(self):
        temp = self.items
        self.items = []
        for item in temp:
            if item % 2 == 1:
                self.items.append(item)
