import unittest   # The test framework
from scripts.Collatz_sequence import collatz_seq
from scripts.smallest_multiple import smallest_multiple
from scripts.p27_quadratic_primes import (
    quadratic_equation,
    quad_primes_size
)
from scripts.p26ReciprocalCycles import max_cycle


class Test_EulerProjectSolutions(unittest.TestCase):
    def test_collatz_seq(self):
        seq_ = collatz_seq(13)
        expected_seq = [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        self.assertEqual(seq_, expected_seq)

    def test_smallest_multiple(self):
        res = smallest_multiple(10)
        expected_res = 2520
        self.assertEqual(res, expected_res)

    def test_quadratic_equation(self):
        res = quadratic_equation(2, 1, 1)
        assert res == 5
        assert quadratic_equation(0, 1, 1) == 1
        assert quadratic_equation(-2, 1, 1) == 3

    def test_no_quadratic_primes(self):
        no_primes = quad_primes_size(1, 41, 0, 39)
        assert no_primes == 40

        no_primes = quad_primes_size(-79, 1601, 0, 79)
        assert no_primes == 80

    def test_max_reciprocal_cycle(self):
        # Assert max_cycle for values less 10
        mrc = max_cycle(10)
        assert mrc.get("cycle") == "142857"
        assert mrc.get("len") == 6
        assert mrc.get("denominator") == 7

        # Assert max_cycle for values less 2
        mrc = max_cycle(2)
        assert mrc.get("cycle") == ""
        assert mrc.get("len") == 0
        assert mrc.get("denominator") is None


if __name__ == '__main__':
    unittest.main()
