class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        maxCount = 0
        count = 0

        for i in range(len(nums)):
            if i == 0 or nums[i] - nums[i - 1] == 1:
                count += 1
            elif nums[i] == nums[i - 1]:
                continue
            else:
                count = 1
            
            maxCount = max(maxCount, count)

        return maxCount