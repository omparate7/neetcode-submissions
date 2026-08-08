# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    def recursion(self,list1,list2,curr):

        if list1 == None:
            curr.next = list2 
        elif list2 == None:
            curr.next = list1
        elif list1.val < list2.val:
            curr.next = list1
            self.recursion(list1.next,list2,curr.next)
        else:
            curr.next = list2
            self.recursion(list1,list2.next,curr.next)

        return

    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        dummy = ListNode(0)
        self.recursion(list1,list2,dummy)

        return dummy.next

        # method1 : traverse both , store both in list , sort the list , traverse the list and build the ll time complex = O(n+m*log(n+m))+O(n+m) space O(n+m)

        # method2 : traverse both at same time and store in a list then build ll , time cpx O(n+m) , space = O(n+m)

        # method3 : traverse both at the same time witout storing them in list.

        # method4: same as method3 but making a rcursive soluion

        

    
       

       
