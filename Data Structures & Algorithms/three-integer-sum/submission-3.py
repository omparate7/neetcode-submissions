class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # approach 1: simple , O(n3)
        # approach 2: two pointer # tricky part is how to avoid duplicatess . here are two cases you need to think, first is after finding one triplet for i , we do normally i++, but if nums[i] = nums[i-1] after i++ , then we are searching the same space essentially .
        #2nd if , after finding a triplet we do l++ r-- but its possible that are the same numbers like -2,0,0,2,2 so we need to shift our l and r pointers untill they point to diffrent element. 
        nums.sort()
        ans = list()
        n = len(nums)

        for i in range(n - 2):
            # for each i apply l , r two pointer approach
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l = i + 1
            r = n - 1

            while l < r:
                if nums[l] + nums[r] == -nums[i]:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < n and nums[l] == nums[l-1]:
                        l+=1
                    while r > 0 and nums[r] == nums[r+1]:
                        r-=1

                elif nums[l] + nums[r] < -nums[i]:
                    l += 1
                else:
                    r -= 1

        return ans
