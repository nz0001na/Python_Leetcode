'''
Given a string s, find the length of the longest
substring without repeating characters.
'''


'''
create a sliding window: [left, cur-1]
last_index show the last appearance of current char.
length of substring: the length of sliding window.

Dictionary: store last appearance of each character

'space' character can not be the key in dictionary.


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
Dictionary: store characters only appeared in the sliding window.

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
