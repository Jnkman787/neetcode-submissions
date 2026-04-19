class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        counts = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                stack_t, stack_i = stack.pop()
                counts[stack_i] = i - stack_i
            
            stack.append((t, i))
        
        return counts