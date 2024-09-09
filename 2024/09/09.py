from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# https://leetcode.cn/problems/merge-nodes-in-between-zeros/?envType=daily-question&envId=2024-09-09
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail = head
        cur = head.next
        while cur.next:
            if cur.val:
                tail.val += cur.val
            else:
                tail = tail.next
                tail.val = 0
            cur = cur.next
        tail.next = None
        return head


if __name__ == '__main__':
    head = ListNode(0, ListNode(3, ListNode(1, ListNode(0, ListNode(4, ListNode(5, ListNode(2, ListNode(0))))))))
    print(Solution().mergeNodes(head))
    head = ListNode(0, ListNode(1, ListNode(0, ListNode(3, ListNode(0, ListNode(2, ListNode(2, ListNode(0))))))))
    print(Solution().mergeNodes(head))
