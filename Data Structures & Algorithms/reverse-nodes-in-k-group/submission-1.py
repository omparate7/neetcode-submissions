# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # its an easy question just some pointer reassingments , what we have to do is break the problem in small steps
        # 1. reversing the ll
        # 2. keeping track of last groups tail and curr groups head
        # 3. avoiding last edge case

        # question is how ?? , implementation baby

        p = head
        res = None
        
        prevTail = None

        while p:
            currTail = p
            prev = None
            k1 = k
            while k1:
                if p is None:
                    while prev != currTail:
                        next = prev.next
                        prev.next = p
                        p = prev
                        prev = next
                    prev.next = p
                    prevTail.next = prev
                    return res
                next = p.next
                p.next = prev
                prev = p
                p = next
                k1 -= 1
            if not prevTail:
                res = prev
                prevTail = currTail
            else:
                prevTail.next = prev
                prevTail = currTail

        return res
