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

### Loading data CSVs
The course uses CSV library. This is very similar to what we did for the file reading but better for reading CSVs

They cover how to use it in the HW. Can go through it in class if struggling with it

A Csv looks like this, You've already come across it in the budget excerise. In this case have a header row
```csv
name,department,birthday month
John Smith,Accounting,November
Erica Meyers,IT,March
```
Can be saved as a .csv or a .txt file

```python
import unicodecsv

with open('employee_birthday.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
          # This is the first row and header rwo
          print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print('---')
            print('name: ' + row[0])
            print('department: ' + row[1])
            print('birthday: ' + row[2])
            line_count += 1
    print(f'Processed {line_count} lines.')
    
```
delimiter specifiers the character that the columns break on. The default is ','

Can directly read into a dictionary so can access using the header
```python
>>> import unicodecsv
>>> with open('employee_birthday.csv') as csvfile:
...     reader = csv.DictReader(csvfile)
...     for row in reader:
...         print(row['name'], row['department'])
...
Baked Beans
Lovely Spam
Wonderful Spam
```

unicode is just a text encoding system (the best one as it supports other languages instead of just american english)

[Additional reading if stuck on csv](https://realpython.com/python-csv/)

Panadas which we will use later for data manipulation also has it's own way of reading csv's. Will cover that later

### Cleaning data
You have to clean data: Similar to budget tracker I had all those deposits (which were not expenses), You had to remove them. 

The homework covers cleaning the data and removing rows that don't need

### Finally we will be doing it as a jupiter notebook
Because the course does it that way, but it is also very useful as it is a good way to present your analysis in a runable format
