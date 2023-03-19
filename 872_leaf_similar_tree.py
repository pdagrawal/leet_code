class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.leaf_nodes(root1) == self.leaf_nodes(root2)

    def leaf_nodes(self, root):
        res = []
        if not root:
            return []
        if not root.left and not root.right:
            res.append(root.val)
        res += self.leaf_nodes(root.left)
        res += self.leaf_nodes(root.right)
        return res


