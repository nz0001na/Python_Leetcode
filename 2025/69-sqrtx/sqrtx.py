class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 0: return None

        root = 0
        while(root <= x):
            if root * root <= x and (root+1)*(root+1) > x:
                return root
            root += 1
        

