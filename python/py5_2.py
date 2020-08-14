def fib(n):
    if n < 1 :
        return []
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]
    for i in range(2, n):
        fibs.append(fibs[i - 1] + fibs[i - 2])
    return fibs


import unittest


class FibTest(unittest.TestCase):
    def test_generate_5_fibs(self):
        self.assertEqual(fib(5), [1, 1, 2, 3, 5])

    def test_generate_10_fibs(self):
        self.assertEqual(fib(10), [1, 1, 2, 3, 5, 8, 13, 21, 34, 55])

    def test_generate_negative_number_fibs(self):
        self.assertEqual(fib(-2), [])

    def test_generate_0_number_fibs(self):
        self.assertEqual(fib(0), [])

    def test_generate_1_number_fibs(self):
        self.assertEqual(fib(1), [1])

    def test_generate_2_number_fibs(self):
        self.assertEqual(fib(2), [1, 1])

if __name__ == '__main__':
    unittest.main()
