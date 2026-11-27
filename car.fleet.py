class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = sorted(zip(position, speed),reverse = True)
        stack = []
        for pos, spd in cars:                   #traverse car from front to back
            time = (target - pos) / spd

            if not stack or time > stack[-1]:   # If current car cannot catch the fleet ahead
                stack.append(time)
        return len(stack)                       #no. of fleets is equal to size of stack