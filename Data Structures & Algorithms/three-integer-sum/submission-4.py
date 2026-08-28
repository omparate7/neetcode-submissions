class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # another approach using hashmap, see , what we will do is we select an i and for i we select each j after that and see if -nums[i]+nums[j] still exists in the array if yes we will add that truple . so it will O(n2) effectively 

        # but # this approach may introduce duplicates . [1,1,2,2,-3,-3] here i can take 1 in two iterations and j also can take 2 , so we need to avoid all these cases . 
        # fyi two pointer approach complexity = O(n2)
        map = Counter(nums)
        n = len(nums)
        nums.sort()
        ans = list()
        for i in range(n):
            map[nums[i]]-=1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,n):
                map[nums[j]] -=1
                if j>i+1 and nums[j] == nums[j-1]:
                    continue
                #check if target still exists in arr
                target = -(nums[i]+nums[j])
                if map[target]>0:
                    ans.append([nums[i],nums[j],target])
                
            for j in range(i+1,n):
                map[nums[j]]+=1

        return ans   

