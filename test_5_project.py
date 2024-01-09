import unittest
from project5 import app_with_most_successful_runs

class Test5(unittest.TestCase):
    def setUp(self):
        self.result1, self.result2  = app_with_most_successful_runs("test2.txt")
    def test1(self):
        self.assertEqual(self.result1,"BackendApp")
        self.assertEqual(self.result2,4)

if __name__ == '__main__':
    unittest.main()