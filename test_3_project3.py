import unittest
from project3 import count_app_failures

class Test3(unittest.TestCase):
    def setUp(self):
        self.result = count_app_failures("test2.txt")

    def test1(self):
        self.assertEqual(self.result.get('FrontendApp'), 0)
        self.assertEqual(self.result.get('BackendApp'),1)
        self.assertEqual(self.result.get('API'),1)
        self.assertEqual(self.result.get('SYSTEM'),0)

if __name__ == '__main__':
    unittest.main()
