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
        while l1 and l2:
            num = (l1.val + l2.val + carry) % 10
            carry = (l1.val + l2.val + carry) // 10
            # update
            ans.next = ListNode(num)
            l2 = l2.next
            l1 = l1.next
            ans = ans.next

        # while l1:
        #     num = (l1.val + carry) % 10
        #     carry = (l1.val + carry) // 10
        #     ans.next = ListNode(num)
        #     l1 = l1.next
        #     ans = ans.next

        # while l2:
        #     num = (l2.val + carry) % 10
        #     carry = (l2.val + carry) // 10
        #     ans.next = ListNode(num)
        #     l2 = l2.next
        #     ans = ans.next

        # if carry:
        #     ans.next = ListNode(carry)



        if l1 :
            while(carry and l1):
                num = (l1.val + carry) % 10
                carry = (l1.val + carry) // 10
                ans.next = ListNode(num)
                l1 = l1.next
                ans = ans.next
            ans.next = l1

        if l2 :
            while(carry and l2):
                num = (l2.val + carry) % 10
                carry = (l2.val + carry) // 10
                ans.next = ListNode(num)
                l2 = l2.next
                ans = ans.next
            ans.next = l2

        if carry:
            ans.next = ListNode(carry)
        return ret.next
