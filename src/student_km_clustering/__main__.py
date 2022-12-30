import sys

from student_km_clustering.cluster import assign_clusters
from student_km_clustering.dao import read_student_data, write_cluster_data


def main(fh_in, fh_out):
    # Expected source format:
    # name, age, skill, category
    students = read_student_data(fh_in.readlines())

    augmented_roster = assign_clusters(students)

    # write cluster assignments back to CSV
    write_cluster_data(fh_out, augmented_roster)


if __name__ == "__main__":
    main(sys.stdin, sys.stdout)
