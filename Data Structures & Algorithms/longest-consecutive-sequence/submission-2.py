class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        k=1
        count = 0
        if not nums:
            return 0
        for i in range (0 , len(nums)-1):
            if  nums[i+1]== nums[i]+1:
                k+=1
            elif nums[i+1]== nums[i]:
                continue
            else:
                if count < k:
                    count = k
                k=1
        count = max(k,count)
        return count