class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        full_list = []
        for row in matrix:
            full_list.extend(row)
        
        l, r = 0, len(full_list) - 1
        while l <= r:
            mid = (l + r) // 2
            if full_list[mid] == target:
                return True
            elif full_list[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False