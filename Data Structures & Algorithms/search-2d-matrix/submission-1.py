class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = matrix[0]
        for rows in matrix[1:]:
            if rows[0] <= target:
                row = rows
        
        l, r = 0, len(row) - 1
        while l <= r:
            mid = (l + r) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False