from my_list import MyList


numbers = MyList()
numbers.append(3)
numbers.append(3)
numbers.append(5)
numbers.append(7)
numbers.append(8)
numbers.append(3)

even_nos = MyList()
even_nos.append(10)

numbers.remove_odd();

# [3, 3, 5, 7, 8, 3]
print(numbers.items)
# [10]
print(even_nos.items)