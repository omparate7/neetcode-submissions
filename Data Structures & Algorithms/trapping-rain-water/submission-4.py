class Solution:
    def trap(self, height: List[int]) -> int:
        # approach 3 :stack
        # we do not need 2n aux space i mean pref and suffix , there can be another implementation , like just storing rightMax for each position because left max we can calculate while traversing . 
        # there can be one more implementation using stack
        # where we only keep track of lefts untill we encounter the right wall . when we find a right wall we will process all the lefts which are valid untill the right wall disappears . 

        # what is specifically means is , maintain a monotonic decreasing stack . and untill stack top < height[i] then pop and calculate the water stored. 
        stack = [] # stack of indices , why?? becoz for calculating width
        res = 0
        n = len(height)
        for i in range(n):

            while len(stack)!=0 and height[stack[-1]] < height[i]:
                bottom = height[stack.pop()]
                # if no left wall exists then break;
                if not stack :
                    break
                leftwall = height[stack[-1]] 
                level = min(leftwall,height[i])-bottom
                width = i - stack[-1] -1
                res += width*level
            
            stack.append(i)
        return res
        


