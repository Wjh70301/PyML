import unittest
from pyml.maths.math_utils import *
from pyml.maths.linear_algebra import *
from pyml.utils import set_seed
import random


class MathsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        set_seed(1970)

        cls.A = [[random.random() for e in range(8)] for x in range(10)]
        cls.B = [[random.random() for e in range(10)] for x in range(8)]

    def test_sort(self):
        array = [-5, 3, 10, 2, 1, -1]
        sorted_array = sort(array)
        self.assertEqual(sorted_array, [-5, -1, 1, 2, 3, 10])

    def test_argsort(self):
        array = [-5, 3, 10, 2, 1, -1]
        argsorted_array = argsort(array)
        self.assertEqual(argsorted_array, [0, 5, 4, 3, 1, 2])

    def test_mean_0(self):
        self.assertAlmostEqual(mean(self.A, 0)[0], 0.44000517100025094)

    def test_mean_0_shape(self):
        self.assertEqual(len(mean(self.A, 0)), 8)

    def test_mean_1(self):
        self.assertAlmostEqual(mean(self.A, 1)[5], 0.5668557306974099)

    def test_mean_1_shape(self):
        self.assertEqual(len(mean(self.A, 1)), 10)


class LinearAlgebraTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        set_seed(1970)

        cls.A = [[random.random() for e in range(8)] for x in range(10)]
        cls.B = [[random.random() for e in range(10)] for x in range(8)]

    def test_transpose(self):
        self.assertAlmostEqual(transpose(self.A)[5][8], 0.38628163852256203)

    def test_matrix_product(self):
        self.assertAlmostEqual(dot_product(self.A, self.B)[5][8], 2.2269865779018874)

    def test_dot_product(self):
        self.assertAlmostEqual(dot_product(self.A[0], transpose(self.B)[0])[0], 0.691239893627)

    def test_subtract(self):
        self.assertAlmostEqual(subtract(self.A, transpose(self.B))[0][3], 0.6442101271237023)

    def test_power(self):
        self.assertAlmostEqual(power(self.A, 2)[0][5], 0.9336806492618525)

    def test_divide(self):
        self.assertAlmostEqual(divide(self.A[0], 0.5)[0], 0.2792398429743861)
