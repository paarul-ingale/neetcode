class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for i in range(len(nums)):
            d[nums[i]]= d.get(nums[i],0)+ 1
        for key , values in d.items():
            if values > len(nums)/2:
                return key
        
        return -1