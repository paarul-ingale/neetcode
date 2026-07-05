class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for no in nums:
            if no in d:
                return True
            else:
                d[no]=1
        return False