# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # approach 2: iteration choosing the minimum of all lists head at a time time complexity O(n*k) becoz we will traverse through k lists almost n times . 
        res = ListNode()
        curr = res
        while True:
            minNode = -1
            minVal = 2**31-1
            for i in range(len(lists)):
                if lists[i]:
                    if lists[i].val < minVal:
                        minNode = i
                        minVal = lists[i].val
            
            if minNode == -1:
                break
            
            curr.next = lists[minNode]
            lists[minNode] = lists[minNode].next
            curr = curr.next
        return res.next

        



        