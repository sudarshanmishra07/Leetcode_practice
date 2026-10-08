class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        l=0
        u=(m*n)-1
        while l<=u:
            mid = (l+u)//2
            row = mid//n
            col = mid%n
            if matrix[row][col] ==target:
                return True
            else:
                if matrix[row][col]<target:
                    l=mid+1
                else:
                    u=mid-1
        return False
        