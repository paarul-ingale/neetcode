class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = [0]*n
        max_n = 0
        for i in range( n-1 , -1 ,-1):
            ans[i] = max_n
            if arr[i]>max_n:
                max_n = arr[i]
            
        ans[n-1] = -1
        return ans