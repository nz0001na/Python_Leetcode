class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        array = {}
        result = []

        for i in range(len(nums)):
            k = nums[i]
            v = i
            m = target - k
            if m in array.keys():
                result.append(i)
                result.append(array[m])
                break
            else:
                array[k] = v

        return result

            

        
        