class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        hours = 0
        left = 1
        right = sum(piles)
        mid = -1
        while right-left>=0:
            hours=0
            mid = left+(right-left)//2
            for i in range(0,len(piles)):
                hours+=math.ceil(piles[i]/mid)
            if hours<=h:
                right=mid-1
            elif hours>h:
                left=mid+1
        return left
            