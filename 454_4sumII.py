'''
454. 4Sum II
Medium

Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are
such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500.
All integers are in the range of -2**28 to 2**28 - 1 and the result is guaranteed to be at most 2**31 - 1.

Example:

Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
'''

#  brute-force method
def sum4(A, B, C, D):
    cnt = len(A)
    timer = 0
    for i in range(cnt):
        for j in range(cnt):
            for k in range(cnt):
                for l in range(cnt):
                    if A[i] + B[j] + C[k] + D[l] == 0:
                        timer += 1
                        print(str(A[i]) + ',' + str(B[j]) + ',' + str(C[k]) + ',' + str(D[l]))
    return timer

# use hashmap
def sum4_2(A, B, C, D):
    hashmap = {}
    for i in range(len(A)):
        for j in range(len(B)):
            s = A[i] + B[j]
            if s in hashmap:
                hashmap[s] += 1
            else:
                hashmap[s] = 1

    timer = 0
    for k in range(len(C)):
        for l in range(len(D)):
            ss = C[k] + D[l]
            if -ss in hashmap:
                timer += hashmap[-ss]

    return timer


# use two hashmap
def sum4_3(A, B, C, D):
    cnt = len(A)
    hashmap1 = {}
    hashmap2 = {}
    for i in range(cnt):
        for j in range(cnt):
            s1 = A[i] + B[j]
            if s1 not in hashmap1:
                hashmap1[s1] = 1
            else:
                hashmap1[s1] += 1
            s2 = C[i] + D[j]
            if s2 not in hashmap2:
                hashmap2[s2] = 1
            else:
                hashmap2[s2] += 1
    timer = 0
    for ch in hashmap1:
        if -ch in hashmap2:
            timer += hashmap1[ch]*hashmap2[-ch]
    return timer




# A = [ 1, 2]
# B = [-2,-1]
# C = [-1, 2]
# D = [ 0, 2]

A = [-1,-1]
B = [-1,1]
C = [-1,1]
D = [1,-1]

print(sum4_3(A, B, C, D))