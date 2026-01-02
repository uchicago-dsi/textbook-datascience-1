## Series.isin()
Checks whether each element in a Series is contained in a given list, set, or other sequence.  
Returns a Boolean Series with `True` for elements that are present and `False` otherwise.   

```python
import pandas as pd
s = pd.Series([1, 2, 3, 4, 5])
s.isin([2, 4, 6])
```

## Series.str.lower()
Converts all string values in a Series to lowercase.  
This method works element-wise across the entire Series without needing `.apply()`.  

```python
s = pd.Series(["Apple", "BANANA", "Cherry"])
s.str.lower()
```