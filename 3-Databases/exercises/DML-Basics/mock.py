from random import random, randrange
from datetime import datetime, timedelta


FIRST_NAMES = ('Abdul', 'David', 'Julia', 'Arnold', 'Bernhard', 'Gerald', 'Anna', 'Yussef', 'Itziar', 'Olivia', 'Emma', 'Amelia', 'Mia', 'Chloe', 'Penelope', 'Grace', 'Layla', 'Ella', 'Abigail', 'Camila', 'Gianna', 'Evelyn', 'Aaliyah', 'Naomi', 'Aarya', 'Araceli', 'Yamileth', 'Loretta', 'Liam', 'Noah', 'William', 'Lucas', 'Benjamin', 'Marc', 'Oriol', 'Arturo', 'Keith', 'Zain', 'Johann', 'Nikolas', 'Ahmed')

LAST_NAMES = ('Smith', 'Blanc', 'Müller', 'Miller', 'Muller', 'Griesebner', 'Hutticher', 'Karnasiotti', 'Martí', 'Vidal', 'Masferrer', 'Doe', 'Adams', 'Anniston', 'Hunter', 'Schwarzenegger', 'White', 'Black', 'Green', 'Schumacher', 'Perez', 'Fiedler', "O''Connor", "McDonald", 'Johnson', 'Williams', 'Brown', 'Garcia', 'Jones', 'Davis', 'Wilson', 'Moore', 'Jackson', 'Lee', 'Ali', 'Ahmas', 'Sanchez', 'Clark', 'Hill', 'Young', 'Wright', 'Lewis', 'Nguyen', 'Allen')

INSTRUMENTS = ("Guitar", "Electric Bass", "Trumpet", "Cello", "Saxphone", "Piano", "Voice", "Drums", "Keyboard", "Flute", "Harp", "Violin", "Trombone", "Clarinet")


def rand(options):
    """Pick an item randomly."""
    index = int(random() * len(options))
    return options[index]


def composed_name(prefix=FIRST_NAMES, suffix=LAST_NAMES):
    """Return a random name."""
    return rand(prefix) + ' ' + rand(suffix)


def date(start=None, end=None):
    """Return a random date after start."""
    start_date = datetime.strptime(start, '%Y-%M-%d')
    if not end:
        end_date = datetime.now()
    else:
        if isinstance(end, str):
            end = datetime.strptime(end, '%Y-%M-%d')
        end_date = end
    time_between_dates = end_date - start_date
    days_between_dates = int(time_between_dates.total_seconds())
    random_number_of_days = randrange(days_between_dates)
    random_date = start_date + timedelta(seconds=random_number_of_days)
    return random_date


def rand_integer(min=0, max=10000):
    """Return a random integer."""
    return randrange(max - min) + min


def fk(total, null=True):
    """Return a random foreign key."""
    _id = randrange(total)
    if _id == 0:
        if null:
            return "NULL"
        return _id + 1
    return _id


num_facilities = 9
# musician
table = 'musician'
sql = f"INSERT INTO {table}(first_name, last_name, date_of_birth, instrument) VALUES\n"
num_members = 384

for i in range(0, num_members):
    first = rand(FIRST_NAMES)
    last = rand(LAST_NAMES)
    birth = date(start='1950-08-10', end="2001-05-05")
    instrument = rand(INSTRUMENTS)
    sql = sql + f"\t('{first}', '{last}', '{birth}', '{instrument}')"
    if i < num_members - 1:
        sql = sql + ",\n"
    else:
        sql = sql + ";"
print(sql)
