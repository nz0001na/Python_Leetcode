class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        if n <= 0: return None

        right = n-1
        while (s[right] == ' ' and right >= 0): 
            right = right - 1
        if right < 0: return 0

        count = 0
        while(s[right] != ' ' and right >= 0):
            count += 1
            right -= 1
        
        return count
        