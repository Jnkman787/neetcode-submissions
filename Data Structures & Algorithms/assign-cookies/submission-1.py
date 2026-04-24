class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)

        i, j = 0, 0

        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                j += 1
            i += 1
            if i == len(g):
                break

        return j