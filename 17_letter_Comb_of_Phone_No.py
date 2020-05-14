'''
17. Letter Combinations of a Phone Number
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.



'''

def lettercomb(digits):
    if len(digits) == 0:
        return ''

    hashtab = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    result = ['']
    for digit in digits:
        tmp_list = []
        for ch in hashtab[digit]:
            for sb in result:
                tmp_list.append(sb+ch)
                # print(sb+ch)
        result = tmp_list
    return result


def lettercomb2(digits):
    if len(digits) == 0:
        return ''

    map = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    result = ['']
    for digit in digits:
        tmp_list = []
        for ss in result:
            for ch in map[digit]:
                tmp_list.append(ss+ch)
        result = tmp_list
    return result



digits = ''
print(lettercomb(digits))
print(lettercomb2(digits))