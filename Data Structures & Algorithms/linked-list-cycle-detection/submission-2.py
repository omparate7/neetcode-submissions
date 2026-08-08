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
        
        fast , slow = head , head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next # condition for this to be valid is already been checked in while loop

            if fast == slow:
                return True
            
            

        
        return False