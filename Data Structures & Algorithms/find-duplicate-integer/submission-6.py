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


        #approach 7: Bit Manupulation
        # xor = 0
        # for i in range(1,len(nums)):
        #     xor ^= i
        # for i in nums:
        #     xor ^= i
        # return xor

        # the above approach has a problem , in question they have given there is only one number that duplicates but , it is not sure that the number only comes twice in the array it can be [3,3,3,3,3] nums[i ] range is [1,4 ] and 3 is in range and it is duplicating 

        # correct approach using bit manupulation;
        #simple you count ocuurance of each bit in [1,n] let say x and in nums let say y . now if both x and y are same that means the number which is duplicated doesn't contain that set bit .  if x<y then that bit is set more than expected so we remember that bit . how ?? by maintaining a res . res|=mask

       # approach 8: fast and slow pointer , LL

       #consider the arr like a ll where nums[i] tells you the next pointer , now if we plot the ll , then it will look like some cycle is being formed anywhre between 1 to n , because two nodes points to the same next node and we can use fast and slow pointer approach to detect the cycle but how we are gonna find the number which is causing so 

       # the answer is not quite intuitive, after finding the first meeting point , we sent slow to the start of nums and keep fast as it is , and then slow+=1 fast+=1 , the 2nd meeting point is the entrance of cycle , why because after deriving distance between meeting point entrance and start there is a relation ship that is dist(start to entrance) = distance (meeting point to entrance) + some number of cycles . 

    #    so  sending slow at start , makes distance for slow and fast till the entrance the same and hence they meet exactly at the entrance.

        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast :
                break

        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow            



        


        