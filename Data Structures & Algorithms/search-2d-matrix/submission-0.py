class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if not matrix or not matrix[0]:
            return False

        t, b = 0, len(matrix) - 1

        while t <= b:
            midRow = (t + b) // 2

            if target < matrix[midRow][0]:
                b = midRow - 1
            elif target > matrix[midRow][-1]:
                t = midRow + 1
            else:
                break  

        if not (t <= b):
            return False

  
        row = (t + b) // 2
        l, r = 0, len(matrix[0]) - 1

        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False
        
                
