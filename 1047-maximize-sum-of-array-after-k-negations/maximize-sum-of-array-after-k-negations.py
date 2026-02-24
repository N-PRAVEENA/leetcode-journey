class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        for i in range(k):
            nums = sorted(nums)
            nums[0] = -nums[0]

        return sum(nums)