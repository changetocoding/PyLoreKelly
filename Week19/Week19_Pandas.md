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


# Array mathematics
```python
a = np.array([[1,2], [3,4]], float)
b = np.array([[2,0], [1,3]], float)
a + b 
a * b # element wise. See below
# array([[2., 0.], [3., 12.]]
```

| array 1 |      |
| ----  |:-----: | 
| 1 * 2 |  2 * 0 |
| 3 * 1 |  4 * 3 |




