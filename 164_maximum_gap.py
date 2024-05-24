'''
164: (medium)

Given an integer array nums, return the maximum difference between two successive elements
in its sorted form. If the array contains less than two elements, return 0.

You must write an algorithm that runs in linear time and uses linear extra space.


Example 1:
Input: nums = [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.

Example 2:
Input: nums = [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.


Constraints:
    1 <= nums.length <= 10^5
    0 <= nums[i] <= 10^9
'''




'''
**********************************************************************
Solution 1: bucket sort
step 1: bucket sort the input nums.
        use a str_list to store intermediate result of each sorting loop
        use a dictionary to process the sorting program

step 2: 

time: O(10n)
space: O(2n)

****************************************************************
Notes: 
for a variable, int->str with fixed length and padded 0:
(1) r = format(str(num), '0nd'),   here 'n' is length, '0' is padding letter.
(2) r = str(num).zfill(n),   here 'n' is length, 

for a list, int list->str list:
(1) str_list = list(map(str, int_list))
(2) str_list = [str(i) for i in int_list]


list + list:
list1 = [1, 2, 3]
list2 = [4, 5, 6]
(1) list1.extend(list2)
    print(list1)  # Output: [1, 2, 3, 4, 5, 6]

(2) concatenated_list = list1 + list2
    print(concatenated_list)  # Output: [1, 2, 3, 4, 5, 6]


if use append(),
    list1.append(list2)
output: [1, 2, 3, [4, 5, 6]]
list2 as one element is added to list1.

'''


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        dict_v = {'0': [], '1': [], '2': [], '3': [], '4': [], '5': [],
                  '6': [], '7': [], '8': [], '9': []}
        str_list = [str(i).zfill(10) for i in nums]

        for d in range(0, 10):
            for cur in str_list:
                num = cur[9 - d]
                dict_v[num].append(cur)

            str_list = []
            for i in range(0, 10):
                k = str(i)
                v = dict_v[k]
                str_list.extend(v)
                dict_v[k] = []

        res_list = [int(j) for j in str_list]
        max_gap = 0
        for j in range(1, len(res_list)):
            if res_list[j] - res_list[j - 1] > max_gap:
                max_gap = res_list[j] - res_list[j - 1]

        return max_gap



