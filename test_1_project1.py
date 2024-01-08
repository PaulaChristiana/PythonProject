import unittest
from project1 import count

class Test1(unittest.TestCase):
    def setUp(self):
        self.result = count("test2.txt")
        print(self.result)
    def test_(self):
        self.assertEqual(self.result[('ERROR', 'BackendApp')],1)
        self.assertEqual(self.result[('INFO', 'BackendApp')],4)
        self.assertEqual(self.result[('INFO', 'API')],3)
        self.assertEqual(self.result[('DEBUG', 'SYSTEM')],1)
        self.assertEqual(self.result[('ERROR', 'API')],1)
        self.assertEqual(self.result[('DEBUG', 'API')],1)
        self.assertEqual(self.result[('DEBUG', 'FrontendApp')],2)

        
if __name__ == '__main__':
    unittest.main()