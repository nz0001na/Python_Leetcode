class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits) == 0: return None
        re = []
        add = 0
        for i in range(len(digits)-1,-1,-1):
            cur = digits[i]
            if i == len(digits) -1:
                out = cur + 1
                if out == 10:
                    re.append(0)
                    add = 1
                else:
                    re.append(out)
                continue
            
            if cur == 9 and add == 1: 
                re.append(0)
                add = 1
            else:
                re.append(cur + add)
                add = 0
        
        if add == 1: re.append(1)
        re.reverse()
        return re








        