class Solution:
    def calculateScore(self, a: int, b: int) -> int:
        binary_numberA = bin(a)[2:]         #int to binary conversion
        binary_numberB = bin(b)[2:]
        count_A = binary_numberA.count("1") #count number of 1s in binary_numberA
        count_B = binary_numberB.count("1") #count number of 1s in binary_numberB
        print(count_A),print(count_B)
        if count_A>=count_B:                
            return count_A*count_B          #return count_A*count_B
        else:
            if count_A==0:                  #for edge case
                return invalid
            else:
                return count_B//count_A     #return count_B//count_A
            