class Solution:
    def eucl_dis(self, p):
        return p[0] ** 2 + p[1] ** 2

    def quick_sort(self, points):
        if len(points) <= 1:
            return points
        
        pivot_dist = self.eucl_dis(points[0])
        left = [x for x in points[1:] if self.eucl_dis(x) < pivot_dist]
        right = [x for x in points[1:] if self.eucl_dis(x) >= pivot_dist]
        return self.quick_sort(left) + [points[0]] + self.quick_sort(right)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = self.quick_sort(points)
        return points[:k]