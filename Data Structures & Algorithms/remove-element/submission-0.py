class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        good = []
        for i in nums:
            if i != val:
                good.append(i)
        for i in range(len(good)):
            nums[i] = good[i]
        return len(good)