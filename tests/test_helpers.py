import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from utils.helpers import (
    index_a,
    dateadder,
    datefiller,
    middle_date,
    compare,
    dict_order,
    datetostamp,
    earlydate,
    formtimeseq,
    indexs
)

class TestHelpers(unittest.TestCase):

    def test_index_a(self):
        arr = [1, 2, 3, 2, 4, 2]
        self.assertEqual(index_a(arr, 1, 2), 1)  # 1st occurrence of 2
        self.assertEqual(index_a(arr, 2, 2), 3)  # 2nd occurrence of 2
        self.assertEqual(index_a(arr, 3, 2), 5)  # 3rd occurrence of 2
        self.assertEqual(index_a(arr, 1, 5), -1) # Not found

    def test_dateadder(self):
        dates = dateadder("2020-01-01", 3)
        self.assertEqual(dates, ["2020-01-01", "2020-01-02", "2020-01-03"])

    def test_datefiller(self):
        dates = datefiller("2020-01-01", "2020-01-03")
        self.assertEqual(dates, ["2020-01-01", "2020-01-02", "2020-01-03"])
        with self.assertRaises(ValueError):
            datefiller("2020-01-03", "2020-01-01")

    def test_middle_date(self):
        mid = middle_date("2020-01-01", "2020-01-11")
        self.assertEqual(mid, "2020-01-06")

    def test_compare(self):
        result = compare("ATT", "ATC")
        self.assertEqual(result['diff'], 1)
        self.assertEqual(result['diffpos'], [2])
        self.assertEqual(result['change'], ["T-C"])

    def test_dict_order(self):
        d = {'a': 3, 'b': 1, 'c': 2}
        self.assertEqual(dict_order(d), ['b', 'c', 'a'])
        self.assertEqual(dict_order(d, Ascending=False), ['a', 'c', 'b'])

    def test_datetostamp(self):
        ts = datetostamp("2020-01-01")
        self.assertTrue(isinstance(ts, float))

    def test_earlydate(self):
        self.assertTrue(earlydate("2020-01-01", "2020-01-02"))
        self.assertFalse(earlydate("2020-01-02", "2020-01-01"))

    def test_formtimeseq(self):
        # Unsorted dates
        adict = {"2020-05-01": 1, "2019-12-01": 1, "2021-01-01": 1, "invalid_date": 1}
        sorted_dates = formtimeseq(adict)
        self.assertEqual(sorted_dates, ["2019-12-01", "2020-05-01", "2021-01-01"])

    def test_indexs(self):
        lst = [1, 2, 3, 5, 6, 8]
        groups = indexs(lst)
        self.assertEqual(groups, [[1, 2, 3], [5, 6], [8]])

if __name__ == '__main__':
    unittest.main()
