# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # Approach 3 : recursion, idea is to keep track while unwinding0

        # using recursion stack to cout from last node

        def rec(last):
            
            if last == None:
                return 0
            
            count = rec(last.next)

            if n == count:
                last.next = last.next.next
                

            
            return 1+count

        c = rec(head)
        if(c == n): 
            return head.next
        return head
            

            
