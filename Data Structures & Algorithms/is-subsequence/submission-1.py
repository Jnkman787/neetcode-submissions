class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        temp = ""
        for c in t:
            if temp == s:
                return True
            if c == s[len(temp)]:
                temp += c
        if temp == s:
            return True
        return False