import unittest

from prime_factors import PrimeFactors

class PrimeFactorsTest(unittest.TestCase):

    def test_one_should_return_empty(self):
        prime_factors = PrimeFactors(1)
        expected = []
        actual = prime_factors.get_data()
        self.assertEqual(expected, actual)

    def test_two_should_return_two(self):
        prime_factors = PrimeFactors(2)
        expected = [2]
        actual = prime_factors.get_data()
        self.assertEqual(expected, actual)

    def test_three_should_return_three(self):
        prime_factors = PrimeFactors(3)
        expected = [3]
        actual = prime_factors.get_data()
        self.assertEqual(expected, actual)

    def test_three_should_return_two_two(self):
        prime_factors = PrimeFactors(4)
        expected = [2, 2]
        actual = prime_factors.get_data()
        self.assertEqual(expected, actual)

    def test_three_should_return_five(self):
        prime_factors = PrimeFactors(5)
        expected = [5]
        actual = prime_factors.get_data()
        self.assertEqual(expected, actual)

    def test_three_should_return_six(self):
        prime_factors = PrimeFactors(6)
        expected = [2, 3]
        actual = prime_factors.get_data()
        self.assertEqual(expected, actual)

    def test_three_should_return_seven(self):
        prime_factors = PrimeFactors(7)
        expected = [7]
        actual = prime_factors.get_data()
        self.assertEqual(expected, actual)

    def test_three_should_return_two_two_two(self):
        prime_factors = PrimeFactors(8)
        expected = [2, 2, 2]
        actual = prime_factors.get_data()
        self.assertEqual(expected, actual)

    def test_three_should_return_three_three(self):
        prime_factors = PrimeFactors(9)
        expected = [3, 3]
        actual = prime_factors.get_data()
        self.assertEqual(expected, actual)

