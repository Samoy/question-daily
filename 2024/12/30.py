from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# https://leetcode.cn/problems/linked-list-in-binary-tree/?envType=daily-question&envId=2024-12-30
class Solution:
    def dfs(self, head: ListNode, rt: TreeNode) -> bool:
        if not head:
            return True
        if not rt:
            return False
        if rt.val != head.val:
            return False
        return self.dfs(head.next, rt.left) or self.dfs(head.next, rt.right)

    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        return self.dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
