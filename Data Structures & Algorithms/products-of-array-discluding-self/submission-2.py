class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix,suffix,res = [1]*(n),[1]*(n),[1]*(n)
        
        for i in range(n):
            if i == 0 :
                prefix[i] = nums[i]
                continue
            prefix[i] = prefix[i-1]*nums[i]
        
        for i in range(n-1,0,-1):
            if i == n-1:
                suffix[i] = nums[i]
                continue
            suffix[i] = suffix[i+1]*nums[i]

        for i in range(n):
            if i == 0 :
                res[i] = suffix[i+1]
            elif i == n-1:
                res[i] = prefix[i-1]
            else:
                res[i] = prefix[i-1]*suffix[i+1]

        return res
        
