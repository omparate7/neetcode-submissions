class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # number of approaches to solve this q

        #approach 1 : Brute force , O(n2) , use two loops thas it find target-ind1
        #approach 2 : use a map , like target-nums[i] : i . and you can do it in one pass , for each element , check in map if exists return i,j if not insert {target-nums[i],i} to map move to next , this will take care of i,i case .
        # approach 3: two pointers since it's sorted we can use low and high and if low + high > target high-1 and wise versa .


        low = 0 
        high = len(numbers)-1

        while(high > low):
            if numbers[low]+numbers[high] > target:
                high-=1
            elif numbers[low]+numbers[high] < target:
                low+=1
            else:
                break
        return [low+1,high+1]
        #approach 3 : the array is sorted , so another approach pops in that is bs , since search space is monotonic ; 


        