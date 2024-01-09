import unittest
from project6 import third_of_day_with_most_failures

class Test6(unittest.TestCase):
    def setUp(self):
        self.result1, self.result2 = third_of_day_with_most_failures("test2.txt")
    def test_(self):
        self.assertEqual(self.result1,'00:00:00 - 07:59:59')
        self.assertEqual(self.result2,1)
        
if __name__ == '__main__':
    unittest.main()