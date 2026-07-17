class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output = []
        n = len(nums)
        right = [0] * n
        left_product = 1

        right[n - 1] = 1
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        for i in range(n):
            output.append(left_product * right[i])
            left_product = left_product* nums[i]

        return output
