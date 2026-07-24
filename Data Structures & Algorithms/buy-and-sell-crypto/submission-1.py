class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        j = 0
        for i in range (0 , len(prices)):
            while i - j>0:
                if prices[i] > prices[j]:
                    if max < prices[i]-prices[j]:
                        max = prices[i]-prices[j]
                    j+=1
                else:
                    j+=1
            j = 0
        return max