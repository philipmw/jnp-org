import csv
import logging

DIALECT = 'excel-tab'

L = logging.getLogger(__name__)


def read_student_data(csvfh):
    students = {}

    reader = csv.reader(csvfh, dialect=DIALECT)
    for rawrow in reader:
        L.debug("Read TSV row: %s" % rawrow)
        name = rawrow[0]
        age = int(rawrow[1])
        skill = int(rawrow[2]) if rawrow[2] != '' else 0
        cat = 'a' if rawrow[3] == 'adult' else 'j'
        if name in students:
            raise Exception('duplicate student: %s' % name)
        students[name] = {
            'age': age,
            'skill': skill,
            'cat': cat,
        }

    L.info("Read %d students from TSV input" % len(students))

    return students


def write_cluster_data(csvfile, students):
    # Write it in tab-separated file since we have commas in the attribute dictionary
    writer = csv.writer(csvfile, dialect=DIALECT)
    for student_record in students:
        writer.writerow(student_record)

    L.info("Wrote %d students to TSV output" % len(students))
