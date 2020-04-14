Week 3 homework review

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
{
   return IsHuman(alien.Father) && IsHuman(alien.Mother)
}

```
So now I'm like is John a human?
Well to know that I need to know if Johns parents are human. To know that I need to know if thier parents (john's grandparents) are human.

Limit of recursion. Python stops the function calls after a depth of 1000 calls.

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

Solve it using 2 different ways:
1. For or while loop
2. Recursion

### Additional HW (Lore): 
1. Prepare and give a 2 minute presentation on source control.
2. Create a git reposition online (github or bitbucket) and commit the code you wrote yesterday to it.

### Optional HW:
(If doing this let me know how easy it was. Think might be too indepth for beginners)
additional more in depth about functions: https://realpython.com/defining-your-own-python-function/  
Additional more in depth about lamdas https://realpython.com/python-lambda/  




