'''
13. Roman to Integer
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together.
Twelve is written as, XII, which is simply X + II.
The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII. Instead, the number four is written as IV.
Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX.
There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:
Input: "III"
Output: 3

Example 2:
Input: "IV"
Output: 4

Example 3:
Input: "IX"
Output: 9

Example 4:
Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 5:
Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''


def roman2int(s):
    hashtab = {}
    hashtab['IV'] = 4
    hashtab['IX'] = 9
    hashtab['XL'] = 40
    hashtab['XC'] = 90
    hashtab['CD'] = 400
    hashtab['CM'] = 900
    hashtab['I'] = 1
    hashtab['V'] = 5
    hashtab['X'] = 10
    hashtab['L'] = 50
    hashtab['C'] = 100
    hashtab['D'] = 500
    hashtab['M'] = 1000

    count = len(s)
    sum = 0
    i = 0
    while(i<count):
        ch = s[i]
        if ch=='I':
            if (i< count-1 and s[i+1] == 'V') or (i< count-1 and s[i+1] == 'X'):
                sum += hashtab[ch+s[i+1]]
                i = i+2
            else:
                sum += hashtab['I']
                i += 1
        elif ch == 'X':
            if i< count-1 and s[i+1] == 'L' or i< count-1 and s[i+1]=='C':
                sum += hashtab[ch+s[i+1]]
                i = i+2
            else:
                sum += hashtab['X']
                i += 1
        elif ch == 'C':
            if i< count-1 and s[i+1] == 'D' or i< count-1 and s[i+1]=='M':
                sum += hashtab[ch+s[i+1]]
                i = i+2
            else:
                sum += hashtab['C']
                i += 1
        else:
            sum += hashtab[ch]
            i += 1
    return sum





s = 'IX'
print(roman2int(s))