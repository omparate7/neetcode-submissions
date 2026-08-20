class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # trivial approach is summation of all elements - n*n+1 /2 that will give ans , but that consumes lot of computation in summation 

        # another method is using set seen, just keep on adding if found in seen return number 

        # another in the same auxilary space bucket is using hash map 

        # another approach is sorting 

        # apporach 5: Negative Marking, idea is as we go along the arr we change the sign to negative , and  as there is only 2 duplicates that means two number point to the same index and we can identify that as when we go to that index's number that will happen to be already negative 


        for i in range(len(nums)):
            if nums[abs(nums[i])] < 0 :
                return abs(nums[i]) 
            else:
                nums[abs(nums[i])]*=-1



        


        