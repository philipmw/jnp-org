import logging
import sys

from instructor_assign.assign import assign_instructors_to_groups
from instructor_assign.dao import read_prefs

# A mapping from group name (must be a unique identifier) to the quantity
# of instructors needed for this group.
#
groups = {
    # Treasure Trails, ages 4-6
    'TT': 3,
    # Little Nords, ages 6-9
    'LN': 5,
    # Trailblazers, ages 9-13 (beginning to intermediate)
    'TB': 5,
    # Freeheelers, ages 9-13 (intermediate to advanced)
    'FH': 4,
    # parents
    'pa': 2,
}


def print_roster_tsv(roster):
    print("instructor\tgroup")
    for (name, group) in roster.items():
        print("%s\t%s" % (name, group))


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    print_roster_tsv(
        assign_instructors_to_groups(groups, read_prefs(sys.stdin))
    )
