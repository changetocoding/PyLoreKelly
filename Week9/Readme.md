# Classes Round 2

## Create Your Own dictionary

```python

str = 'abab'
ord(str[0])

```



## Homework
Recreate the dictionary class with some changes
1. Use len(string) instead for the hashing function  
2. Add a remove method  


Create your own string builder class
```python
# 1. You should be able to create it
str = YourStringBuilder()

# 2. You should be able to create it with a string
str = YourStringBuilder('Test')

# 3. You can add a string to it
str.add('ing')
str.add(' is about')
str.add(' making sure your script works.')

# 4. You should be able to display it
other = str.to_string()
print(other) # prints "Testing is about making sure your script works."

# 5. You should be able to remove the last added string
str.remove()
str.remove()
other = str.to_string()
print(other) # prints "Testing"

```
