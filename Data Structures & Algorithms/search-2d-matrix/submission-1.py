class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = -1
        left = 0
        right = len(matrix)-1
        while right-left>=0:
            mid =(left+(right-left)//2)
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                i = mid
                break
            elif matrix[mid][0]>target:
                right = mid-1
            elif matrix[mid][0]<target:
                left = mid+1
            
            else:
                return False
            
        left = 0
        right = len(matrix[i])-1
        while right - left >=0:
            mid =(left+(right-left)//2)
            if matrix[i][mid]>target:
                right = mid-1
            elif matrix[i][mid]<target:
                left =mid+1
            elif matrix[i][mid]==target:
                return True
        return False
