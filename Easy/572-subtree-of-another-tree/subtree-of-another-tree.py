# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.subtree = True

        def dfs(node):
            if not node:
                return "x"
            return "o" + str(node.val) + dfs(node.left) + dfs(node.right)

        Tarr = dfs(root)
        Tsubarr = dfs(subRoot)

        if Tsubarr not in Tarr:
            self.subtree = False

        return self.subtree

        
