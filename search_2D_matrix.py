class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m=len(matrix)                       #row of matrix
        n=len(matrix[0])                    #column of matrix
        l=0
        u=(m*n)-1
        while l<=u:
            mid = (l+u)//2          
            row = mid//n                    #position in row
            col = mid%n                     #position in column
            if matrix[row][col] ==target:
                return True
            else:
                if matrix[row][col]<target: 
                    l=mid+1                 #set new mid
                else:
                    u=mid-1                 #set new mid
        return False
        