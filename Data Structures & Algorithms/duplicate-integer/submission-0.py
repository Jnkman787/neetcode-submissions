class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        thin = set(nums)
        if len(thin) == len(nums):
            return False
        return True