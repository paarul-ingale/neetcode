class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_v = prices[0]
        left = 0
        max_p = 0
        for right in range(0,len(prices)):
            max_p = max(max_p , (prices[right] - min_v))
            left+=1
            min_v = min(min_v , prices[right])
        return max_p