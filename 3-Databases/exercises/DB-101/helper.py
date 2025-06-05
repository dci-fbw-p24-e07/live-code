from multiprocessing import Process
import os
import sys
from optparse import OptionParser
import math
from faker import Faker


def generate_data(rows, columns, file_name='customers.csv'):
    try:
        rows = int(rows)
    except TypeError:
        print("Number of rows should be an integer")
        sys.exit(1)
    f = open(file_name, 'w')
    f.write(",".join(columns) + "\n")
    f.close()
    content = ""
    for i in range(1, rows+1):
        _faker = Faker()
        name = _faker.name()
        address = _faker.address()
        date_of_birth = _faker.date_of_birth()
        row = "{},{},{},{}\n".format(i, name, '-'.join(
            address.replace(',', '').split('\n')), date_of_birth)
        content += row
        print(row)
        print('='*(math.floor(0.5 * len(row))))
    f = open(file_name, 'a')
    f.write(content)
    f.close()


def file_open(*args):
    fileName = args[0]

    with open(os.path.dirname(__file__) + "/" + fileName) as f:
        data = f.read()
        print(data)


def profile():
    pass


def read_file(users=1, file_name='customers.csv'):
    try:
        for i in range(int(users)):
            p = Process(target=file_open, args=([file_name]))
            p.start()
            p.join()
    except:
        print(
            "An error occurred, fix by using the correct integer value or correct file name")
        sys.exit()


# TODO -> experiment with editing a file while reading its contents
# TODO -> confirm how easy profiling could be with timeit
parser = OptionParser()
parser.add_option('-t', '--task', dest="task", help="Run a task e.g. make-csv")
parser.add_option('--file', dest='file',
                  help="The file you would like to create.")
parser.add_option('--rows', dest='rows',
                  help="The number of rows to be filled with data in file.")
parser.add_option('--users', dest='users',
                  help="The number of users attempting to access file.")
if __name__ == '__main__':
    (options, args) = parser.parse_args()

    # Default values
    file_name = None
    task = None
    number_of_users = 10
    rows = 10

    if options:
        try:
            task = options.task
        except AttributeError:
            print(
                "Missing an argument needed for the task you want to run. See documentation.")
            sys.exit(1)

        try:
            file_name = options.file
        except:
            pass

        try:
            rows = options.rows
        except:
            pass

        if task == 'make-csv' and not file_name:
            raise Exception('A file name is required when making a CSV file')

        if task == 'make-csv':
            generate_data(rows, ['id', 'name', 'address',
                          'date_of_birth'], file_name)
        try:
            users = options.users
        except:
            pass

        if task == 'read-csv':
            read_file(users, file_name)
