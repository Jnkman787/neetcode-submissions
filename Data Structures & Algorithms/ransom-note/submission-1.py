class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote = ''.join(sorted(list(ransomNote)))
        magazine = ''.join(sorted(list(magazine)))
        
        i = 0
        j = 0

        while i < len(ransomNote) and j < len(magazine):
            if ransomNote[i] == magazine[j]:
                i += 1
            j += 1
        return i == len(ransomNote)