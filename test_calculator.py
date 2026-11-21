import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self):
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(-2, 3), -6)
        self.assertEqual(mul(0, 5), 0)

    def test_divide(self):
        self.assertEqual(div(2, 10), 5)
        self.assertEqual(div(5, 10), 2)
        self.assertEqual(div(-2, 10), -5)
    # ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(2, -5)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(5, 12), 13)
        self.assertAlmostEqual(hypotenuse(-3, -4), 5)

    def test_sqrt(self):
        self.assertAlmostEqual(square_root(25), 5)
        self.assertAlmostEqual(square_root(2), 1.41421356)
        with self.assertRaises(ValueError):
            square_root(-4)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()