"""Tests for functions in statistics."""
from unittest import TestCase
from statistics import average, variance, stdev
from math import sqrt


class AverageTest(TestCase):
    """Tests for average function."""

    def test_average_interger(self):
        """Average of integers."""
        self.assertEqual(10, average([10, 10, 10, 10, 10]))
        self.assertEqual(3, average([1, 2, 3, 4, 5]))
        self.assertEqual(6, average([10, 2, 8, 4, 6]))

    def test_average_none(self):
        """Average of empty list raise ValueError."""
        self.assertRaises(ValueError, average, [])


class VarianceTest(TestCase):
    """Tests for variance function."""

    def test_variance_typical_values(self):
        """Variance of typical values."""
        self.assertEqual(0.0, variance([10.0, 10.0, 10.0, 10.0, 10.0]))
        self.assertEqual(2.0, variance([1, 2, 3, 4, 5]))

    def test_variance_non_integers(self):
        """Variance should work with decimal values."""
        # variance([x,y,z]) == variance([x+d,y+d,z+d]) for any d
        self.assertAlmostEqual(4.0, variance([0.1, 4.1]), delta=0.001)
        # variance([0,4,4,8]) == 8
        self.assertAlmostEqual(8.0, variance([0.1, 4.1, 4.1, 8.1]),
                               delta=0.001)

    def test_variance_none(self):
        """Variance of empty list raise ValueError."""
        self.assertRaises(ValueError, variance, [])


class StdevTest(TestCase):
    """Tests for stdev function."""

    def test_stdev(self):
        """Standard devaiation of values."""
        # standard deviation of a single value should be zero
        self.assertEqual(0.0, stdev([10.0]))
        # simple test
        self.assertEqual(2.0, stdev([1, 5]))
        # variance([0, 0.5, 1, 1.5, 2.0]) is 0.5
        self.assertEqual(sqrt(0.5), stdev([0, 0.5, 1, 1.5, 2]))
