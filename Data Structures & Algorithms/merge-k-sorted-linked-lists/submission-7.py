# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # implementation 2 : iteration ; crazy approach
        # same idea divide and conquer 

        # instead of merging left to right along the height / depth , like recursion, , merge all leaves at once , like breadth . then all 2nd level lists then all 3rd level lists . and keep on doing it untill len(lists) == 1
        if not lists:
            return None
        while len(lists) > 1:
            mergedLists = []
            for i in range(0,len(lists),2):
                mergedLists.append(self.mergeList(lists[i],lists[i+1] if i+1 < len(lists) else None))
            lists = mergedLists
        return lists[0]


    def mergeList(self, l1, l2):
        dummy = ListNode()
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

