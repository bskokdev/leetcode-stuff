class Solution:
    def find_row_with_target(self, matrix: List[List[int]], target: int) -> int:
        if not matrix: return False
        top, bot = 0, len(matrix)-1
        while top <= bot:
            mid = (top + bot) // 2
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bot = mid - 1
            else:
                return (top+bot)//2
        return -1

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False
        rows, cols = len(matrix), len(matrix[0])
        # get the row where target should be
        row = self.find_row_with_target(matrix, target)
        left, right = 0, cols-1
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True
            elif target > matrix[row][mid]:
                left = mid + 1
            else:
                right = mid - 1
        return False
            
        