class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) <= 0 or len(b) <= 0: return None
        max_len = max(len(a), len(b))
        str_a = a.zfill(max_len)
        str_b = b.zfill(max_len)

        is_add = 0
        re = []
        for i in range(max_len-1, -1, -1):
            if str_a[i] == '1' and str_b[i] == '1':
                if is_add == 1:
                    out = '1'                
                elif is_add == 0:
                    out = '0'
                is_add = 1

            if str_a[i] == '1' and str_b[i] == '0' or str_a[i] == '0' and str_b[i] == '1':
                if is_add == 1: 
                    out = '0'
                    is_add = 1
                elif is_add == 0:
                    out = '1'

            if str_a[i] == '0' and str_b[i] == '0':
                if is_add == 1: 
                    out = '1'
                    is_add = 0
                elif is_add == 0: 
                    out = '0'

            re.append(out)
        
        
        if is_add == 1: re.append('1')
        re.reverse()

        s = ""
        for i in range(len(re)): s += re[i]
        return s

        