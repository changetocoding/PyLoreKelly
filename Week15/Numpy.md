# Starting off

# Course structure:
Week 15: Setup env, loading data & cleaning data
Week 16 & 17: Investigating the data (might only spend 1 week on this depending on how you get on)


### Anaconda
Think of it as a version of python with all the stuff you need for data science
Dependencies/requirements are the libaries that your python script will use. This is code that someone else has written that performs a useful function for your script without you having to write it

### jupyter notebook
Remember it is below to start the jupyter server
```
jupyter notebook
```

Check everyone is setup and got the notebooks working


# Homework
https://classroom.udacity.com/courses/ud170/lessons/

Upto and including chpt 13:
This will get your environment setup (last weeks homework) and cover loading the data and cleaning the data

### loading data CSVs
The course uses CSV library. This is very similar to what we did for the file reading but better for reading CSVs

They cover how to use it in the HW. Can go through it in class if struggling with it
```python
>>> import unicodecsv
>>> with open('names.csv') as csvfile:
...     reader = csv.DictReader(csvfile)
...     for row in reader:
...         print(row['first_name'], row['last_name'])
...
Baked Beans
Lovely Spam
Wonderful Spam
```
unicode is just a text encoding system (the best one as it supports other languages instead of just american english)

### Cleaning data
have to clean data: Similar to budget tracker I had all those deposits, had to clean them out. 

The homework covers cleaning the data and removing rows that don't need

### Finally we will be doing it as a jupiter notebook
Because the course does it that way, but it is also very useful as it is a good way to present your analysis in a runable format
