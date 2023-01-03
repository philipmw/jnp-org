import os
import unittest
from instructor_assign.dao import read_prefs


class TestDao(unittest.TestCase):
    def test_read_happy(self):
        dirname = os.path.dirname(__file__)
        test_filename = os.path.join(dirname, './test_data/happy.tsv')
        with open(test_filename, newline='') as csvfh:
            instr_prefs = read_prefs(csvfh)

        self.assertEqual(len(instr_prefs), 2)
        # check last record of the file
        self.assertEqual(instr_prefs['White, Philip'], {'TT': -1, 'LN': -1, 'TB': -1, 'FH': 2, 'pa': 1})

    def test_read_duplicate(self):
        dirname = os.path.dirname(__file__)
        test_filename = os.path.join(dirname, './test_data/duplicate.tsv')
        with open(test_filename, newline='') as csvfh:
            with self.assertRaisesRegex(Exception, 'duplicate instructor: Last, First'):
                read_prefs(csvfh)

    def test_read_wrong_points(self):
        dirname = os.path.dirname(__file__)
        test_filename = os.path.join(dirname, './test_data/wrong_points.tsv')
        with open(test_filename, newline='') as csvfh:
            with self.assertRaisesRegex(Exception, 'For Last, First, prefs sum to 1 points, but we expected sum of 0'):
                read_prefs(csvfh)

    def test_read_wrong_header(self):
        dirname = os.path.dirname(__file__)
        test_filename = os.path.join(dirname, './test_data/wrong_header.tsv')
        with open(test_filename, newline='') as csvfh:
            with self.assertRaisesRegex(Exception, 'In header row, col 3, expected TB but got FH'):
                read_prefs(csvfh)
