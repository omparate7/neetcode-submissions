class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = Counter(s)
        count2 = Counter(t)

        if len(s) != len(t):
            return False

        return count1 == count2
        