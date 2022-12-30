from instructor_assign.assign import assign_instructors_to_groups

# A mapping from group name (must be a unique identifier) to the quantity
# of instructors needed for this group.
#
groups = {
    # Treasure Trails, ages 4-6
    'TT': 1,
    # Little Nords, ages 6-9
    'LN': 1,
    # Trailblazers, ages 9-13 (beginning to intermediate)
    'TB': 1,
    # Freeheelers, ages 9-13 (intermediate to advanced)
    'FH': 1,
    # parents
    'pa': 1,
}

# Assign N points across the groups above to each instructor.
all_instr_prefs = {
    'Instructor 1': {'TT': 2, 'LN': 2, 'TB': 2, 'FH': 2, 'pa': 2},
    'Instructor 2': {'TT': 2, 'LN': 2, 'TB': 2, 'FH': 2, 'pa': 2},
    'Instructor 3': {'TT': 2, 'LN': 2, 'TB': 2, 'FH': 2, 'pa': 2},
    'Instructor 4': {'TT': 2, 'LN': 2, 'TB': 2, 'FH': 2, 'pa': 2},
    'Instructor 5': {'TT': 2, 'LN': 2, 'TB': 2, 'FH': 2, 'pa': 2},
}

if __name__ == "__main__":
    print(assign_instructors_to_groups(groups, all_instr_prefs))
