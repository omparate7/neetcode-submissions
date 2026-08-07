class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in nums:
            hashmap[i] = 1+hashmap.get(i,0)

        sortedHashMap = dict(sorted(hashmap.items(), key=lambda x: x[1], reverse=True))
        ans = list(sortedHashMap.keys())[:k]
        return ans

