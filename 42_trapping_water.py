'''
42. Trapping Rain Water
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

Example:
Input: [3,2,1,0,4,2,3,1,5]
output: 12

Approach:  use stack,
        when p[i] < p[i-1], push
        when p[i] > p[i-1], pop and calculate sum


'''

import sys

def trapingWater(height):
    stack = []
    bottom = 0
    bot = None
    sum = 0
    for i in range(len(height)):
        if len(stack) == 0:
            stack.append([i, height[i]])
            continue
        if height[i] <= height[i-1]:
            stack.append([i,height[i]])
            bottom = 0
        else:
            if bottom == 0:
                bot = stack.pop()
                ltop = bot
                bottom = 1

            rtop = height[i]
            while(len(stack) > 0 ):
                sum += (min(stack[len(stack)-1][1], rtop) - bot[1]) * (i-stack[len(stack)-1][0]-1)
                bot = stack[len(stack)-1]
                if stack[len(stack)-1][1] <= rtop:
                    stack.pop()
                else:
                    break

            stack.append([i, height[i]])


    return sum



nums = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# nums = [3,2,1,0,4,2,3,1,5]
print(trapingWater(nums))