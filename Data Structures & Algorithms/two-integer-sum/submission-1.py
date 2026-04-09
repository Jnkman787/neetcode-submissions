class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        history = {}
        for i, v in enumerate(nums):
            difference = target - v
            if difference in history:
                return [history[difference], i]
            history[v] = i