class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 0
        right = n*(n+1)/2
        while left <= right:
            mid = int(left+(right-left)/2)
            if n>(mid*(mid+1))/2:
                left = mid+1
            elif n<mid*(mid+1)/2:
                right = mid-1
            elif n ==mid*(mid+1)/2:
                return left
        return left-1