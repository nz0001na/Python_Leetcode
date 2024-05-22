'''
Question: (Meduim)

We can shift a string by shifting each of its letters to its successive letter.

For example, "abc" can be shifted to be "bcd".
We can keep shifting the string to form a sequence.

For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd" -> ... -> "xyz".

Given an array of strings strings, group all strings[i] that belong to the same shifting sequence.
You may return the answer in any order.


Example 1:
Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]

Example 2:
Input: strings = ["a"]
Output: [["a"]]


Constraints:

1 <= strings.length <= 200
1 <= strings[i].length <= 50
strings[i] consists of lowercase English letters.

'''


'''
Solution 1:
use dictionary to store the result:
        Key: pattern of string in the input array, for example, ‘#2#6#9#13#’, 
             number between '#' means difference between two characters s[i] and s[i+1].
        value: substring list with same pattern as shown in the key
the values are result.

'''
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:

        def key(s):
            k = '#'
            for i in range(1, len(s)):
                b = s[i]
                a = s[i - 1]
                d = (ord(b) + 26 - ord(a)) % 26
                k = k + str(d) + '#'
            return k

        num = len(strings)
        if num <= 0:
            return None

        r_dict = {}
        result = []
        for i in range(len(strings)):
            k = key(strings[i])
            if k in r_dict.keys():
                r_dict[k].append(strings[i])
            else:
                r_dict[k] = [strings[i]]

        result = list(r_dict.values())
        return result





