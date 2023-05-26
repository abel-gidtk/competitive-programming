class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        def sum(arr):
            sum = 0
            for elem in arr:
                sum += elem
            return sum

        return sum(range(len(nums)+1)) - sum(nums)
