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
        # appraoch 2 : storing copied node in random pointer 
        if head is None : 
            return None
        l1 = head
        while(l1):
            l2 = Node(l1.val)
            l2.next = l1.random
            l1.random = l2
            l1 = l1.next
        
        l1 = head
        while(l1):
            #assigning random pointers of new list
            l1.random.random = l1.random.next.random if l1.random.next else None
            l1 = l1.next
        l1 = head
        res = head.random
        while(l1):
            temp = l1.random.next
            l1.random.next = l1.next.random if l1.next else None
            l1.random = temp
            l1 = l1.next 
        return res
        

        