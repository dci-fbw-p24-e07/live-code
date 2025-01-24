# Dates in Python

## 23.01.25

- What is a date and datetime?
- How to represent a date
- The datetime module
- How to format a date and time in different formats
- Timestamps

### What is a date and datetime?

- `date` is an object used to represent the calendar date wit no time of day.
- `datetime` includes the time of day down to the microsecond
- We use the `date` and `datetime` classes of the `datetime` module to handle any dates. 
- The `datetime` module is part of the Python installation

    **The ISO8601 datetime format:**
    1. The ISO8601 format specifies datetimes from the largest to the smallest unit of time ***`(YYYY-MM-DD HH:MM:SS TZ)`*** TZ representing TimeZone.

    2. Advantages of the ISO 8601 are:
        - It avoids confusion between `MM/DD/YYYY` and `DD/MM/YYYY` formats.
        - The 4 digit year representation mitigates overflow problems after the year 2099
        - Using numeric month values (08 not AUG) makes it language independent, so dates make sense throughout the world.
        - Python is optimized for this format since it makes comparison and sorting easier.

### Using the datetime module

> You can find the full documentation of the `datetime` module here: [https://docs.python.org/3/library/datetime.html](https://docs.python.org/3/library/datetime.html)

1. To import the full datetime module

    ```python
    import datetime
    ```

    **Use the date class:**

    ```python
    datetime.date()
    ```

    **Use the time class:**

    ```python
    datetime.time()
    ```

2. Import each class separately:

    1. Import the `date` class

        ```python
        from datetime import date
        ```

    2. Import the time class

        ```python
        from datetime import time
        ```

#### Representing a date in Python

- The date in Python is represented using the date class of the datetime module

    1. Import `date` from `datetime`:

        ```python
        from datetime import date
        ```

    2. Create the date object to represent a date

        ```python
        # Give a date in the format (YYYY, MM, DD)
        d = date(2026, 9, 14)
        ```

    **Get todays date:**

    - We use the `date.today()` function to get the current date.

    1. Import `date` from `datetime`:

        ```python
        from datetime import date
        ```

    2. Create an object to represent todays date

        ```python
        todays_date = date.today() # Result: 2025-01-23
        ```

    **Get the year, month and day:**
    - We can tap in to the `year`, `month` and `day` variables of the `today()` function.

    1. Import `date` from `datetime`:

        ```python
        from datetime import date
        ```

    2. Get the current date:

        ```python
        todays_date = date.today() # Result: 2025-01-23
        ```

    3. Extract the year, month, day:

        ```python
        print("Current year: ", todays_date.year)
        print("Current month: ", todays_date.month)
        print("Current day: ", todays_date.day)
        ```

#### Representing time in Python

- To represent a time object in Python we use the `time` class of the `datetime` module


    1. Import `time` from from datetime:

        ```python
        from datetime import time
        ```

    2. Create an object to represent the time

        ```python
        # Using the format(hour, minute, second, microsecond)
        a = time(11, 45, 35, 234566) # Result: 11:45:35.234566

        # Using the format(hour, minute, second)
        b = time(11, 45, 35) # Result: 11:45:35

        # Using the format(hour, minute)
        c = datetime.time(11, 45) # Result: 11:45:00
        ```

    > NOTE: The hours are represented using the numbers `0 - 23`

    **Print the hour, minute, second and microsecond separately**

    1. Import the time class from datetime:

        ```python
        from datetime import time
        ```

    2. Create an object to represent the time

        ```python
        # Using the format(hour, minute, second, microsecond)
        a = time(11, 45, 35, 234566) # Result: 11:45:35.234566

        print("Hour =", a.hour)
        print("Minute =", a.minute)
        print("Second =", a.second)
        print("Microsecond =", a.microsecond)
        ```

#### Representing a date and time

- The `datetime` module has a `datetime` class that allows us to represent both the date and time as one object

    1. Import the `datetime` class from `datetime`

        ```python
        from datetime import datetime
        ```

    2. Create an object to represent the date and time

        ```python
        # datetime(year, month, day, hour, minute, second and microsecond)
        a = datetime(2019, 5, 19, 15, 44, 32, 345678) 
        print(a) # Output: 2019-05-19 15:44:32.345678

        # datetime(year, month, day)
        b = datetime(2072, 3, 9)
        print(b)
        ```

    **Getting the current date and time:**

    - We can use the `datetime.now()` function to access the current date and time

    1. import the datetime class

        ```python
        from datetime import datetime
        ```

    2. Create an object to represent the current datetime

        ```python
        now = datetime.now()
        print(now)
        ```

#### Timestamp

- we can also create date objects from a timestamp.
- A UNIX timestamp is the number seconds between a particular date and **`1 January 1970 at UTC`**.
- You can convert a timestamp to a date using the `fromtimestamp()` method of the `date` class.

use the `fromtimestamp()` method of the `date` class function to get the date for 13599465454

```python
import datetime

date = datetime.date.fromtimestamp(13599465454)
```

#### Formatting the date and time

- The way date and time are represented may  be different across regions, places, organisations, etc.
- Python provides 2 methods to handle conversion of date and time formats:

    1. `strftime()`

        - is under the classes `date`, `time` and `datetime`. 
        - It creates aa formatted string from a given `date`, `time` or `datetime` object.

            ```python
            from datetime import datetime

            # current date and time
            now = datetime.now()

            # to format the time (H:M:S)
            formatted_time = now.strftime("%H:%M:%S")
            print("Time: ", formatted_time)

            # to format the date time to the US format (mm/dd/YY, H:M:S)
            us_format = now.strftime("%m/%d/%Y, %H:%M:%S")
            print(us_format)


            # to format the date to the German format (dd.mm.YYYY)
            de_format = now.strftime("%d.%m.%Y")
            print(de_format)
            ```

        > You can find the full list of format codes at: [https://www.w3schools.com/python/python_datetime.asp](https://www.w3schools.com/python/python_datetime.asp)

    2. `strptime()`

        - This functions 2 arguments:
            1. a **string** representing date and time
            2. format code equivalent to the first argument

        ```python
        from datetime import datetime

        date_string = "22 December, 2022"

        # use strptime() to create the date object
        date_object = datetime.strptime(date_string, "%d %B, %Y") 
        ```

## 24.01.25 timedelta, timezones and the calendar module

- what is timedelta
- creating a timedelta object
- difference two dates
- Using the calendar module
- Handling timezones

### What is timedelta?

- a `timedelta` object represents the difference between two dates or times.
- gives the out output in days and hours, minutes and seconds

#### Creating a timedelta object

1. Using the `date` class

    ```python
    from datetime import date

    # create 2 date objects
    date_1 = date(year=2007, month=6, day=20)
    date_2 = date(year=1965, month=3, day=4)
    
    # craeting the timedelta object
    timedelta_obj = date_1 - date_2 # Output: 15448 days, 0:00:00
    ```

2. Using the `datetime` class

    ```python
    from datetime import datetime

    # Create 2 datetime objects
    date_3 = datetime(year=2024, month=12, day=19, hour=9, minute=45, second=23)
    date_4 = datetime(year=2079, month=8, day=26, hour=15, minute=53, second=19)

    # creating the timedelta object
    timedelta_obj = date_3 - date_4

    print(timedelta_obj) # Output: -19974 days, 17:52:04
    ````

3. using the `timedelta` class

    ```python
    from datetime import timedelta

    # create 2 timedelta objects
    t_1 = timedelta(weeks=64, days=6, hours=5, minutes=45, seconds=33)
    t_2 = timedelta(days=100, hours=3, minutes=63, seconds=76)

    result = t_1 - t_2
    print(result) # Output: 354 days, 1:41:17
    ```

    **Using timedelta to get duration in seconds:**
    - The timedelta class has a `total_seconds()` function.

        ```python
        from datetime import timedelta

        t = timedelta(days=67, hours=23, minutes=15, seconds=45)

        print(t.total_seconds()) # Output: 5872545.0
        ```

### Using the calendar module

- Part of the built-in Python modules
- The calendar module allows us to output calendars and provides additional useful functions related to the calendar. 
- It uses the Gregorian calendar
- By default it has Monday as the first day of the week and Sunday as the last

    > You can find the documentation at: [https://docs.python.org/3/library/calendar.html](https://docs.python.org/3/library/calendar.html)


    **Display the calendar of a given month**

    ```python
    import calendar
    
    year = 1992
    month = 9

    print(calendar.month(year, month))
    ```

### Handling timezones using `pytz` module

- is a module that allows us to convert time between one timezone and the other

    ```python
    from datetime import datetime
    import pytz

    # get our local time
    local = datetime.datetime.now()
    print("Local time: ", local.strftime("%d/%m/%y, %H:%M"))

    # use the pytz module to get the New York Timezone
    ny_timezone = pytz.timezone("America/New_York")
    datetime_ny = datetime.datetime.now(ny_timezone)
    print("New York time: ", datetime_ny.strftime("%d/%m/%y, %H:%M"))

    # get the time for London ("Europe/London")
    lon_timezone = pytz.timezone("Europe/London")
    datetime_lon = datetime.datetime.now(lon_timezone)
    print("London time: ", datetime_lon.strftime("%d/%m/%y, %H:%M"))
    ```
