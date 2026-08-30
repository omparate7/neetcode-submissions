class Solution:
    def trap(self, height: List[int]) -> int:
        # most efficeint 2 pointers approach, O(n) time , const space;
        # key idea : water at i = min(leftMax,rightMax)-height[i]
        # can i know wether leftMax< or > rightMax without knowing the actual value, because any way the answer depends upon minimum of leftMax and rightMax.
        # we will maintain two pointers l and r and left max and right max along. at a position may be l or r by looking at the leftMx and rightMx we can say one thing with certainity . suppose at a position i , leftmax is < rightmax, so one thing is sure we will get water level at most upto leftmax level. because , water level is determined by minimum of the two walls, and now we process the ith position by substracting height[i] from left max and move our pointer to right , now we update out left max, if its still lower do the same if right one is lower than we are certian that there will be atmost rightmax water at pos r and then we calculate and move r to left update right max

        l = 0
        r = len(height) - 1
        leftMax = height[l]
        rightMax = height[r]
        res = 0
        while(l<r):
            
            if leftMax <= rightMax:
                res += leftMax - height[l]
                l+=1
                leftMax = max(leftMax,height[l])
            else:
                res += rightMax - height[r]
                r-=1
                rightMax = max(rightMax,height[r])
                
        return res
