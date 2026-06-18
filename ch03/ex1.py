s = [1, 2, 3, 5, 6, 7, 8, 10, 12, 13, 15, 16, 18, 19, 20, 22]

def binary_search(x, a):
    i = 0
    j = len(a) - 1

    while i < j:
        m = (i + j) // 2

        if x > a[m]:
            i = m + 1
        else:
            j = m

    if x == a[i]:
        location = i + 1
    else:
        location = 0

    return location

# Test
print(binary_search(19, s))
