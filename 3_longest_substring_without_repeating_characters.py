'''
3. (medium)
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.



'''


'''
Solution 1: 
    for loop with index cur on input string:
       create a sliding window: [left, cur-1]
       last_index show the last appearance (index) of current char.
       length of substring: the length of sliding window.
    
    Dictionary: store last appearance of each character
    
    if s[cur] is not in the dictionary as a key, add into the dictionary.
    if yes, check if the index (in value) of stored key at last appearance (last_index) in s is in the sliding window.
        if no, just update the index value of this key in dictionary.
        if yes, get the size of the sliding window, move the left point of the sliding window to last_index+1.
    get max length.
    
    note: ' ' character can not be the key in dictionary.


'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        dict_q = {}
        maxLen = 0
        left = 0
        last_index = -1

        for cur in range(len(s)):
            c = s[cur]
            if c == " ": c = 's s'
            if c not in dict_q.keys():
                dict_q[c] = cur
            else:
                last_index = dict_q[c]
                if last_index < left:
                    dict_q[c] = cur
                    continue
                else:
                    count = cur - left
                    if count > maxLen:
                        maxLen = count

                    left = last_index + 1
                    dict_q[c] = cur

        if len(s) - left > maxLen:
            maxLen = len(s) - left

        return maxLen


'''
Solution 2:

    Dictionary: store characters only appeared in the sliding window.
                del dict[k] if not is the sliding window.

'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        dict_q = {}
        maxLen = 0
        left = 0
        last_index = -1

        for cur in range(len(s)):
            c = s[cur]
            if c == " ": c = 's s'
            if c not in dict_q.keys():
                dict_q[c] = cur
            else:
                count = len(dict_q)
                if count > maxLen:
                    maxLen = count

                last_index = dict_q[c]
                while (left <= last_index):
                    if s[left] == ' ':
                        del dict_q['s s']
                    else:
                        del dict_q[s[left]]
                    left += 1

                dict_q[c] = cur

        if len(s) - left > maxLen:
            maxLen = len(s) - left

        return maxLen
