class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
        pairs = {'(': ')', '[': ']', '{': '}'}

        for i in s:
            if i in pairs:
                brackets.append(i)
            else:
                if len(brackets) == 0: return False
                top = brackets.pop()
                if pairs[top] != i:
                    return False

        return len(brackets) == 0