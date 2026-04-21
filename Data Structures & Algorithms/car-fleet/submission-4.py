class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = sorted(zip(position, speed), reverse = True)

        for i in range(len(cars)):
            time = (target - cars[i][0]) / cars[i][1]
            if i == 0 or time > stack[-1]:
                stack.append(time)
        return len(stack)