class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # what if we can find a way to locate the start of the sequence 
        #then we can just add +1 to it and check in the hash set if its there or not;

        #a start of a sequence is what , a number n s.t. n-1 doesn't exist . 

        #fyi , naive appraoch will be to just sort the arr and start counting from first 

        stt = set(nums)
        ans = 0
        for i in nums:
            if(i-1 not in stt):
                j = i
                count = 0
                while(j in stt):
                    count+=1
                    j+=1
                ans = max(ans,count)
            
        return ans

