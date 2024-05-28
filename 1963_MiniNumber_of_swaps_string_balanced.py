'''
1963: (medium)

You are given a 0-indexed string s of even length n.
The string consists of exactly n / 2 opening brackets '[' and n / 2 closing brackets ']'.

A string is called balanced if and only if:

    It is the empty string, or
    It can be written as AB, where both A and B are balanced strings, or
    It can be written as [C], where C is a balanced string.

You may swap the brackets at any two indices any number of times.
Return the minimum number of swaps to make s balanced.


Example 1:
Input: s = "][]["
Output: 1
Explanation: You can make the string balanced by swapping index 0 with index 3.
The resulting string is "[[]]".

Example 2:

Input: s = "]]][[["
Output: 2
Explanation: You can do the following to make the string balanced:
- Swap index 0 with index 4. s = "[]][][".
- Swap index 1 with index 5. s = "[[][]]".
The resulting string is "[[][]]".

Example 3:
Input: s = "[]"
Output: 0
Explanation: The string is already balanced.


Constraints:
    n == s.length
    2 <= n <= 10^6
    n is even.
    s[i] is either '[' or ']'.
    The number of opening brackets '[' equals n / 2, and the number of closing brackets ']' equals n / 2.

'''

'''
***********************************************************************************
Solution:
  use a variable 'acc' to indicate the number difference of '[' and ']' for current index
  if difference shows more ']' than '[', accumulate the difference to variable 'swap', and reset acc=0, count again.
  Actually, in fact, 'swap' counts the number of ']' making the string not valid.
  In the end:
        (1) if 'swap' is even: 
            the final minimum swapping number is n/2.
        (2) if 'swap' is odd:
            the minimum swapping number is (n+1)/2
  
  

'''


class Solution:
    def minSwaps(self, s: str) -> int:
        acc = 0
        swap = 0
        for c in s:
            if c == '[':
                acc += 1
            else:
                acc -= 1

            if acc < 0:
                swap += -acc
                acc = 0

        return int((swap + 1) / 2)





