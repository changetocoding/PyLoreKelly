# Classes Round 2

## Create Your Own dictionary

```python

str = 'abab'
ord(str[0])

```



## Homework

### Recreate the dictionary class with some changes
1. Add a remove method to remove the value for a given key


### Create your own string builder class

String builder allows you to compose strings on the fly. It tends to be useful when we compose strings from partial information
e.g. we get users telep


This is example code for how another developer using your code should be able to use it:

```python
# 1. They should be able to create an instance of it
str = YourStringBuilder()

# 2. They should be able to create it with a string
str = YourStringBuilder('Test')

# 3. They can add a string to it
str.add('ing')
str.add(' is about')
str.add(' making sure your script works.')

# 4. They should be able to display it
other = str.to_string()
print(other) # prints "Testing is about making sure your script works.". it was constructed with 'Test' in part 2, 'ing' ' is about' '  making sure your script works.' were added in part 3

# 5. They should be able to remove the last added string
str.remove()
str.remove()
other = str.to_string()
print(other) # prints "Testing"

```
