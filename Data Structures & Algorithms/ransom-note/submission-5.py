class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = {}
        for c in magazine:
            count[c] = count.get(c, 0) + 1

        for c in ransomNote:
            if count.get(c, 0) > 0:
                count[c] -= 1
            else:
                return False
        return True