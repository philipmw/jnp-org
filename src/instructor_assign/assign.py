import logging
import math
from scipy.optimize import linear_sum_assignment

L = logging.getLogger(__name__)


def assign_instructors_to_groups(groups, all_instr_prefs):
    # We ensure the bipartite graph is balanced by expanding group categories
    # into a list containing an entry for each group, and likewise expanding
    # each group category preference into these entries.

    group_names_indexed = make_group_names_indexed(groups)

    prefs_matrix = [make_prefs_row(groups, instr_name, prefs)
                    for (instr_name, prefs) in all_instr_prefs.items()]
    L.debug("Prefs matrix: %s" % prefs_matrix)

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


def make_prefs_row(groups, instr_name, instr_pref):
    # Starting out, organizer-entered preferences sum to 0 by category.
    # We need to sum to 0 by broken-out groups.
    # We do this by dividing each expressed preference by group size.
    # To stick with integers, we multiply all values by the LCM of group sizes.

    multiplier = math.lcm(*groups.values())

    row = []
    for i, (cat_key, cat_qty) in enumerate(groups.items()):
        for group_i_of_cat in range(cat_qty):
            row.append(int(instr_pref[cat_key] * multiplier / cat_qty))

    if sum(row) != 0:
        raise Exception("Prefs matrix of %s has weights that add to %d, but expected 0"
                        % (instr_name, sum(row)))

    return row
