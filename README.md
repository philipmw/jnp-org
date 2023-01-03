# Organizing JNP #

## intended audience

Computer-savvy JNP organizers.
This software is not intended for the public (though it is open source for anyone interested).
It has only a command-line interface; no graphics.

## project goals

1. Records about each student that allow us to determine which ski group is most appropriate for them.
2. A system to assign students to the optimal ski group. This needs to take into account:
    * the number of groups we want;
    * minimum and maximum group sizes;
    * separation between kid and adult groups;
    * (maybe) affinity for certain pairs of students to be together or apart

## student records

Student records with the needed dimensions are in a Google Sheet shared by JNP leaders.

## assigning students to groups

There are two mechanisms I can think of:

1. [k-means clustering](https://en.wikipedia.org/wiki/K-means_clustering)
2. [assignment problem](https://en.wikipedia.org/wiki/Assignment_problem)

### K-means clustering

Specifically, the [k-means-constrained](https://joshlk.github.io/k-means-constrained/)
library, which allows us to set min/max size limits on clusters it produces.

Procedure:

1. Define one or more dimensions for students: age, skill, etc.
2. Define the desired number of groups, and the min/max group size
3. Apply _k-means-constrained_ clustering algorithm.

Pros:

* we maximize the similarity of members within each group
* it is relatively simple and I have it working already

Cons:

* limited control over group sizes, as min/max values are applied to *all* groups.
* no control over the quantity of groups assigned to each category of students.

Unknowns:

* how robustly can we control student-pair affinities?

### Assignment problem

Procedure: TBD.

Pros:

* finer control over group sizes, since we control slots directly

## How to use this software

These instructions were tested on macOS 13. I expect it would work on Linux and Windows just as well.

### Initial setup and run unit tests

1. Install Python 3.

Then go into this repository's directory, and:

    $ pip3 install .
    $ python3 -m unittest discover -v -s src

Unit tests should run and pass.

### To cluster students

1. Create a tab-separated values (TSV) file in the format of `./test_data/students-happy.tsv`

Then run:

    $ python3 -m student_km_clustering < ~/student_roster.tsv

If it succeeds, you'll get an output of your input file plus the cluster number for each student,
also in tab-separated values (TSV) format.

### To assign instructors to groups

1. Survey the instructors for their preferences.
2. Create a tab-separated values (TSV) file in the format of `./test_data/happy.tsv` with preferences.
3. Update `groups` in `__main__.py` with the quantity of each category of groups we need.
    The quantity of groups must match the quantity of instructors and their preferences.

Then run:

      $ python3 -m instructor_assign < ~/instructor_prefs.tsv

If it succeeds, you'll get an output of instructors with their group assignments,
also in tab-separated values (TSV) format.
