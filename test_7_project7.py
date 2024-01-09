import unittest
from project7 import run_times_per_app

class Test7(unittest.TestCase):
    def setUp(self):
        self.result= run_times_per_app("test2.txt")
        print(self.result)
    def test_(self):
        self.assertEqual(self.result[0].get('BackendApp'),('13:08:50', 20))
        self.assertEqual(self.result[0].get('API'), ('03:42:50', 22))
        self.assertEqual(self.result[1].get('BackendApp'),('02:51:24', 15))
        self.assertEqual(self.result[1].get('API'),('17:23:35', 14))

       # self.assertEqual(self.result2,1)
        
if __name__ == '__main__':
    unittest.main()