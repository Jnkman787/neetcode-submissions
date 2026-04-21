class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        num_fleets = 0
        times = []

        sorted_s = [val for _, val in sorted(zip(position, speed))][::-1]
        sorted_p = sorted(position)[::-1]

        for i in range(len(sorted_p)):
            time = (target - sorted_p[i]) / sorted_s[i]
            if i == 0 or time > max(times):
                num_fleets += 1
            times.append(time)
        return num_fleets