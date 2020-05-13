'''
273. Integer to English Words
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

Example 1:
Input: 123
Output: "One Hundred Twenty Three"

Example 2:
Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"

Example 3:
Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

Example 4:
Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"

'''


def int2english(num):
    if num==0:
        return 'Zero '

    hashtab = {}
    hashtab[0] = 'Zero '
    hashtab[1] = 'One '
    hashtab[2] = 'Two '
    hashtab[3] = 'Three '
    hashtab[4] = 'Four '
    hashtab[5] = 'Five '
    hashtab[6] = 'Six '
    hashtab[7] = 'Seven '
    hashtab[8] = 'Eight '
    hashtab[9] = 'Nine '
    hashtab[10] = 'Ten '
    hashtab[11] = 'Eleven '
    hashtab[12] = 'Twelve '
    hashtab[13] = 'Thirteen '
    hashtab[14] = 'Fourteen '
    hashtab[15] = 'Fifteen '
    hashtab[16] = 'Sixteen '
    hashtab[17] = 'Seventeen '
    hashtab[18] = 'Eighteen '
    hashtab[19] = 'Nineteen '
    hashtab[20] = 'Twenty '
    hashtab[30] = 'Thirty '
    hashtab[40] = 'Fourty '
    hashtab[50] = 'Fifty '
    hashtab[60] = 'Sixty '
    hashtab[70] = 'Seventy '
    hashtab[80] = 'Eighty '
    hashtab[90] = 'Ninety '
    hashtab[100] = 'Hundred '

    hlist = [100,10,1]

    def int2eng00(n):
        s = ''
        flag = 0
        for i in range(len(hlist)):
            d = n//hlist[i]
            if d > 0:
                if i==0:
                    s += hashtab[d] + hashtab[100]
                elif i == 1:
                    if d > 1:
                        s += hashtab[d*10]
                    elif d == 1:
                        flag = 1
                elif i==2:
                    if flag==1:
                        s += hashtab[10+d]
                    else:
                        if d > 0:
                            s += hashtab[d]
            else:
                if flag==1 and i==2:
                    s += hashtab[10]
            n = n%hlist[i]
        return s

    dlist = [10**9, 10**6, 10**3, 1]
    dic = {}
    dic[10**9] = 'Billion '
    dic[10**6] = 'Million '
    dic[10**3] = 'Thousand '


    ss = ''
    for j in range(len(dlist)):
        dd = num//dlist[j]
        if dd > 0:
            if j == 0:
                ss += int2eng00(dd) + dic[10**9]
            elif j == 1:
                ss += int2eng00(dd) + dic[10**6]
            elif j == 2:
                ss += int2eng00(dd) + dic[10**3]
            else:
                ss += int2eng00(dd)
        num = num%dlist[j]

    return ss.strip()


num = 10
print(int2english(num))
# print(2**31-1)