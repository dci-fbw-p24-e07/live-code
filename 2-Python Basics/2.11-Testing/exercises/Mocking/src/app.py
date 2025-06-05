import os

def rm(filename):
    # Task4
    if os.path.isfile(filename):
        os.remove(filename)
    else:
        raise FileNotFoundError('file is not found')