import unittest
from instructor_assign.assign import assign_instructors_to_groups


class TestAssign(unittest.TestCase):
    def test_balanced(self):
        groups = {'g1': 1, 'g2': 1, 'g3': 1}
        all_instr_prefs = {
            'i1': {'g1': 0, 'g2': 0, 'g3': 1},
            'i2': {'g1': 0, 'g2': 1, 'g3': 0},
            'i3': {'g1': 1, 'g2': 0, 'g3': 0},
        }
        expected_assignments = {
            'i1': 'g3',
            'i2': 'g2',
            'i3': 'g1',
        }
        actual_assignments = assign_instructors_to_groups(groups, all_instr_prefs)
        self.assertEqual(actual_assignments, expected_assignments)

    def test_balanced_big_groups(self):
        groups = {'g1': 3, 'g2': 1}
        all_instr_prefs = {
            'i1': {'g1': 0, 'g2': 1},
            'i2': {'g1': 0, 'g2': 1},
            'i3': {'g1': 1, 'g2': 0},
            'i4': {'g1': 1, 'g2': 0},
        }
        expected_assignments = {
            'i1': 'g2',
            'i2': 'g1',
            'i3': 'g1',
            'i4': 'g1',
        }
        actual_assignments = assign_instructors_to_groups(groups, all_instr_prefs)
        self.assertEqual(actual_assignments, expected_assignments)

    def test_not_enough_instructors(self):
        groups = {'g1': 1, 'g2': 2}
        all_instr_prefs = {
            'i1': {'g1': 0, 'g2': 1},
            'i2': {'g1': 1, 'g2': 0},
        }

        with self.assertRaisesRegex(Exception, 'Not enough instructors for the groups'):
            assign_instructors_to_groups(groups, all_instr_prefs)

    def test_too_many_instructors(self):
        groups = {'g1': 1, 'g2': 1}
        all_instr_prefs = {
            'i1': {'g1': 0, 'g2': 1},
            'i2': {'g1': 1, 'g2': 0},
            'i3': {'g1': 0, 'g2': 0},
        }

        with self.assertRaisesRegex(Exception, 'Too many instructors for the groups'):
            assign_instructors_to_groups(groups, all_instr_prefs)
