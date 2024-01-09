import unittest
from project8 import busiest_hour_per_app

class Test8(unittest.TestCase):
    def setUp(self):
        self.result= busiest_hour_per_app("test2.txt")
        print(self.result)
    def test_(self):
        self.assertEqual(self.result.get('BackendApp'),('01', 2))
        self.assertEqual(self.result.get('API'), ('17', 4))
        self.assertEqual(self.result.get('FrontendApp'),('13', 1))

       # self.assertEqual(self.result2,1)
        
if __name__ == '__main__':
    unittest.main()