import unittest
from project4 import count_app_failures

class Test4(unittest.TestCase):
    def setUp(self):
        self.result1, self.result2  = count_app_failures("test2.txt")
    def test1(self):
        self.assertEqual(self.result1,"BackendApp")
        self.assertEqual(self.result2,1)

if __name__ == '__main__':
    unittest.main()