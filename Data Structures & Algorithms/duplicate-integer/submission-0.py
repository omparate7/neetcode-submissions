class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = Counter(nums)
        for key,val in counts.items():
            if val > 1:
                return True
        return False
            