class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        left, right = 0, len(heights) - 1
        while left < right:
            water = (right - left) * min(heights[left], heights[right])
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
            maxWater = max(maxWater, water)
        return maxWater