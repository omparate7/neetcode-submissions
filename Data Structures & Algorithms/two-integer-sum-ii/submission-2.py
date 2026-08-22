class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # number of approaches to solve this q

        #approach 1 : Brute force , O(n2) , use two loops thas it find target-ind1
        #approach 2 : use a map , like target-nums[i] : i . and you can do it in one pass , for each element , check in map if exists return i,j if not insert {target-nums[i],i} to map move to next , this will take care of i,i case .
        # approach 3: two pointers since it's sorted we can use low and high and if low + high > target high-1 and wise versa .

        #approach 4 : the array is sorted , so another approach pops in that is bs , since search space is monotonic ; 
        
        # simple # for each nums[i] we will do bs on other half finding target-nums[i] 
        n = len(numbers)
        for i in range(n):
            
            def bs(target):
                low = i+1
                high = n-1
                while(high >= low):
                    mid = (high+low)//2
                    if(numbers[mid] > target):
                        high=mid-1
                    elif(numbers[mid] < target):
                        low = mid+1
                    else:
                        return mid
                return -1
            j = bs(target-numbers[i])
            if j != -1:
                return [i+1,j+1]
            
        
            
             


        