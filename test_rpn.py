import unittest

import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate("1 1 +")
        self.assertEqual(2, result)
    def test_subtract(self):
        result = rpn.calculate("5 3 -")
        self.assertEqual(2, result)
    def test_multiply(self):
        result = rpn.calculate("5 3 *")
        self.assertEqual(15, result)
    def test_divide(self):
        result = rpn.calculate("6 3 /")
        self.assertEqual(2, result)
    def test_carat(self):
        result = rpn.calculate("5 3 ^")
        self.assertEqual(125, result)
    def test_summation(self):
        result = rpn.calculate("5 3 1 sum")
        self.assertEqual(9, result)
    def test_rotation(self):
        result = rpn.calculate("5 3 1 rot")
        self.assertEqual(5, result)
    def test_copy(self):
        result = rpn.calculate("5 3 1 copy")
        self.assertEqual(1, result)

if __name__ == '__main__':
    unittest.main()
