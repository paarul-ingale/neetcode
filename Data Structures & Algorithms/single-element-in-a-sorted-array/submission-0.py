class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while right>left:
            mid = left+(right-left)//2
            if mid % 2 == 1:
                if nums[mid]==nums[mid-1]:
                    left = mid+1
                else:
                    right = mid
            else:
                if nums[mid+1] == nums[mid]:
                    left = mid+2
                else:
                    right = mid
        return nums[left]
