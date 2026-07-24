class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol=[]
        for k in range (0,len(nums)):
            rem = 0-nums[k]
            i=k+1
            j=len(nums)-1
            while i<j:
                if nums[j]+nums[i]>rem:
                    j-=1
                elif nums[j]+nums[i]<rem:
                    i+=1
                elif i==j==k:
                    continue 
                elif nums[j]+nums[i]==rem:
                    if [nums[k], nums[i], nums[j]] not in sol:
                        sol.append([nums[k], nums[i], nums[j]])
                    i+=1
                    j-=1
                else:
                    continue 
        return sol