class Solution:
    def searchMatrix(matrix, target):
        num_rows, num_cols = len(matrix), len(matrix[0])
        left, right = 0, num_rows * num_cols - 1

        while left <= right:
            mid = (left + right) // 2
            row, col = mid // num_cols, mid % num_cols
            value = matrix[row][col]

            if value > target:
                right = mid - 1
            elif value < target:
                left = mid + 1
            else:
                return True
        return False