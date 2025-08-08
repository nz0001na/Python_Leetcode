class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        n = len(s)

        reverse_s = []
        for i in range(n-1, -1, -1):
            reverse_s.append(s[i])
        
        list_s = list(s)
        if list_s == reverse_s:
            return True
        else:
            return False




       