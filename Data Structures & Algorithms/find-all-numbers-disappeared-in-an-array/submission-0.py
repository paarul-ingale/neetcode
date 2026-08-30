class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ref = []
        for i in range(len(nums)):
            ref.append(i + 1)
        nums.sort()
        ans = []
        i = 0
        j = 0
        while i < len(ref) and j < len(nums):
            if ref[i] == nums[j]:
                i += 1
                j += 1
            elif ref[i] < nums[j]:
                ans.append(ref[i])
                i += 1
            else:
                j += 1
        while i < len(ref):
            ans.append(ref[i])
            i += 1

        return ans