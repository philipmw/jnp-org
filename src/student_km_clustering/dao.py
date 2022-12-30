import csv


def read_student_data(csvfh):
    students = {}

    reader = csv.reader(csvfh)
    for rawrow in reader:
        name = rawrow[0]
        age = int(rawrow[1])
        skill = int(rawrow[2]) if rawrow[2] != '' else 0
        cat = 'a' if rawrow[3] == 'adult' else 'j'
        if name in students:
            raise Exception('duplicate student %s' % name)
        students[name] = {
            'age': age,
            'skill': skill,
            'cat': cat,
        }

    return students


def write_cluster_data(csvfile, augmented_roster):
    # Write it in tab-separated file since we have commas in the attribute dictionary
    writer = csv.writer(csvfile, dialect='excel-tab')
    for roster_row in augmented_roster:
        writer.writerow(roster_row)
