import unittest
from student_km_clustering.cluster import assign_clusters


class TestCluster(unittest.TestCase):
    def test_two_junior_clusters(self):
        students = {
            'Neutral15': {'age': 15, 'cat': 'j', 'skill': 0},
            'Neutral16': {'age': 16, 'cat': 'j', 'skill': 0},
            'Stronger15': {'age': 15, 'cat': 'j', 'skill': 1},
            'Weaker16': {'age': 16, 'cat': 'j', 'skill': -1},
        }
        expected_roster = [
            [0, 'Neutral15', {'age': 15, 'cat': 'j', 'skill': 0}],
            [0, 'Weaker16', {'age': 16, 'cat': 'j', 'skill': -1}],
            [1, 'Neutral16', {'age': 16, 'cat': 'j', 'skill': 0}],
            [1, 'Stronger15', {'age': 15, 'cat': 'j', 'skill': 1}],
        ]
        actual_roster = assign_clusters(students, {'n': 2, 'size_min': 1, 'size_max': 4})
        self.assertEqual(actual_roster, expected_roster)

    def test_juniors_and_adults(self):
        students = {
            'Adult1': {'age': 20, 'cat': 'a', 'skill': 0},
            'Adult2': {'age': 20, 'cat': 'a', 'skill': 0},
            'Adult3': {'age': 20, 'cat': 'a', 'skill': 0},
            'Adult4': {'age': 20, 'cat': 'a', 'skill': 0},
            'Junior1': {'age': 20, 'cat': 'j', 'skill': 0},
        }
        expected_roster = [
            [0, 'Junior1', {'age': 20, 'cat': 'j', 'skill': 0}],
            [1, 'Adult1', {'age': 20, 'cat': 'a', 'skill': 0}],
            [1, 'Adult2', {'age': 20, 'cat': 'a', 'skill': 0}],
            [1, 'Adult3', {'age': 20, 'cat': 'a', 'skill': 0}],
            [1, 'Adult4', {'age': 20, 'cat': 'a', 'skill': 0}],
        ]
        actual_roster = assign_clusters(students, {'n': 2, 'size_min': 1, 'size_max': 4})
        self.assertEqual(actual_roster, expected_roster)
