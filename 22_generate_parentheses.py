'''
22. Generate Parentheses
https://www.youtube.com/watch?v=sz1qaKt0KGQ
https://www.youtube.com/watch?v=PCb1Ca_j6OU

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]


'''

# recursion

def generate(s, open, close, k, res_list):
    if close==k:
        res_list.append(s)
        return res_list
    if open < k:
        generate(s+'(', open+1, close, k, res_list)
    if close < open:
        generate(s+')', open, close+1, k, res_list)



def generateParentheses(n):
    if n < 1:
        return None
    result_list = []
    generate('(', 1, 0, n, result_list)
    return result_list


n = 2
print(generateParentheses(n))