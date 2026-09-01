# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        
        group = 0
        curr = head

        while group < k and curr:
            curr = curr.next
            group+=1

        if group == k:

            curr = self.reverseKGroup(curr,k)
            while group:
                next = head.next
                head.next = curr
                curr = head
                head = next
                group-=1
            head = curr
        

        
        return head