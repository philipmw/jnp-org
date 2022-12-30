from k_means_constrained import KMeansConstrained

DEFAULT_CLUSTER_SETTINGS = {
    'n': 18,
    'size_min': 5,
    'size_max': 11,
}


def student_attributes_to_feature_array(attr_dict):
    age = attr_dict['age']
    skill = attr_dict['skill']
    skillage = age + skill

    cat = 100 if attr_dict['cat'] == 'a' else 0
    return [skillage, cat]


def assign_clusters(students, cluster_settings=None):
    if cluster_settings is None:
        cluster_settings = DEFAULT_CLUSTER_SETTINGS

    # feature array
    farray = list(map(student_attributes_to_feature_array, students.values()))

    # https://joshlk.github.io/k-means-constrained/
    km = KMeansConstrained(
        n_clusters=cluster_settings['n'],
        size_min=cluster_settings['size_min'],
        size_max=cluster_settings['size_max'],
        random_state=0
    )

    # group students by cluster
    predictions = km.fit_predict(farray)

    assignments = [[] for x in range(km.n_clusters)]
    for i, name in enumerate(students.keys()):
        cluster_i = predictions[i]
        assignments[cluster_i].append(name)

    cluster_assn = []
    for cluster_i in range(len(assignments)):
        student_list = assignments[cluster_i]
        for student_name in student_list:
            attrs = students[student_name]
            cluster_assn.append([
                cluster_i,
                student_name,
                # Write out attrs as one cell so that we don't have to define
                # the list of attributes here and keep it in sync with other places.
                attrs
            ])

    return cluster_assn
