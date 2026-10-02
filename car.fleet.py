class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = sorted(zip(position, speed),reverse = True)
        stack = []
        for pos, spd in cars:
            time = (target - pos) / spd

            # If current car cannot catch the fleet ahead
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)