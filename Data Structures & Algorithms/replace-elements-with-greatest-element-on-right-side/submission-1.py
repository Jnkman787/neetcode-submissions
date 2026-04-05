class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) > 1:
            originalArr = arr[:]
            for i in range(len(originalArr[:-1])):
                arr[i] = max(originalArr[i + 1:])
        arr[-1] = -1
        return arr