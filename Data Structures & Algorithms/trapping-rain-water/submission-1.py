class Solution:
    def trap(self, height: List[int]) -> int:
        # the main core is , water trapped at ith height = min(leftmax,rightmax) - height[i]
        # space optimisation ;intead of storing all left and right we can calculate them on the go 
        #  for i in range(n):
            # leftMax = rightMax = height[i]

            # for j in range(i):
            #     leftMax = max(leftMax, height[j])
            # for j in range(i + 1, n):
            #     rightMax = max(rightMax, height[j])

            # but that will increase time complexity to O(n2).
            # yo


        left = [0]*len(height)
        right = [0]*len(height)
        if len(height)<=2:
            return 0
        for i in range(1,len(height)):
            if height[i-1] > left[i-1]:
                left[i]=height[i-1]
            else:
                left[i]=left[i-1]
        for i in range(len(height)-2,-1,-1):
            if height[i+1] > right[i+1]:
                right[i]=height[i+1]
            else:
                right[i]=right[i+1]
        maxWater = 0
        for i in range(0,len(height)):
            maxWater += max(0,min(left[i],right[i])-height[i])
        return maxWater
        

