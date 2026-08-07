class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        for i in nums:
            hashmap[i] += 1

        sortedHashMap = dict(sorted(hashmap.items(), key=lambda x: x[1], reverse=True))
        ans = list(sortedHashMap.keys())[:k]
        return ans

