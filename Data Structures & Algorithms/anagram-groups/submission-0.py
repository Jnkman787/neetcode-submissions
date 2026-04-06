class Solution:
    def createDictionary(self, word, count):
        for char in word:
            if char not in count:
                count[char] = 1
            else:
                count[char] += 1
        return count

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []

        for word in strs:
            if len(groups) == 0:
                groups.append([word])
                continue

            wordAnagram = self.createDictionary(word, {})
            added = False
            for group in groups:
                groupAnagram = self.createDictionary(group[0], {})
                if wordAnagram == groupAnagram:
                    group.append(word)
                    added = True
                    continue

            if added == False:
                groups.append([word])

        return groups