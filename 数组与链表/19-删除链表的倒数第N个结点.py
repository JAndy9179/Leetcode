"""
思路:

如果直接处理比较麻烦的话, 可以尝试添加一个头节点
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        h = ListNode(0, head)
        fast, slow = h, h
        for _ in range(n):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return h.next
        