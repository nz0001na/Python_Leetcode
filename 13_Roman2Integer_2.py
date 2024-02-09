'''
use dictionary
'''

def romanToInt_1(s):
    roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    inst_dict = {'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
    count = len(s)
    result = 0
    i = 0
    while i < count:
        ch = s[i:i+2]
        c = s[i]
        if ch in inst_dict.keys():
            result += inst_dict.get(ch)
            i += 2
            continue
        else:
            result += roman_dict[c]
            i += 1
    return result


s = "LVIII"
s = "MCMXCIV"
print(romanToInt_1(s))