def is_one_to_one(f, n):
    outputs = {f(x) for x in range(1, n + 1)}

    return len(outputs) == n

# Test
def f_one(x):
    return x * 2

print(is_one_to_one(f_one, n=3))
