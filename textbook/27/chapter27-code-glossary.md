## pd.to_datetime()
A method used to convert dates to special datetime objects in Python. The function can also be used to specify the `format` of dates and time stamps.
```
pd.to_datetime('2026-01-01 12:00:00',
               format='%Y-%m-%d %H:%M:%S%f')
```

## pd.date_range(start=None, end=None, periods=None)
A method which takes in the primary arguments `start`, `end`, and `periods` to create a series of dates. In the example below, a series of consecutive daily dates will be generated starting from 2000-07-01 to 2000-07-06:
```
pd.date_range(`start='2000-07-01',
                end='2000-07-06',
                freq='D')
```

## str.split()
A method used to split a string by a character or pattern of characters.
```
telephone_number = '123-456-7890'
telephone_number.split('-')
```