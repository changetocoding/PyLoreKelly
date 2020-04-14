# Homework review

-Structure of homework will be chapter from coursebook and an assignment that puts into practise what know so far
-Also sometimes don't immediately understand why works in example: Field those questions in first 30 mins of class
- Went through chaptr 4.14 in homework: What 2 different ways of doing it.
- Went through dictionary.items() is a tuple

# Git
Git and other source control tools provide an important function letting developers share code, backs up code and keeps track of changes made to code.

Kelly show lore how to set it up. 

Course git repo: https://github.com/changetocoding/PyLoreKelly


### 1. Install Git
Install https://desktop.github.com/ because it installs Git in the most consistent way across. We won't use the UI for it, Just the command line and we'll use pycharm for the ui bits (We'll cover that later)


Alternatively can install just git itself from the offical site.  
Install From: https://git-scm.com/  
In the install options: Text editor: Vim or notepad++ (if picking vim most important thing to know is :wq to save and quit it)  https://stackoverflow.com/questions/11828270/how-do-i-exit-the-vim-editor  
And chose the option for use git from commandline. For the rest doesnt matter  
![textEditor](./img/textEditor.png)  
![CommandLine](./img/CommandLine.png)  


### 2. Install and follow interactive tutorial tool
Download the tutorial tool from here: https://github.com/jlord/git-it-electron/releases  
Unzip it then click on the exe.  
Follow the tutorial.  

An additional tutorial is: https://product.hubspot.com/blog/git-and-github-tutorial-for-beginners  


# Functions

Functions group together logic & code. Scope of variables only within function too.
```python
def increment_by_one(count):
	new_count = count + 1
	return new_count
```

What do you think happens in this scenario
```python
p = 20

def increment_by_one(count):
	count = count + 10
	return count
	
b = inc(p)

# What do you think value of b is?
# What do you think value of p is?

```

### Examples from class
```python
def change_to_user(names):
	temp = []
	for name in names:
		temp.append(name.lower().replace(" ", "_"))
	return temp


def change_to_user_mod(names):
	for i in range(len(names)):
		names[i] = names[i].lower().replace(" ", "_")
    return names
```

# Recursion
This is when a function calls itself.

```python
# Summing numbers recursively

def sum(list):
    if len(list) == 1:
        return list[0]
    else:
        return list[0] + sum(list[1:])

print(sum([5,7,3,8,10]))

```

  
Recursion happens a lot languages. An example:
> Every human's mother and father is a human.

So lets rewrite it as a function:

IsHuman(person) = IsHuman(person.Father) && IsHuman(person.Mother)

So would look like
```python
def IsHuman(alien): 
   return IsHuman(alien.father) && IsHuman(alien.mother)
```
So now I'm like is John a human?
Well to know that I need to know if Johns parents are human. To know that I need to know if thier parents (john's grandparents) are human.

Limit of recursion. Python stops the function calls after a depth of 1000 calls.

In class example
```python
def sum_it(no):
    print("Summing: %d" % no)
	new_no = no + 5
	if (new_no > 100):
		return 100
	else:
		sum_recursive = sum_it(new_no)
		print("Recursive_sum is : %d" % sum_recursive)
		return no + sum_recursive
		
sum_it(0)
```
# Lamadas:
Shorthand for writing a function


# Homework


## Course book
HW: https://classroom.udacity.com/courses/ud1110 Lesson 5 (Control Flow, Functions). Control flow is revision of lesson 1  
(Functions, variable scope, default arguments, lamda functions)

### Fibonacci numbers

Fibonacci numbers are a sequence that is got by adding the previous two numbers.

The sequence looks like this: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34  
https://www.mathsisfun.com/numbers/fibonacci-sequence.html

There are several ways to solve this.

Solve it using 3 different ways:
1. For loop
2. While loop
3. Recursion

Expecting 3 different .py files, one for each method. Code should look something like this inside it:
```python
# The index we want to find the Fibonacci number at
fib_index = 18
# the name/variable to store the Fibonacci number at that index
fib_no_at_index = 0

# Your logic work out what value of fib_no_at_index should be
...

# print fib_no_at_index using string formating
...
```



### Additional HW (Lore, Amedu): 
1. Prepare and give a 2 minute presentation on source control.
2. Create a git reposition online (github or bitbucket) and commit the code you wrote yesterday to it.

### Optional HW:
(If doing this let me know how easy it was. Think might be too indepth for beginners)
additional more in depth about functions: https://realpython.com/defining-your-own-python-function/  
Additional more in depth about lamdas https://realpython.com/python-lambda/  




