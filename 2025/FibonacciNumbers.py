def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)


def fib_topdown(n, lookup):
    if n <= 1:
        lookup[n] = n

    if lookup[n] is None:
        lookup[n] = fib_topdown(n-1, lookup) + fib_topdown(n-2, lookup)

    return lookup[n]

def fib_bottomup(n):
    lookup = [None] * (n+1)
    lookup[0] = 0
    lookup[1] = 1
    for i in range(2, n+1,1):
        lookup[i] = lookup[i-1] + lookup[i-2]

    return lookup[n]


def fib_bottomspace(n):
    if n <=1: return n
    fn_1 = 1
    fn_2 = 0
    for i in range(2,n+1, 1):
        fn = fn_1 + fn_2
        fn_2 = fn_1
        fn_1 = fn

    return fn






n = 9
# lookup = [None] * (n+1)
# print(fib_topdown(n, lookup))
# print(fib_bottomup(9))
print(fib_bottomspace(9))