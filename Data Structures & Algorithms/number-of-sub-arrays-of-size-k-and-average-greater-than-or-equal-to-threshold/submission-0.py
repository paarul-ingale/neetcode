class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        left = 0
        average = 0
        for right in range (len(arr)):
           
            average += (arr[right]/k)
            if (right - left +1) > k:
                
                average -= (arr[left]/k)
                left+=1
            if (right - left +1)== k:
                if average >= threshold:
                    count+=1
        return count