class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 1
        right = num
        while right>=left:
            mid = left+(right-left)//2
            if mid*mid==num:
                return True
            elif mid*mid>num:
                right = mid-1
            elif mid*mid<num:
                left = mid+1
        return False