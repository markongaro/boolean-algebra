u = ['a', 'b', 'c','d', 'e', 'f', 'g', 'h']
n = len(u)

A_set = {'a', 'c', 'd', 'e', 'h'}
B_set = {'b', 'e', 'h', 'g'}

def to_bitstring(subset, u):
    bitmask = 0

    for i, item in enumerate(u):
        if item in subset:
            bitmask |= 1 << (n - 1 - i)
    return bitmask

def to_set(bitmask, universe):
    dmp_set = set()

    for i, item in enumerate(universe):
        shift_len = len(universe) - 1 - i

        if (bitmask >> shift_len) & 1:
            dmp_set.add(item)
    return dmp_set

def fmt(bitmask, length):
    return f"{bitmask:0{length}b}"

a_bits = to_bitstring(A_set, u)
b_bits = to_bitstring(B_set, u)

complement_mask = (1 << n) - 1
not_a_bits = ~a_bits & complement_mask
not_b_bits = ~b_bits & complement_mask

a_union_b = a_bits | b_bits
a_intersection_b = a_bits & b_bits
a_minus_b = a_bits & not_b_bits
a_xor_b = a_bits ^ b_bits

# Test
print(f"A'    (Complement):     {fmt(not_a_bits, n)}")
print(f"A ∪ B (Union):          {fmt(a_union_b, n)}")
print(f"A ∩ B (Intersection):   {fmt(a_intersection_b, n)}")
print(f"A − B (Difference):     {fmt(a_minus_b, n)}")
print(f"A ⊕ B (Symmetric Diff): {fmt(a_xor_b, n)}")
