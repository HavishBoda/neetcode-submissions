class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carPosition = {}
        res = 1

        for i, pos in enumerate(position):
            carPosition[i] = pos

        times = [0] * len(position)

        for i, sp in enumerate(speed):
            time = ((target - carPosition[i]))/sp
            times[i] = (carPosition[i], time)
        
        times.sort()

        fleet_time = times[-1][1]
        for i in range(len(times)-1, -1, -1):
            if times[i][1] > fleet_time:
                res += 1
                fleet_time = times[i][1]
        
        return res


