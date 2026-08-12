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
        hashMap = dict()
        hashMap[None] = None
        dummy = Node(0)
        copy = dummy
        curr = head
        while(curr):
            dummy.next = Node(curr.val)
            hashMap[curr]=dummy.next
            curr=curr.next
            dummy = dummy.next
        
        curr = head
        while(curr):
            temp1 = hashMap[curr]
            curr2 = curr.random
            temp2 = hashMap[curr2]
            temp1.random = temp2
            curr = curr.next
        return copy.next

        
        
        