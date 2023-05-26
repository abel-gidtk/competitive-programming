class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in hashtable:
                return [i, hashtable[difference]]
            hashtable[nums[i]] = i
