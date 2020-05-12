# Lesson 6: Exceptions and Reading/Writing files

# Reading and Writing to files

### Additional info
[here](https://realpython.com/read-write-files-python/)

### Files intro
Need to know about files from [here](https://realpython.com/read-write-files-python/)
1. What is a file
2. File paths  (/ or \\), (.), (..)
3. Line endings (\r\n)

### Opening a file & closing it
```python
reader = open('dog_breeds.txt')
try:
    # Further file processing goes here
finally:
    reader.close()
```

You need to remember to close it. Or alternatively use the with syntax

 ```python
 with open('dog_breeds.txt', 'r') as reader:
    # Further file processing goes here
```

The r parameter indicates reading. 3 most common
Parameter | Explanation
--- | ---
r | Reading (default)
w | Writing. overrides file first
a | Writing. appends to the end of the file

### Now file is open can read
Read entire file
```python
with open('myfile.txt', 'r') as reader:
    print(reader.read())
```

Read lines
```python
# line by line
with open('myfile.txt', 'r') as reader:
    print(reader.readline())
    print(reader.readline())
  
# all the lines
with open('myfile.txt', 'r') as reader:
    reader.readlines()

# readlines returns a list so can do this:
with open('myfile.txt', 'r') as reader:
    for line in reader.readlines():
        print(line, end='')
```
The print(line, end='') makes sure that print doesnt chuck an additional enter at the end of the line.
"test\n".rstrip() also removes it

### Writing to files
```python
.write(string)
.writelines(seq)
```

Need to convert objects to string. E.g.
```python
value = ('the answer', 42)
s = str(value)  # convert the tuple to string
f.write(s)
```

# Exceptions
### Handling Exceptions
Handles bad situations. In the examples with files, what if the file does not exist? 
Or the user gives us input that is a word when what we want is a number?

```python
try:
    file = open(arg, 'r')
    line = file.readline()
    no = int(line.strip())
except OSError:
    # What to do on named exception. Can have multiple except
    print('cannot open', arg)
except ValueError:
    print("Could not convert data to an integer.")
else:
    # code to be executed if no exception raised
    print(arg, 'has', len(file.readlines()), 'lines')
finally:
    # Clean up code. Gets executed whether exception or not. Remember we said we always had to close files:
    file.close()
```

### Raising an exception
You can manually raise an exception by using raise keyword
```python
raise ValueError('My own error')
```

### You can also create your own exceptions
It should derive from the exception class and when creating a module that can raise several distinct errors, a common practice is to create a base class for exceptions defined by that module, and subclass that to create specific exception classes for different error conditions:

```python
class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class DavidException(Error):
    """Davids Exception

    Attributes:
        message -- explanation of the error
    """

    def __init__(self,  message):
        self.message = message
```

HW: https://classroom.udacity.com/courses/ud1110  Lesson 6 Scripting (chpt 13 - 19
HW: Phonebook update to save to a file and load form a file
HW (optional) Add abilty to remove names
