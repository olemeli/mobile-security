from itertools import combinations, permutations

adj_matrix = [[0, 1, 0, 1, 1, 0, 0, 0, 0],
              [1, 0, 1, 1, 1, 1, 0, 0, 0],
              [0, 1, 0, 0, 1, 1, 0, 0, 0],
              [1, 1, 0, 0, 1, 0, 1, 1, 0],
              [1, 1, 1, 1, 0, 1, 1, 1, 1],
              [0, 1, 1, 0, 1, 0, 0, 1, 1],
              [0, 0, 0, 1, 1, 0, 0, 1, 0],
              [0, 0, 0, 1, 1, 1, 1, 0, 1],
              [0, 0, 0, 0, 1, 1, 0, 1, 0]]

vertices = [0, 1, 2, 3, 4, 5, 6, 7, 8]

def all_permutations(k):
    combs = list(combinations(vertices, k))
    perms = list()
    for comb in combs:
        perms_of_comb = list(permutations(list(comb)))
        perms.extend(perms_of_comb)
    return perms

def check_for_path(possible_path):
    for i in range(1, len(possible_path)):
        if adj_matrix[possible_path[i-1]][possible_path[i]] == 0:
            return False
    return True

def all_valid_paths_of_length(k):
    perms = all_permutations(k)
    valid_paths = []
    for possible_path in perms:
        if (check_for_path(list(possible_path))):
            valid_paths.append(possible_path)
    return valid_paths

def count_valid_paths_of_length(k):
    return len(all_valid_paths_of_length(k))


for k in range(2, 10):
    print(count_valid_paths_of_length(k) / 2)
