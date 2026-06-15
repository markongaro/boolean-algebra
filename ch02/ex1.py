u = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
n = len(u)

A_set = {'a','c', 'e', 'f', 'h', 'd'}
B_set = {'g', 'd', 'a', 'c'}


def to_bitstring(subset, universe):
    bitmask = 0
    for i, item in enumerate(universe):
        if item in subset:
            bitmask |= 1 << (len(universe) -1 - i)
    return bitmask


def fmt(bitmask, length):
    return f"{bitmask:0{length}b}"

# TOD0: Write a function that converts an integer bitmask to characters

a_bits = to_bitstring(A_set, u)
b_bits = to_bitstring(B_set, u)




        
