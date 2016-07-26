from mathmagician import *
import unittest

class test_mathmagician(unittest.TestCase):

    def test_structure(self):
        self.structure_test = Mathmagician()
        self.assertIsInstance(self.structure_test, Mathmagician)
        self.assertEqual(self.structure_test.number, 0)

    def test_primes(self):
        self.prime_test = Mathmagician()

        self.prime_test.prime(3)
        self.assertEqual(self.prime_test.number, 5)

        self.prime_test.prime(1)
        self.assertEqual(self.prime_test.number, 2)

        self.prime_test.prime(5)
        self.assertEqual(self.prime_test.number, 11)

        self.prime_test.prime(8)
        self.assertEqual(self.prime_test.number, 19)

    def test_fibonacci(self):
        self.fibonacci_test = Mathmagician()

        self.fibonacci_test.fibonacci(3)
        self.assertEqual(self.fibonacci_test.number, 2)

        self.fibonacci_test.fibonacci(1)
        self.assertEqual(self.fibonacci_test.number, 1)

        self.fibonacci_test.fibonacci(5)
        self.assertEqual(self.fibonacci_test.number, 5)

        self.fibonacci_test.fibonacci(8)
        self.assertEqual(self.fibonacci_test.number, 21)

    def test_integers(self):
        self.integer_test = Mathmagician()

        self.integer_test.integer(3)
        self.assertEqual(self.integer_test.number, 3)

        self.integer_test.integer(1)
        self.assertEqual(self.integer_test.number, 1)

        self.integer_test.integer(5)
        self.assertEqual(self.integer_test.number, 5)

        self.integer_test.integer(8)
        self.assertEqual(self.integer_test.number, 8)


if __name__ == '__main__':
    unittest.main()
