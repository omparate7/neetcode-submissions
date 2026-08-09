class Solution:
    def encode(self, strs: List[str]) -> str:
        e = ""
        for s in strs:
            e = e + str(len(s)) + "#" + s 
        return e

    def decode(self, s: str) -> List[str]:
        strs = list()
        i = 0
        while i < len(s):
            # find how long is char, that is number in the start of the string before '#'
            j=i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            start = j + 1
            strs.append(s[start : start + length])

            i = start + length
        return strs
