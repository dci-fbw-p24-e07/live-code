import unittest
from tool import Tool, Laptop


# Do not modify the following
# Test Class : code for running the test
class TestGadget(unittest.TestCase):
    def setUp(self):
        self.l1 = Laptop()

    def test_instance(self):
        self.assertIsInstance(self.l1, Tool)

    def test_use_method(self):
        try:
            self.l1.work()
            result = True, "All OK!"
        except NotImplementedError as e:
            print(str(e))
            result = False, str(e)
        self.assertTrue(result, msg=result[1])


if __name__ == '__main__':
    unittest.main()
