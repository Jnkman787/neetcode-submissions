class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                brackets.append(i)
            else:
                if len(brackets) == 0: return False
                if i == ')':
                    if brackets[-1] == '(':
                        brackets.pop()
                    else:
                        return False
                elif i == ']':
                    if brackets[-1] == '[':
                        brackets.pop()
                    else:
                        return False
                else:
                    if brackets[-1] == '{':
                        brackets.pop()
                    else:
                        return False
        
        if len(brackets) == 0: return True
        return False