class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # appraoch 3: using hash Map , idea is mpp[i] will store length of consecutive sequence that it is part of , now it becomes efficient when for calculating len of num we can simply do mpp[num+1] + mpp[num-1] +1 ; that's the whole core essential logic , that  we can calculate the length of seq associated with a num by merging the seqences just before and after it . and then update the rest of the map ,

        # on updation of map there can be two ways one brute force , that after every insertion we update the whole sequence for which num is the part of , how ???
        mpp = {}
        res = 0
        for i in nums:
            if i not in mpp:
                mpp[i] = 1
                # check for connecting sequences
                if i - 1 in mpp:
                    # if yes ,
                    # find the sequence
                    left = i - 1
                    while left-1 in mpp:
                        left -= 1
                    right = i - 1
                    while right+1  in mpp:
                        right += 1

                    # now [left , right ] is the sequence now , update all elements in seq

                    for i in range(left, right + 1):
                        mpp[i] = right - left +1

                if i + 1 in mpp:
                    left = i + 1
                    while left-1 in mpp:
                        left -= 1
                    right = i + 1
                    while right+1 in mpp:
                        right += 1

                    # now [left , right ] is the sequence now , update all elements in seq

                    for i in range(left, right + 1):
                        mpp[i] = right - left + 1 
                    # similarly same logic as above just in place of  just left,right = i+1 ,i+1

                res = max(res, mpp[i])

        return res
