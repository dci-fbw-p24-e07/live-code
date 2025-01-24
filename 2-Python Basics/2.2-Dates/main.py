import datetime
import calendar
import pytz


d = datetime.date(2026, 9, 14)
print(d)

a = datetime.time(11, 45, 35, 234566)
print(a)

# Using the format(hour, minute, second)
b = datetime.time(11, 45, 35)
print(b)

# Using the format(hour, minute)
c = datetime.time(11, 45)
print(c)

e = datetime.datetime(2019, 5, 19, 15, 44, 32, 345678)
print(e)

# datetime(year, month, day)
f = datetime.datetime(2072, 3, 9)
print(f)

now = datetime.datetime.now()
print(now)

date = datetime.date.fromtimestamp(13599465454)
print(date)

# to format the time (H:M:S)
formatted_time = now.strftime("%I:%M:%S %p")
print("Time: ", formatted_time)

# to format the date time to the US format (mm/dd/YY, H:M:S)
us_format = now.strftime("%m/%d/%Y, %H:%M:%S")
print(us_format)

# to format the date to the German format (dd.mm.YYYY)
de_format = now.strftime("%d.%m.%Y")
print(de_format)

date_string = "22 December, 2022"

# use strptime() to create the date object
date_object = datetime.datetime.strptime(date_string, "%d %B, %Y") 
print(date_object)


# create 2 date objects
date_1 = datetime.date(year=2007, month=6, day=20)
date_2 = datetime.date(year=1965, month=3, day=4)

# creating the timedelta object
timedelta_obj = date_1 - date_2

print(timedelta_obj)

# Create 2 datetime objects
date_3 = datetime.datetime(year=2024, month=12, day=19, hour=9, minute=45, second=23)
date_4 = datetime.datetime(year=2079, month=8, day=26, hour=15, minute=53, second=19)

# creating the timedelta object
timedelta_obj_2 = date_3 - date_4

print(timedelta_obj_2)


# create 2 timedelta objects
t_1 = datetime.timedelta(weeks=64, days=6, hours=5, minutes=45, seconds=33)
t_2 = datetime.timedelta(days=100, hours=3, minutes=63, seconds=76)

result = t_1 - t_2
print(result)


year = 1992
month = 9

print(calendar.month(year, month))
print(calendar.isleap(2021))


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
