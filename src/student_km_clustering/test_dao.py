import os
import unittest
from student_km_clustering.dao import read_student_data


class TestDao(unittest.TestCase):
    def test_read(self):
        dirname = os.path.dirname(__file__)
        test_filename = os.path.join(dirname, './test_data/students-happy.tsv')
        with open(test_filename, newline='') as csvfh:
            students = read_student_data(csvfh)

        self.assertEqual(len(students), 4)
        # check last record of the file
        self.assertEqual(students['Weaker, 16'], {'age': 16, 'skill': -1, 'cat': 'j'})

    def test_read_duplicate_names(self):
        dirname = os.path.dirname(__file__)
        test_filename = os.path.join(dirname, './test_data/students-duplicate.tsv')
        with open(test_filename, newline='') as csvfh:
            with self.assertRaisesRegex(Exception, 'duplicate student: Neutral, 15'):
                read_student_data(csvfh)
