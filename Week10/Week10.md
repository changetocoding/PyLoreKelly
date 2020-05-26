# Modules, importing libaries and revision of objects
Modules. We will cover modules and importing other python files.  
We will then cover external libaries and how to import them. Creating a webserver with bottle will be used as a demonstration
[Offical Docs](https://docs.python.org/3/tutorial/modules.html

# Modules

### Local scripts
To import a script use this.
```python
import foo
```
You can now use the functions in foo.py like
```python
foo.doSomething
```

Demo in class

### The module gets executed when imported
But only once
```python
# foo.py
print('hello world')
```
```python
# main.py
import foo

print('hello world already printed...')
```
Can use this to initialise variables in the module that you want to be singleton (only initialised once).  

But for most part don't have code that executes in your imported module: just functions and classes that can be called (no nasty side effects from importing)


### from ... import ...
There is another way which means you don't have to do the foo.functionName(). But this is bad as it imports all the names from the module into your scope.

Very bad
```python
from modu import *
[...]
x = sqrt(4)  # Is sqrt part of modu? A builtin? Defined above?
```

Better but still bad
```python
from modu import sqrt
[...]
x = sqrt(4)  # sqrt may be part of modu, if not redefined in between
```

Best
```python
import modu
[...]
x = modu.sqrt(4)  # sqrt is visibly part of modu's namespace
```

### Module names Names:
1. Keep short
2. No dots. Avoid _ . Dots are treated like folders so "library.plugin.foo" means it it will look for foo.py in /library/plugin.


### Packages:
Any directory with an __init__.py file is considered a Python package

A file modu.py in the directory pack/ is imported with the statement import pack.modu. This statement will look for an __init__.py file in pack and execute all of its top-level statements. Then it will look for a file named pack/modu.py and execute all of its top-level statements. After these operations, any variable, function, or class defined in modu.py is available in the pack.modu namespace.

# External scripts
pip install
bottle
https://bottlepy.org/docs/dev/

Anaconda.

# HW
HW: https://classroom.udacity.com/courses/ud1110 - Lesson 6 Scripting (Sections 22 till end)  
HW: [Modules](https://www.learnpython.org/en/Modules_and_Packages)  
