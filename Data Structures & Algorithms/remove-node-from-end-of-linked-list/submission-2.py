# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        length = 0 
        curr = head
        while(curr):
            curr=curr.next
            length+=1

        curr = head
        for _ in range(length-n-1):
            curr=curr.next
        #2 edge cases 
        #1. n=1 , and l = 1 , deleting the only element
        #2. n=n deleting the first element

        if(length == n):  #this will handle both cases
            return head.next
        else:
            temp = curr.next
            curr.next = curr.next.next
            temp.next = None
        

        return head

        