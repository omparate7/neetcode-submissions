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
        
        # space optimised approach 1 : what i want is a way to get to the copy nodes as well as orignal nodes along with remembering their mapping , so in this approach we will store copy nodes in orignal nodes's next pointer 

        # approach 2 : same idea as one but here we will store copy nodes in random pointer 

        #1

        l1 = head
        if not l1 :
            return None
        while(l1):
            temp = l1.next
            l1.next = Node(l1.val)
            l1.next.next = temp
            l1 = temp
        
        l1 = head

        while(l1):
            l1.next.random = l1.random.next if l1.random else None
            l1 = l1.next.next

        l1 = head
        res = head.next
        while(l1):
            l2 = l1.next
            l1.next = l2.next
            l2.next = l2.next.next if l2.next else None
            l1 = l1.next
        
        return res
        


