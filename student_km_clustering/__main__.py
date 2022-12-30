import sys

import cluster
import dao


def main(fh_in, fh_out):
    # Expected source format:
    # name, age, skill, category
    students = dao.read_student_data(fh_in.readlines())

    augmented_roster = cluster.assign_clusters(students)

    # write cluster assignments back to CSV
    dao.write_cluster_data(fh_out, augmented_roster)


if __name__ == "__main__":
    main(sys.stdin, sys.stdout)
