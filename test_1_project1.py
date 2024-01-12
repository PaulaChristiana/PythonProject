import unittest
from project1 import count
from project2 import average_run_time_excluding_system
from project3 import count_app_failures3
from project4 import count_app_failures

class Test1(unittest.TestCase):
    def setUp(self):
        self.result = count("test2.txt")
        self.result2 = average_run_time_excluding_system("test2.txt")
        self.result3 = count_app_failures3("test2.txt")
        self.result41, self.result42  = count_app_failures("test2.txt")

    def test_(self):
        self.assertEqual(self.result[('ERROR', 'BackendApp')],1)
        self.assertEqual(self.result[('INFO', 'BackendApp')],4)
        self.assertEqual(self.result[('INFO', 'API')],3)
        self.assertEqual(self.result[('DEBUG', 'SYSTEM')],1)
        self.assertEqual(self.result[('ERROR', 'API')],1)
        self.assertEqual(self.result[('DEBUG', 'API')],1)
        self.assertEqual(self.result[('DEBUG', 'FrontendApp')],2)
    
    def test_2(self):
        self.assertEqual(self.result2[('BackendApp')],17.25)
        self.assertEqual(self.result2[('API')],18.67)

    def test_3(self):
        self.assertEqual(self.result3.get('FrontendApp'), 0)
        self.assertEqual(self.result3.get('BackendApp'),1)
        self.assertEqual(self.result3.get('API'),1)
        self.assertEqual(self.result3.get('SYSTEM'),0)

    def test_4(self):
        self.assertEqual(self.result41,"BackendApp")
        self.assertEqual(self.result42,1)

        
if __name__ == '__main__':
    unittest.main()