"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.map = {}


    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if head is None:
            return None
        if head in self.map: # what i want to check is if head exists in  map or not . # if the key exists then it is sure that the value also exists , because of the nature of our recursion func.
            return self.map[head]
        copy = Node(head.val)
        self.map[head] = copy
        copy.next= self.copyRandomList(head.next)
        copy.random = self.map.get(head.random)  # getting value without getting key error , if map[None] it will return None , because that we never added in the map
        

        return copy
    
        