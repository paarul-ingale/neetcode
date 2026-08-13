class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cur_max = 0
        ans = 0
        for i in range(0 ,len(nums)):
            if nums[i]==1:
                cur_max +=1
            else:
                ans= max(ans,cur_max)
                cur_max = 0
        return max(ans,cur_max)