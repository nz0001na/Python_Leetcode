class Solution:
    def romanToInt(self, s: str) -> int:
        
        dic = {"I": 1, "V": 5, "X": 10, "L": 50,
                "C": 100, "D": 500, "M":1000}
        
        sp_dic = {"IV": 4, "IX": 9, "XL":40, "XC":90, "CD":400, "CM":900}

        n = len(s)
        if n <= 0: return None

        result = 0
        i = 0
        while(i < n):
            dc = s[i:i+2]
            if dc in sp_dic.keys():
                result += sp_dic[dc]
                i += 2
            else:
                c = s[i]
                result += dic[c]
                i += 1
                
        return result
