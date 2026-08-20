class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # trivial approach is summation of all elements - n*n+1 /2 that will give ans , but that consumes lot of computation in summation 

        # another method is using set seen, just keep on adding if found in seen return number 

        # another in the same auxilary space bucket is using hash map 

        # another approach is sorting 

        # apporach 5: Negative Marking, idea is as we go along the arr we change the sign to negative , and  as there is only 2 duplicates that means two number point to the same index and we can identify that as when we go to that index's number that will happen to be already negative 

        # approach 6: Binary Search On Answer
        # here we search in space[1,n] and will find mid and keep on eliminating the half . based on mid
        # How???? actually for mid we will count how many elements are less than or equal to mid in orignal array , if it is greater than mid then ignore the right half duplicate exists in [1,mid] range , if its equal to mid then duplicate exist in other half that is [mid,n] the apprach will take O(n*logn) time , 


        low = 0 
        high = len(nums)-1
        while(high>=low):
            mid =( low + high )//2
            def count(n):
                c = 0
                for i in nums:
                    if i<=n:
                        c+=1
                return c
            if(count(mid)<= mid):
                low = mid+1
            else:
                high = mid-1
        
        return low 
            



        


        