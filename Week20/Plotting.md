# Things should know by now
- Load data into pandas and numpy
- Manipulate data using pandas & numpy
- Clean data using numpy (https://realpython.com/pandas-python-explore-dataset/#cleaning-data)


# Plotting
First off we need to import the plotting library
```python
%matplotlib
```
Or "%matplotlib inline" because it displays the plot in the Jupyter Notebooks itself, immediately below the cell that creates the plot:
```python
%matplotlib
```

The data we are working with

```python
import pandas as pd
download_url = (
    "https://raw.githubusercontent.com/fivethirtyeight/"
    "data/master/college-majors/recent-grads.csv"
)
df = pd.read_csv(download_url)
type(df)
```python

### Plotting median and percentiles
```python
df.plot(x="Rank", y=["P25th", "Median", "P75th"])
```
Note if not in jupyter noteback need to do this instead:
```python
import matplotlib.pyplot as plt
df.plot(x="Rank", y=["P25th", "Median", "P75th"])
plt.show()
```

## Different kind of plots
Can either pass a parameter to the kind argument or use one of below methods
```python
    .area()
    .bar()
    .barh()
    .box()
    .hexbin()
    .hist()
    .kde()
    .density()
    .line()
    .pie()
    .scatter()
```

## Plot a series as a histogram.
```python
median_column = df["Median"]
type(median_column)  # pandas.core.series.Series
# median_column.plot(kind="hist")
```

This is also very useful for identifying outlies

### Investigate outlier:
We'll sort and then plot top 5
```python
top_5 = df.sort_values(by="Median", ascending=False).head()
top_5.plot(x="Major", y="Median", kind="bar", rot=5, fontsize=4)
```

Can investigate a bit futher by for example ploting only those with a median salary of more than $60k
```python
top_medians = df[df["Median"] > 60000].sort_values("Median")
top_medians.plot(x="Major", y=["P25th", "Median", "P75th"], kind="bar")
```

Outliers interesting as can point out invalid data

## Check for Correlation = scatter plot
```python
df.plot(x="Median", y="Unemployment_rate", kind="scatter")
```

For an overview of the correlations between different columns, you can use ".corr()"

## Analysing caterogies/groupings
To process bigger chunks of information, the human mind consciously and unconsciously sorts data into categories. This technique is often useful, but it’s far from flawless.

In this case lets draw a horizontal bar to represent totals
```python
cat_totals = df.groupby("Major_category")["Total"].sum().sort_values()
cat_totals
cat_totals.plot(kind="barh", fontsize=4)
```

## Pie chart
Here we draw a pie chart from that data. But even better we group together the smaller categories
```python
small_cat_totals = cat_totals[cat_totals < 100_000]
big_cat_totals = cat_totals[cat_totals > 100_000]

# Adding a new item "Other" with the sum of the small categories
small_sums = pd.Series([small_cat_totals.sum()], index=["Other"])
big_cat_totals = big_cat_totals.append(small_sums)
big_cat_totals.plot(kind="pie", label="")
```

# Homework:
Follow this tutorial:
Do this mini course on plotting: https://realpython.com/courses/python-histograms/  
Pick one of the datasets have been working with and create some plots for it 
(optional) https://realpython.com/pandas-project-gradebook/

# Next week we will cover the GG library
https://classroom.udacity.com/courses/ud359/lessons/692548568/concepts/6785689500923



# Further reading:
https://realpython.com/learning-paths/data-visualization-python/
https://realpython.com/pandas-plot-python/
