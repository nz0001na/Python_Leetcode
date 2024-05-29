'''
438: medium

Given two strings s and p, return an array of all the start indices of p's anagrams in s.
You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.


Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".



Constraints:

    1 <= s.length, p.length <= 3 * 104
    s and p consist of lowercase English letters.


'''



'''
*******************************************************************************
Solution 1: straight-forward solution
    create frequency dictionary 'freq' to represent p.
    loop for s:
        get substring with length as len(p), create a frequency dictionary too.
        compare with 'freq' to check if same.
    
Time: O(n^2)
Space: O(n)

'''

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return

        freq = {}
        for c in p:
            if c in freq.keys():
                freq[c] += 1
            else:
                freq[c] = 1
        res = []
        for j in range(len(s)-len(p)+1):
            sub = s[j:j+len(p)]
            q = {}
            for c in sub:
                if c in q.keys():
                    q[c] += 1
                else:
                    q[c] = 1
            if q == freq:
                res.append(j)
        return res




''''
*******************************************************************************
Solution 2:
   use a sliding window strategy [l, i], l: left location of the list s, i: right location of list s.
   dictionary 'freq' shows the frequency of each letters occurs in list p.
   variable 'count' indicates the the number of letters that the sliding window still needs.
   2 loops:
   outer loop: i from 0 to len(s)
        add s[i] into the sliding window, if s[i] is contained in p, check if freq[s[i]]>0, if so, count-1( it means
        the sliding window needs this letter to meet the requirement of p, and after added into the window, count decreases by 1), 
        and then freq[s[i]]-1.
   inner loop :
        if the value of 'count' is 0, means the window don't need any extra letters required by p,
        next, we need to analyze the window if contains anagrams of p.
        this loop is to move left location 'l' to right to try to find possible anagrams.
        for each loop (count == 0 and l<=i)
            remove s[l] out of the window.
            freq[s[l]] + 1.
            if freq[s[l]] > 0: count + 1
            when the length of window equals to len(p), we can add index l to result list.

Time: O(n)
Space: O(1)

Notes:
(1) letter to ASCII: function ord()
    e.g., ord('a')

'''


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        freq = {}
        for i in range(26):
            freq[ord('a') + i] = 0
        for c in p:
            freq[ord(c)] += 1

        l = 0
        res = []
        count = len(p)
        for i in range(len(s)):
            c = s[i]
            if freq[ord(c)] > 0:
                count -= 1
            freq[ord(c)] -= 1
            while (count == 0 and i >= l):
                cl = s[l]
                freq[ord(cl)] += 1
                if freq[ord(cl)] > 0:
                    count += 1
                if i - l + 1 == len(p):
                    res.append(l)
                l += 1
        return res







