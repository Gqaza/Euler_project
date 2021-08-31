import unittest   # The test framework
from scripts.Collatz_sequence import collatz_seq
from scripts.smallest_multiple import smallest_multiple


class Test_EulerProjectSolutions(unittest.TestCase):
    def test_collatz_seq(self):
        seq_ = collatz_seq(13)
        expected_seq = [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        self.assertEqual(seq_, expected_seq)

    def test_smallest_multiple(self):
        res = smallest_multiple(10)
        expected_res = 2520
        self.assertEqual(res, expected_res)


if __name__ == '__main__':
    unittest.main()
