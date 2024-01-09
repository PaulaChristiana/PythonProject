import unittest
from project9 import calculate_failure_rates


class Test9(unittest.TestCase):
    def setUp(self):
        self.result= calculate_failure_rates("test2.txt")
        
    def test_(self):
        
        self.assertEqual(self.result.get('BackendApp'), 11.11)
        self.assertEqual(self.result.get('API'), 12.50)
        self.assertEqual(self.result.get('SYSTEM'), 0.0)
        self.assertEqual(self.result.get('FrontendApp'), 0.0)
        
if __name__ == '__main__':
    unittest.main()