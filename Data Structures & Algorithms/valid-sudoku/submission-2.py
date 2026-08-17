class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # approach 3: BitMasking 
        # what is it ? -> we represent complex states inform of bitstream , it's like a space efficient version of hashing , 
        #we assign each bit position for specific symbol and the mask can represent the currenct state , 
        #here , for each row , col , square we have a 9bit bit mask , ith bit rep wether i+1th number is present or not , 
        # so space complexity , O(9*3) 27 units of memory that's it fix for all no dependency of n

        # how to make a mask of a digit , simple left operation << 
        # how to update state mask , simple || operation 
        #how to check the state mask , simple && operation


        # initialising 
        rows = [0]*9
        cols = [0]*9
        squares = [0]*9

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                mask = 1 << int(board[i][j])
                if ( rows[i] & mask != 0 or cols[j] & mask != 0 or squares[(i//3 * 3 )+ j // 3] & mask != 0):
                    return False

                rows[i]|=mask
                cols[j]|=mask
                squares[(i//3 * 3)+j//3] |= mask 

        return True
