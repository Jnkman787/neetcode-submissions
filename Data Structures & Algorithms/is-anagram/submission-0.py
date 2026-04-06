class Solution:
    def fillDictionary(self, word, count):
        for char in word:
            if char not in count:
                count[char] = 1
            else:
                count[char] += 1
    
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = {}
        count2 = {}
        self.fillDictionary(s, count1)
        self.fillDictionary(t, count2)

        if count1 == count2:
            return True
        return False