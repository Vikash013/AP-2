class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        summ = nums[0]
        max_sum = summ
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                summ += nums[i]
            else:
                summ = nums[i]
            max_sum = max(max_sum, summ)
        return max_sum
