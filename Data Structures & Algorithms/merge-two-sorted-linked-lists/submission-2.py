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

        dummy = ListNode(0, None)
        curr = dummy

        while list1 and list2:
            if list1.val < list2.val :
                curr.next = list1
                list1=list1.next
            else:
                curr.next = list2
                list2=list2.next
            curr = curr.next

        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2

        return dummy.next

       

       
