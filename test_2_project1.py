import unittest
from project2 import average_run_time_excluding_system

class Test2(unittest.TestCase):
    def setUp(self):
        self.result = average_run_time_excluding_system("test2.txt")
        print(self.result)
    def test_(self):
        self.assertEqual(self.result[('BackendApp')],17.25)
        self.assertEqual(self.result[('API')],18.67)
        
if __name__ == '__main__':
    unittest.main()