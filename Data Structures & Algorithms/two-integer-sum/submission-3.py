class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans={}

        for i in range (0 , len(nums)):
            compliment = target - nums[i]
            if compliment in ans and i != ans[compliment]:
                return [ans[compliment] , i]
            ans[nums[i]] = i