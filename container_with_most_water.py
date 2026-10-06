class Solution:
    def maxArea(self, heights: List[int]) -> int:
        height = 0
        #initialise left and right pointer
        l=0
        r=len(heights)-1
        max_area = 0
        while l < r:                                       #continue until both pointer meet
            new_height = min(heights[l], heights[r])
            width = r - l
            current_area = new_height*width                #calculat area of current container
            max_area= max([max_area,current_area])         #update maximum area
            if heights[l] < heights[r]:                    #move pointer pointing to the shorter line
                l+=1
            else:
                r-=1
        return max_area                                    #return maximum area found