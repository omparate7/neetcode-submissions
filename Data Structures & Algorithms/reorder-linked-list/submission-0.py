# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def recursion(self,curr,n):
        if n <= 0:
            curr.next = None
            return
        len=n
        temp = curr.next
        it = curr
        while(n):
            it = it.next
            n-=1
        curr.next = it
        it.next = temp

        # self.recursion(temp,n-2) yaha pe there is a mistake , after while loop n becomes 0 . you have to store the len
        self.recursion(temp,len-2)

        

    def reorderList(self, head: Optional[ListNode]) -> None:
        length = 0
        dummy = head
        while dummy:
            length+=1
            dummy = dummy.next
        self.recursion(head,length-1)
        
        