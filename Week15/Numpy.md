# Starting off

# Course structure:
- Week 15 (today): Setup env, loading data & cleaning data
- Week 16 & 17: Investigating the data (might only spend 1 week on this depending on how you get on)
- Week 18: Numpy  
Then break for a week  
- Week 19+: pandas :panda_face:


### Anaconda
Think of it as a version of python with all the stuff you need for data science
Dependencies/requirements are the libaries that your python script will use. This is code that someone else has written that performs a useful function for your script without you having to write it

Check can run anaconda in pycharm

https://www.jetbrains.com/help/pycharm/conda-support-creating-conda-virtual-environment.html


### Jupyter notebooks
Remember it is below to start the jupyter server
https://www.codecademy.com/articles/how-to-use-jupyter-notebooks

1. Open your terminal 
2. Navigate to the directory where you would like to save your notebook. For me it was:
```
cd C:\Dev\Teaching\Pupils\PyLoreKelly\Week15\Homework\david
```
3. Then type the command jupyter notebook
```
jupyter notebook
```

**Excerise In class**: Check everyone is setup and got the notebooks working


# Homework
https://classroom.udacity.com/courses/ud170/

Upto and including chpt 15:
This will get your environment setup (last weeks homework) and cover loading the data and cleaning the data

### Getting started:
1. Download all the csv and the jupyter notebook from the resources section on the right menu bar in the udacity course into a folder in the git repository
2. Follow steps in "Jupyter notebooks" section to open the jupyter notebooks in that folder


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

with open('test.csv', 'rb') as csv_file:
    # open('test.csv') did not work for me, had to do above (include the 'b'). See https://github.com/jdunck/python-unicodecsv/issues/79
    csv_reader = unicodecsv.reader(csv_file, delimiter=',')
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
>>> with open('test.csv', 'rb') as csvfile:
...     reader = unicodecsv.DictReader(csvfile)
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

