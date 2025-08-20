class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n <= 0: return None

        left_list = ['(', '{', '[']
        right_list = [')', '}', ']']
        match_dict = {'(':')', '[':']', '{':'}'}

        stack_s = []

        for i in range(n):
            cur = s[i]
            if cur in left_list:
                stack_s.append(match_dict[cur])
            if cur in right_list:
                if len(stack_s) <= 0: return False
                if cur == stack_s[-1]:
                    stack_s.pop()
                else:
                    return False
        
        if len(stack_s) == 0: 
            return True
        else:
            return False
       
        