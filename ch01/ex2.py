import math

def num_of_subsets(n):
    total_subsets = 0

    for u in range(n + 1):
        total_subsets += math.comb(n, u)
    return total_subsets

