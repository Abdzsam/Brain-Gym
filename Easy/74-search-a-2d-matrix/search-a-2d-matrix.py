class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix) - 1
        theOne = 0

        while low <= high:
            mid = (low + high) // 2

            if  matrix[mid][0] == target:
                return True

            if matrix[mid][0] <= target and target <= matrix[mid][-1]:
                theOne = mid
                break

            elif matrix[mid][0] < target and matrix[mid][-1] < target:
                low = mid + 1

            elif matrix[mid][0] > target and matrix[mid][-1] > target:
                high = mid - 1

        lowIn = 0
        highIn = len(matrix[0]) - 1

        while lowIn <= highIn:
            mid = (lowIn + highIn) // 2

            if matrix[theOne][mid] == target:
                return True
            
            elif matrix[theOne][mid] < target:
                lowIn = mid + 1

            else:
                highIn = mid - 1

        return False
