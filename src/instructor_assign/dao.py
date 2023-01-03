import csv
import logging

EXPECTED_POINT_SUM = 0

QTY_COLS_BEFORE_PREFS = 1
PREF_KEY_SEQ = ['TT', 'LN', 'TB', 'FH', 'pa']
DIALECT = 'excel-tab'
L = logging.getLogger(__name__)


def read_prefs(csvfh):
    header_seen = False
    instructors = {}

    reader = csv.reader(csvfh, dialect=DIALECT)
    for rawrow in reader:
        L.debug("Read TSV row: %s" % rawrow)
        if not header_seen:
            # This is the header row
            header_seen = True

            expected_cols_min = QTY_COLS_BEFORE_PREFS + len(PREF_KEY_SEQ)
            cols_ignored = len(rawrow) - expected_cols_min
            if cols_ignored > 0:
                L.warning("Ignoring %d columns in the input" % cols_ignored)

            for i, key in enumerate(PREF_KEY_SEQ):
                col_name = rawrow[i+1]
                if col_name != key:
                    raise Exception('In header row, col %d, expected %s but got %s' % (i+1, key, col_name))
            L.debug("Verified header row")
            continue

        name = rawrow[0]
        if name in instructors:
            raise Exception('duplicate instructor: %s' % name)

        instructors[name] = {}
        for i, group_cat in enumerate(PREF_KEY_SEQ):
            instructors[name][group_cat] = int(rawrow[i+1])
        L.debug("Saved instructor %s with preferences %s" % (name, instructors[name]))

        point_sum = sum(instructors[name].values())
        if point_sum != EXPECTED_POINT_SUM:
            raise Exception('For %s, prefs sum to %d points, but we expected sum of %d'
                            % (name, point_sum, EXPECTED_POINT_SUM))

    L.info("Read %d instructors from TSV input" % len(instructors))

    return instructors
