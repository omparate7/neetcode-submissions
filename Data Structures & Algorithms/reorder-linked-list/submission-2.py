# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # recursive solution


        def rec(first , last):
            if last == None:
                return first
            
            first = rec(first,last.next)
            if not first:
                return None
                
            temp = None
            if first == last or first.next == last:
                last.next = None
            else:
                temp = first.next
                first.next = last
                last.next = temp 
            
            return temp

        head = rec(head,head.next)