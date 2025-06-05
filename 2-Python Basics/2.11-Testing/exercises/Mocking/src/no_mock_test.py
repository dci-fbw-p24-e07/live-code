import unittest
from app import rm
import os

# Task1
class RmTestCase(unittest.TestCase):
    def test_rm(self):
        # create a file
        open('somefile.txt', 'a')
        # try to delete it
        rm('somefile.txt')
        # check if still exist 
        self.assertFalse(os.path.isfile('/somefile.txt'), 'failed to remove the file')

if __name__ == '__main__':
    unittest.main()