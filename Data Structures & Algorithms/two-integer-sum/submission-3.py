class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {target-nums[i]:i for i in range(len(nums))}
        
        for i in range(len(nums)):
            if nums[i] in hashmap and i!= hashmap[nums[i]]:
            
                return sorted([i,hashmap[nums[i]]])
        
      