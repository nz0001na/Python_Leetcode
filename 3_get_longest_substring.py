'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


Approach 1: Brute-force methods, two loop searching
Approach 2: slide window with set
'''


# brute-force method
def lengthOfLongestSubstring(str):
    count = len(str)
    if count == 0 or count == 1:
        return count
    length = []
    for i in range(count):
        cha = {}
        n = 1
        cha[str[i]] = n
        for j in range(i+1, count):
            key = str[j]
            if key in cha.keys():
                length.append(n)
                break
            else:
                n = n + 1
                cha[str[j]] = n
                if j == count - 1:
                    length.append(n)
                    break
    length.sort(reverse=True)
    return length[0]


# slide window with set
def lengthOfLongestSubstring2(str):
    count = len(str)
    if count == 0 or count == 1:
        return count
    i,j = 0,0
    A = set()
    max = 0
    while (i < count and j < count):
        if str[j] not in A:
            A.add(str[j])
            if j == count - 1:
                if max < len(A): max = len(A)
                break
            j = j + 1
        else:
            if max < len(A): max = len(A)
            A.clear()
            i = i + 1
            j = i
    return max



str = 'pwwkew'
print(lengthOfLongestSubstring2(str))