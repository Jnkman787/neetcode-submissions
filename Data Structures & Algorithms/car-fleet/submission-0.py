class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(x, v) for x, v in zip(position, speed)]
        cars = sorted(cars)

        fleet = 1
        x, v = cars.pop()
        prevTime = (target-x)/v
        
        while cars:
            x, v = cars.pop()
            time = (target-x)/v
            if time > prevTime:
                fleet += 1
                prevTime = time

        return fleet