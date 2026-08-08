# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #case1 : the list contains only unique numbers then its very simple , just use a hashset and see if the element is there ornot if not there insert in set if there then return true

        #the above uses O(n) extra space , 

        # using two pointers fast and slow we can do it in O(1)
        if not head : 
            return False

        fast = head.next
        slow = head
        while fast and slow:

            if fast == slow:
                return True
            if fast.next:
                fast=fast.next.next
            else: 
                fast=fast.next
            slow=slow.next
        
        return False