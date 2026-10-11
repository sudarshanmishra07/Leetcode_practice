from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i,t in enumerate(temperatures):         #traverse temperature
            while stack and t > stack[-1][0]:
                prev_t, prev_i = stack.pop()        #remove previous day
                result[prev_i] = i - prev_i         #calculate waiting days

            stack.append([t,i])                     #push current days
        return result                               #return result