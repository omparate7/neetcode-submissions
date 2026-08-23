# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# approach 1 : intutuion is repeatedly apply merging of two lists , keep two list , left and right , right will traverse through arr and left will be the combined result. time cpx O(N*K) N: number of nodes K : len(lists) i mean number of lists  ,,, every node is processed roughly k times , actually ll1 : k times , ll2: k-1 times , ll3 k-2 times like that . so each node in ll1 is processed k times similarly so on . , because that many times merge is called . merge cost = O(n+m) nand m are size of each ll , that is optimal , but we are kalling merge k times ; space cpx (1) but that's giving a TLE why ?? :down
#
# The key hint is:
# Don't merge everything into one growing list immediately. Merge lists of roughly equal size.
# For example, instead of:
# 1 + 2 → 12
# 12 + 3 → 123
# 123 + 4 → 1234
# 1234 + 5 → 12345
# 12345 + 6 → ...
# think:
# 1 + 2 → 12
# 3 + 4 → 34
# 5 + 6 → 56
# 7 + 8 → 78
# 12 + 34 → 1234
# 56 + 78 → 5678
# 1234 + 5678 → final
# left = ListNode(-(2**31))
# def merge(left,right):
#     temp = left if left.val <= right.val else right

#     while(left and right):

#         while left.next and left.next.val <= right.val:
#             left = left.next
#         while right.next and right.next.val < left.val:
#             right = right.next

#         if left.val <= right.val:
#             t = left.next
#             left.next = right
#             left = t
#         else:
#             t = right.next
#             right.next = left
#             right = t

#     return temp

# for i in range(len(lists)):

#     right = lists[i]
#     if right == None:
#         continue
#     left = merge(left,right)

# return left.next


## Aproach 2: simply iterating through all , store in list , sort the list , make ll again O(n) space O(n log n ) time
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(l1, l2):
            dummy = ListNode()
            tail = dummy
            # instead of using the same l1 and l2 for reassigning and traversing , use a diffrent pointer tail to keep track of tail of merged list
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

        for i in range(1,len(lists)):
            lists[i] = merge(lists[i-1],lists[i])

        return lists[len(lists)-1] if lists else None

                
