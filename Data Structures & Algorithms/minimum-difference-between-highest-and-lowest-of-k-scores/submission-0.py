class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        j = 0
        min_d = float('inf')
        for i in range (k-1 , n):
            min_d = min((nums[i] - nums[j]) , min_d)
            j+=1
        return min_d