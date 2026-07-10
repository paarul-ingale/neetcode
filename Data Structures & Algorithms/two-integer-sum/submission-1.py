class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans={}
        for i in range (0 , len(nums)):
            ans[nums[i]] = i
        for i in range (0 , len(nums)):
            compliment = target - nums[i]
            if compliment in ans:
                if i != ans[compliment]:
                    return [i , ans[compliment]]