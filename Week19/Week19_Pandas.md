Evolution to Pandas

### List:
1D data structure
![visual List representation](https://files.realpython.com/media/t.eb0b38e642c5.png)

### Numpy 
2d data structure

| col 4 is       | right-aligned           |  $122  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

### Pandas
Table like structure used to. With headers and row labels

![visual pandas data structure](https://pandas.pydata.org/docs/_images/01_table_dataframe.svg)



# Numpys
https://sites.engineering.ucsb.edu/~shell/che210d/numpy.pdf

### Create 2d array
```python
a = np.array([[1, 2, 3], [4, 5, 6]], float)
```

### Indexing
Select elements
```python
a[0,0] # 1.0
a[0,1] # 2.0
```

### Array slicing
":" indicates everything along that dimension
```python
a[1,:]
a[:,2]
```

### Shape & type 
Shape is the array dimensions
```python
a.shape # (2, 3)
a.dtype # dtype('float64')
```

Can be reshaped - Changes it to a new dimensions. The transpose command will swap the x and y axis around
```python
a = np.array(range(10), float) # array([ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9.])
a.reshape((5, 2))
# array([[ 0.,  1.],
#       [ 2.,  3.],
#       [ 4.,  5.],
#       [ 6.,  7.],
#       [ 8.,  9.]])

a.transpose()
```

### Joining np arrays
```
a = np.array([[1, 2], [3, 4]], float)
b = np.array([[5, 6], [7,8]], float)
np.concatenate((a,b))
# array([[ 1.,  2.],
#        [ 3.,  4.],
#        [ 5.,  6.],
#        [ 7.,  8.]])

np.concatenate((a,b), axis=0)
# array([[ 1.,  2.],
#        [ 3.,  4.],
#        [ 5.,  6.],
#        [ 7.,  8.]])

np.concatenate((a,b), axis=1)
# array([[ 1.,  2.,  5.,  6.],
#        [ 3.,  4.,  7.,  8.]])
```

### Creating with zeros and ones
Creates an array with the spec you want filled with either zeros or ones. We also have the identity matrix
```python
np.ones((2,3), dtype=float)
np.zeros(7, dtype=int)
np.identity(4, dtype=float)
# identity matrix:
# array([[ 1.,  0.,  0.,  0.],
#        [ 0.,  1.,  0.,  0.],
#        [ 0.,  0.,  1.,  0.],
#        [ 0.,  0.,  0.,  1.]])
```


### Array mathematics
```python
a = np.array([[1,2], [3,4]], float)
b = np.array([[2,0], [1,3]], float)
a + b 
a * b # element wise. See below
# array([[2., 0.], [3., 12.]]
```

| Result|      |
| ----  |:-----: | 
| 1 * 2 |  2 * 0 |
| 3 * 1 |  4 * 3 |


For matrix multiplication do: np.dot(b,a)

### Mean, median
```python
np.median(a)
np.mean(a)
```


# Pandas


## Summary Statistics
Covered row/column selection in last lesson
```python
titanic["Age"].mean()
titanic[["Age", "Fare"]].median()
```

Describe give a list of stats: Count, mean, standard deviation, min, max ....
```python
titanic[["Age", "Fare"]].describe()
```

We can also group first before taking stats (from the hw).

Aka: What is the average age for male versus female Titanic passengers?
```python
titanic[["Sex", "Age"]].groupby("Sex").mean()

# or just for age:
titanic.groupby("Sex")["Age"].mean()
```

You can also group by multiple categories
Aka: What is the mean ticket fare price for each of the sex and cabin class combinations?
```python
titanic.groupby(["Sex", "Pclass"])["Fare"].mean()
```

Finally value counts:
```python
titanic["Pclass"].value_counts()
```


# Next week we are going to start predicting the future:
# Linear regression:
![Linear Regression](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Linear_regression.svg/2880px-Linear_regression.svg.png)
