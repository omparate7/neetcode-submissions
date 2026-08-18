# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry = 0
        ans = ListNode(0)
        ret = ans
        while(l1 and l2):
            num = (l1.val + l2.val + carry)%10 
            carry = (l1.val + l2.val + carry)//10
            # update 
            ans.next = ListNode(num)
            l2  = l2.next
            l1 =  l1.next
            ans = ans.next
        
        while(l1):
            num = (l1.val + carry)%10 
            carry = (l1.val + carry)//10
            ans.next = ListNode(num)
            l1 = l1.next
            ans = ans.next
        
        while(l2):
            num = (l2.val + carry)%10 
            carry = (l2.val + carry)//10
            ans.next = ListNode(num)
            l2 = l2.next
            ans = ans.next
        
        if carry : 
            ans.next = ListNode(carry)
        

        return ret.next
             # above thing ki zaroorat hi kya hai 

             # seedha you can join the remaining list by adding carry . but that can lead to more edge case handling and complication . 

        