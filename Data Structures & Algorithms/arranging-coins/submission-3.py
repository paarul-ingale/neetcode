class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        add = 0
        arr = []
        while add <= n :
            add+=i
            i+=1
            arr.append(add)
        left = 0
        right = len(arr)-1
        while left <= right:
            mid = int(left+(right-left)/2)
            if n>arr[mid]:
                left = mid+1
            elif n<arr[mid]:
                right = mid-1
            elif n ==arr[mid]:
                return left+1
        return left
        
