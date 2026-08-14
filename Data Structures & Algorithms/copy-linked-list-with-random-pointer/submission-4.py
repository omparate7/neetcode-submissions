"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # appraoch 2 : single pass , what if the copy node already exist and when we traverse through orig list we overwrite the data ; that's possible through default dict.

        hashMap = defaultdict(lambda : Node(0))
        hashMap[None] = None
        # curr = head
        def func(curr,hashMap):
            if not curr:
                return
            hashMap[curr].val = curr.val
            hashMap[curr].next = hashMap[curr.next]
            hashMap[curr].random = hashMap[curr.random]
            func(curr.next,hashMap)
        func(head,hashMap)
        return hashMap[head]
        

        