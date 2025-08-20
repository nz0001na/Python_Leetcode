class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) <= 0 or len(b) <= 0: return None
        max_len = max(len(a), len(b))
        str_a = a.zfill(max_len)
        str_b = b.zfill(max_len)

        is_add = 0
        re = ""
        for i in range(max_len-1, -1, -1):
            s = int(str_a[i]) + int(str_b[i]) + is_add
            out = str(s%2)
            is_add = s//2         
            re = out + re
        
        if is_add == 1: re = '1' + re
        
        return re

        