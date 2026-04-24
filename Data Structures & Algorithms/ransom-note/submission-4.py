class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        countR = {}
        countM = {}
        for c in ransomNote:
            countR[c] = countR.get(c, 0) + 1
        for c in magazine:
            countM[c] = countM.get(c, 0) + 1

        for c in countR:
            if c not in countM:
                return False
            if countM[c] < countR[c]:
                return False

        return True