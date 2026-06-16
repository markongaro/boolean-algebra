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

def to_set(bitmask, universe):
    dump_set = set()
    for i, item in enumerate(universe):
        shift_len = len(universe) - 1 - i

        if (bitmask >> shift_len) & 1:
            dump_set.add(item)
    return dump_set

a_bits = to_bitstring(A_set, u)
b_bits = to_bitstring(B_set, u)

# TODO: Perform logic operations (Union, Intersection, Complement e.t.c)



        
