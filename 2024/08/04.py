from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# https://leetcode.cn/problems/subtree-of-another-tree/?envType=daily-question&envId=2024-08-04
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]):
        def is_same_tree(p: Optional[TreeNode], t: Optional[TreeNode]):
            if not p and not t:
                return True
            if not p or not t:
                return False
            return p.val == t.val and is_same_tree(p.left, t.left) and is_same_tree(p.right, t.right)

        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        return is_same_tree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


if __name__ == '__main__':
    print(Solution().isSubtree(TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5)),
                               TreeNode(4, TreeNode(1), TreeNode(2))))
    print(Solution().isSubtree(TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0))), TreeNode(5)),
                               TreeNode(4, TreeNode(1), TreeNode(2))))
