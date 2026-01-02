## norm.ppf()
A `scipy` library function that calculates percentiles of the normal distribution. Arguments of the function include `q`, the lower tail probability, `loc` the mean, and `scale` the standard deviation of the normal distribution to generate.

```python
# percentiles needed for a 90% confidence interval
L0=norm.ppf(0.05, loc=0, scale=1/2)
U0=norm.ppf(0.95, loc=0, scale=1/2)
```

## np.percentile()
Takes in an `array` of a distribution and computes the `q` percentile of data. 

```python
np.percentile(array, q=97.5)
```