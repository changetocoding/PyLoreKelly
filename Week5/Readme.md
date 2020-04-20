# Lesson 5: Objects

[Tutorial 1](https://www.hackerearth.com/practice/python/object-oriented-programming/classes-and-objects-i/tutorial/)
[Tutorial 2](https://pythonbasics.org/class/)

## Pycharm
We will start using pycharm. You should now be comfortable using a text editor and the python interpreter so we will start using and IDE (Intergrated development environment). This makes coding easier for us

## Class is an object. 
It lets us compose more complicated things. But also group together related things. E.g. a person has a name 
```python
class Person:
     name = "David"
     age = 29
     
david = Person()
print(david.name)
```

## Methods
Classes can have methods
```python
class Person:
     name = "David"
     age = 29
     
    def change_name(self, new_name): # note that the first argument is self
        self.name = new_name # access the class attribute with the self keyword     
     
     
david = Person()
print(david.name)
david.change_name("Fred")
print(david.name)
```

## Init method
Constructor in other languages. Allows you to initialise an object the way you want
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def change_name(self, new_name): # note that the first argument is self
        self.name = new_name # access the class attribute with the self keyword      
        
person1 = Person("David", 29)
person2 = Person("Fred", 22)

person3 = person1

# what happens if I do
person3.change_name("Paula")
print(person1)
print(person3)
```

## Naming conventions:
https://pep8.org/#naming-conventions

Class Names: Class names should normally use the CapWords convention.
> class ExcelWorkBook:

Method names & variables: lower_case_with_underscore
> def my_method:
> self.my_variable = 10

# Homework
## Coursebook:
Classes and objects:
- [Classes](https://www.learnpython.org/en/Classes_and_Objects)
Revision: 
- [Sets](https://www.learnpython.org/en/Sets), 
- [Dictionaries](https://www.learnpython.org/en/Dictionaries), 
- [Functions](https://www.learnpython.org/en/Functions)


## Project Phonebook:
The goal of this task is to create a phonebook application. 

The application takes 2 commands
- Add: the user can enter name and 11 digit numbers pairs. e.g 12345678901
- Query: the user can query the phone book using a name or a number: given an 11 digit number it returns the name of a person. Or given a name returns the number of the person. Return a useful error message if the person does not exist.

E.g. sample input/output

\>Command:  
Add David 02345678901  
\>Command:  
Add Tom 12345678900  
>Command:  
Query David  
>David's number is 02345678901  
>Command:  
Query 12345678900  
>Tom's number is 12345678900  
>Command:  


Constraints:
- You must define a class called PhoneBook and use it (Helpful hint this class should have 3 methods (add, query using a number, query using a name)
- You must store the phone number as a number (Use string formating to add leading 0's when outputting)
