class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # approach 1 : straight forward and naive , take all product in one pass and in second pass divide the ith number with prod . 
        prod = 1
        ans = list()
        zcount = 0
        for i in nums:
            if i!=0:
                prod *= i
            else: 
                zcount+=1
            
        if zcount > 1 :
            return [0]*len(nums)

        for i in nums:
            if i != 0 and zcount:
                ans.append(0) 
            elif i!= 0 :
                ans.append(prod//i)
            else:
                ans.append(prod)
        return ans
        