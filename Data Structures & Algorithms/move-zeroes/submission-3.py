class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n =len(nums)
        j = -1
        for ind in range (0 , n):
            if nums[ind]== 0:
                j = ind
                break
        if j!= -1:
            for i in range (j+1 , n):
                if nums[i]!=0:
                    nums[i] , nums[j] = nums[j] ,nums[i]
                    j+=1
                else:
                    pass       