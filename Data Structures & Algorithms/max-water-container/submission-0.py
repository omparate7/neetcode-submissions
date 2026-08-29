class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #brute force 
        #for every pair i,j  area is min(nums[i],nums[j])*j-i
        # we can# run 2 loops for every i , j{from i+1} and keep track of maximum area that .

        # hint , if we keep twopointer on ends l and r it convers the maximum length , but now which pointer to move and based on what 

        # got an idea , if we see whose height is more l or r then whose height is more we will fix that and move the smaller one forwrd . 

        l = 0
        r = len(heights)-1
        maxArea = 0
        while(r>l):
            area = min(heights[l],heights[r])*(r-l)
            maxArea = max(area,maxArea)
            if heights[l]==heights[r]:
                l+=1
                r-=1
            elif heights[l]>heights[r]:
                r-=1
            else:
                l+=1
            # what if if equal heights then moving on either side will result in area loss after one step only we can decide , if hight greater than previous appears we will fix that and move the other end . 
            # so , why not do it first hand we can move both ponters at the same time without missing any max area because its already recorded.
        return maxArea

         