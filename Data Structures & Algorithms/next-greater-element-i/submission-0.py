class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        ans = []
        d = {}
        for i in range(len(nums2)-1,-1,-1):
            while stack and nums2[i]>nums2[stack[-1]]:
                stack.pop()

            if stack:
                d[nums2[i]] = nums2[stack[-1]]
            else:
                d[nums2[i]] = -1
            stack.append(i)
        for num in nums1:
            ans.append(d[num])
        return ans