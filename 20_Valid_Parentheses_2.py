'''
20. Valid Parentheses
'''

def isValid(s):
    count = len(s)
    if count == 0:
        return True
    s_list = []
    s_map = {')': '(', ']':'[', '}':'{'}
    for i in range(count):
        c = s[i]
        if c in ['(', '[', '{']:
            s_list.append(c)
        if c in [')', '}', ']']:
            if len(s_list) == 0:
                return False
            else:
                cp = s_list.pop()
            if cp != s_map[c]:
                return False
    return True


s = "({})[()]{[]}]"
print(isValid(s))