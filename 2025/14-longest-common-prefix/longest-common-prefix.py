class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: return None
        if len(strs) == 1: return strs[0]
        
        target = strs[0]
        if target == "": return ""
        cur = 0
        while(cur < len(target)):
            for i in range(1,len(strs),1):
                if len(strs[i])<=cur:
                    return strs[i]
                if strs[i] == "": return ""
                if strs[i][cur] != target[cur]:
                    if cur > 0: 
                        return target[0:cur]
                    else:
                        return ""
                    break
            cur += 1
        return target[0:cur+1]




