# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # approach 3: divide and conquer

        # implementation 1: recursion;

        def merge(l, r):
            def merge2(l1, l2):

                dummy = ListNode(0)
                tail = dummy
                while l1 and l2:
                    if l1.val < l2.val:
                        tail.next = l1
                        l1 = l1.next
                    else:
                        tail.next = l2
                        l2 = l2.next
                    tail = tail.next
                if l1:
                    tail.next = l1
                if l2:
                    tail.next = l2

                return dummy.next
            if not lists:
                return None
            if r > l:
                mid = (r + l) // 2
                l1 = merge(l, mid)
                l2 = merge(mid + 1, r)
                return merge2(l1, l2)
            return lists[l]

        return merge(0,len(lists)-1)


