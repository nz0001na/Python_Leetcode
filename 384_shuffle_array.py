'''
384. Shuffle an Array
Medium

https://www.geeksforgeeks.org/python-ways-to-shuffle-a-list/
https://www.geeksforgeeks.org/shuffle-a-given-array-using-fisher-yates-shuffle-algorithm/
https://www.cnblogs.com/grandyang/p/5783392.html

Shuffle a set of numbers without duplicates.

Example:
// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();

'''


class Solution:

    def __init__(self, nums):
        self.nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        """
        print(self.nums)
        return self.nums

    # Shuffle a given array using Fisher–Yates shuffle Algorithm
    def shuffle(self):
        """
        Returns a random shuffling of the array.
        """
        res = self.nums
        cnt = len(res)
        if cnt <= 1:
            return res
        import random
        for i in range(cnt-1, 0, -1):
            j = random.randint(0,i)
            res[i], res[j] = res[j], res[i]
        print(res)



# Your Solution object will be instantiated and called as such:
nums = [1, 2, 3]
obj = Solution(nums)
param_1 = obj.reset()
param_2 = obj.shuffle()