class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n;
        j = n -1

        for i in range (0 , (n//2)):
            
            nums[i], nums[j] = nums[j], nums[i]
            j-=1

        j = n-1    
        for i in range (k, (n + k)//2):
            nums[i], nums[j] = nums[j], nums[i]
            j-=1

        last = k-1
        for i in range (0,k//2):
            nums[i], nums[last] = nums[last], nums[i]
            last-=1