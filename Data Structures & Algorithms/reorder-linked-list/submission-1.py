# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
     
        slow, fast = head , head
        while fast and fast.next:
           slow = slow.next
           fast = fast.next.next
        
        part2 = slow.next
        slow.next = None

        #now reverse the part2 
        prev = None
        curr = part2

        while(curr):
            temp = curr.next
            curr.next = prev
            prev =curr
            curr = temp
        
        while head and prev:
            temp1 = head.next
            temp2 = prev.next
            head.next = prev
            prev.next = temp1
            head = temp1
            prev = temp2
        
        


