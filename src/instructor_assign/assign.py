from scipy.optimize import linear_sum_assignment


def assign_instructors_to_groups(groups, all_instr_prefs):
    group_names_indexed = make_group_names_indexed(groups)

    prefs_matrix = [make_prefs_row(group_names_indexed, prefs) for prefs in all_instr_prefs.values()]
    (assn_row_ind, assn_col_ind) = linear_sum_assignment(prefs_matrix, maximize=True)

    if len(assn_row_ind) != len(all_instr_prefs):
        raise Exception('Too many instructors for the groups')

    if len(assn_col_ind) != sum(groups.values()):
        raise Exception('Not enough instructors for the groups')

    assignments = {}
    for i, instr_name in enumerate(all_instr_prefs.keys()):
        assignments[instr_name] = group_names_indexed[assn_col_ind[i]]

    return assignments


def make_group_names_indexed(groups):
    group_names_indexed = []
    for i, (cat_key, cat_qty) in enumerate(groups.items()):
        for group_i_of_cat in range(cat_qty):
            group_names_indexed.append(cat_key)
    return group_names_indexed


def make_prefs_row(group_names_indexed, instr_pref):
    row = []
    for group_name in group_names_indexed:
        row.append(instr_pref[group_name])
    return row
