import unittest
from sample import divide

class TestDivide(unittest.TestCase):

    def test_divide(self):
        self.assertEqual(divide(4,2), 2)



if __name__ == '__main__':
    unittest.main()
