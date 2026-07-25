class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        j = 2
        while j >0:
            for i in range(0 , len(nums)):
                    ans.append(nums[i])
            j-=1
        return ans