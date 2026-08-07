# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # method1 : traverse , store , reverse, build again time compx o(2n) space O(n) 

        # method 2: O(n) reverse on the go use 3 pointers.

        #method1 

        # temp = list()
        # curr = head
        # while(curr):
        #     temp.append(curr.val)
        #     curr = curr.next

        # temp.reverse()

        # curr = head
        # for i in temp:
        #     curr.val = i
        #     curr=curr.next


        # return head

        #method 2
        if head==None: 
            return None
        curr = head
        prev = None
        next = None
        
        while(curr):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev


    