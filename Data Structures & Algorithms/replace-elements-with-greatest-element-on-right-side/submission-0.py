class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(0 , len(arr)-1):
            rem = []
            for j in range( i+1 , len(arr)):
                rem.append(arr[j])
            arr[i] = max(rem)
        arr[len(arr)-1] = -1
        return arr