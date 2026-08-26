class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = 0
        summ=nums[0]
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                summ+=nums[i]
            else:
                max_sum = max(summ,max_sum)
                summ = nums[i]
        return max(max_sum,summ)