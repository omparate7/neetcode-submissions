# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    # we can find maximum depth of left subtree and right subtree and add them for each node.
    def depth(self, node, map):
        if not node:
            return 0
        if map.get(node):
            return map[node]
        map[node] = 1 + max(self.depth(node.left, map), self.depth(node.right, map))
        return map[node]

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        stack = [root]
        map = {}
        while stack:
            node = stack.pop()
            ans = max(ans, self.depth(node.left, map) + self.depth(node.right, map))
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return ans
