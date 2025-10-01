## matplotlib
A popular Python library for creating static, animated, and interactive visualizations.  
[Documentation](https://matplotlib.org/stable/index.html)

## matplotlib.pyplot
A submodule of matplotlib that provides a MATLAB-like interface for plotting.  
Usually imported as:
```python
import matplotlib.pyplot as plt
```
[Documentation](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html)

## seaborn
A statistical visualization library built on top of matplotlib.  
It provides high-level plotting functions that make complex plots easier to create.  
```python
import seaborn as sns
sns.scatterplot(x="col1", y="col2", data=df)
```
[Documentation](https://seaborn.pydata.org/)

## plt.scatter()
Creates a scatter plot of two variables.  
```python
plt.scatter([1,2,3], [4,5,6])
plt.show()
```
[Docs](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html)

## plt.plot()
Creates a line plot.  
```python
plt.plot([0,1,2], [0,1,4])
plt.show()
```
[Docs](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html)

## df.plot()
A pandas method for quick plots using matplotlib underneath.  
```python
df["column"].plot(kind="line")
```
[Docs](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html)

## plt.hist()
Creates a histogram to show a variable’s distribution.  
```python
plt.hist([1,1,2,3,3,3,4])
plt.show()
```
[Docs](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html)

## plt.bar()
Creates a vertical bar chart.  
```python
plt.bar(["A","B","C"], [3,5,2])
plt.show()
```
[Docs](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html)

## plt.show()
Displays all active plots.  
[Docs](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html)

## plt.title()
Adds a title to a plot.  
[Docs](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html)

## plt.xlabel() / plt.ylabel()
Add axis labels.  
[Docs](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html)

## plt.figure()
Creates a new plotting figure.  
[Docs](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html)

## plt.colorbar()
Adds a color scale bar to a plot.  
[Docs](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.colorbar.html)

## plt.xticks()
Sets tick positions or labels on the x-axis.  
[Docs](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html)

## plt.subplots()
Creates a figure with one or more subplots, returning (fig, ax).  
[Docs](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html)

## fig.suptitle()
Adds a title to the entire figure (all subplots).  
[Docs](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.Figure.suptitle)

## ax.set_title() / ax.set_xlabel() / ax.set_ylabel()
Set labels and titles for a specific subplot.  
[Docs](https://matplotlib.org/stable/api/axes_api.html)

## ax.set_ylim() / ax.set_xticks()
Control y-axis range and x-axis tick marks for a subplot.  
[Docs](https://matplotlib.org/stable/api/axes_api.html)

## df.hist()
A pandas method for quick histograms.  
[Docs](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.hist.html)

## ax.bar()
Bar plot for a specific subplot (axis object).  
[Docs](https://matplotlib.org/stable/api/axes_api.html#matplotlib.axes.Axes.bar)

## ax.bar_label()
Add numeric labels to bars in a bar chart.  
[Docs](https://matplotlib.org/stable/api/axes_api.html#matplotlib.axes.Axes.bar_label)

## df.transpose()
Swaps rows and columns of a DataFrame.  
[Docs](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.transpose.html)

## plt.barh()
Creates a horizontal bar chart.  
[Docs](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.barh.html)

## bar.set_color()
Change the color of a bar object.  
[Docs](https://matplotlib.org/stable/api/artist_api.html)

## plt.pie()
Creates a pie chart.  
[Docs](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pie.html)

## plt.legend()
Adds a legend to a plot.  
[Docs](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html)

## plt.boxplot() / df.plot.box()
Box-and-whisker plots for distributions.  
[Docs](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.boxplot.html)

## plt.stackplot()
Stacked area plot.  
[Docs](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.stackplot.html)

## plt.margins()
Adjusts plot margins/padding.  
[Docs](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.margins.html)

## plt.tight_layout()
Automatically adjusts subplot spacing to prevent overlap.  
[Docs](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html)

