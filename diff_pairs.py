import unittest

"""

Given a list of integers and a single integer k, find the number of unique pairs where each pair is an integer in
the list and the difference between k and that integer, if the difference is in the list.

[1, 2, 3] with k=3 returns 2 because the following unique pairs:

(1, 2), (2, 1)  created from  3-1 (2) -> (1, 2) and 3-2 (1) -> (2, 1)

A dictionary (hash table) is used to provide a runtime complexity of O(2 * n)

"""


def number_of_pairs(a, k):
    pairs = []
    diffs = {}
    for value in a:
        if value not in diffs:
            diffs[value] = k - value
    for value in a:
        diff = k - value
        if diff in diffs:
            p1 = (value, diffs[diff])
            if p1 not in pairs:
                pairs.append(p1)
    return len(pairs)


class TestNumberOfPairs(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(number_of_pairs([1, 2, 3], 3), 2)

    def do_biglist(self):
        return number_of_pairs(self.gen_list(1000), 1000)

    def gen_list(self, n):
        count = 0
        while count < n:
            yield count
            count += 1


if __name__ == '__main__':
    unittest.main()
