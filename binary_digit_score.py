class Solution:
    def calculateScore(self, a: int, b: int) -> int:
        binary_numberA = bin(a)[2:]
        binary_numberB = bin(b)[2:]
        count_A = binary_numberA.count("1")
        count_B = binary_numberB.count("1")
        print(count_A),print(count_B)
        if count_A>=count_B:
            return count_A*count_B
        else:
            if count_A==0:
                return invalid
            else:
                return count_B//count_A
            