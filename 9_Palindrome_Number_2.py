'''
reverse the number
'''

def isPalindrome_1(x):
    x_str = str(x)
    x_rev = ''
    count = len(x_str)
    for i in range(count):
        c = x_str[count-1-i]
        x_rev = x_rev + c
    if x_str == x_rev:
        return True
    else:
        return False

'''
compare two sides
'''
def isPalindrome_2(x):
    x_str = str(x)
    count = len(x_str)
    for i in range(count//2+1):
        if x_str[i] != x_str[count-i-1]:
            return False
        else:
            return True



x = 121
print(isPalindrome_1(x))
print(isPalindrome_2(x))