'''
204. Count Primes
Easy

Count the number of prime numbers less than a non-negative number, n.

Example:
Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

'''



def countprime(n):
    nums=[True for i in range(n)]

    i = 2
    while i*i<n:
        j = i
        while j*i < n:
            nums[j*i] = False
            j += 1
        i += 1


    count = 0
    for p in range(2,n):
        if nums[p] == True:
            count += 1

    print(count)
    return count







n = 10
print(countprime(n))