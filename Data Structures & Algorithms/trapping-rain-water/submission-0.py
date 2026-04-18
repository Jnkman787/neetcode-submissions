class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        prefix = []
        suffix = []

        for i in range(len(height)):
            if i == 0:
                prefix.append(height[i])
                suffix.append(height[-1])
            else:
                prefix.append(max(prefix[-1], height[i]))
                suffix.insert(0, max(suffix[0], height[-1 - i]))
        
        for i in range(len(height)):
            water += min(prefix[i], suffix[i]) - height[i]

        return water