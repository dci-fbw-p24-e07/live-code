import datetime


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