elements = ['a', 'b', 'c']

def powerset(elements):
    result = [[]]

    for elem in elements:
        new_subsets = [subset + [elem] for subset in result]
        result += new_subsets
    return result
