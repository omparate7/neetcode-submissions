# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        # method1 : traverse both , store both in list , sort the list , traverse the list and build the ll time complex = O(n+m*log(n+m))+O(n+m) space O(n+m)

        # method2 : traverse both at same time and store in a list then build ll , time cpx O(n+m) , space = O(n+m)

        # method3 : traverse both at the same time witout storing them in list.

        # method3:

        curr1 = list1
        curr2 = list2

        dummy = ListNode(0, None)
        curr = dummy

        while curr1 and curr2:
            if curr1.val < curr2.val:
                curr.next = ListNode(curr1.val)
                curr1 = curr1.next
            else:
                curr.next = ListNode(curr2.val)
                curr2 = curr2.next

            curr = curr.next

        while curr1:
            curr.next = ListNode(curr1.val)
            curr1 = curr1.next
            curr = curr.next

        while curr2:
            curr.next = ListNode(curr2.val)
            curr2 = curr2.next
            curr = curr.next

        return dummy.next

       
