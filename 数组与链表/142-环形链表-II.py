"""
思路:

直接用一个集合, 每经过一个节点就把节点添加到集合中, 直到遇到重复元素
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()
        curr = head

        while curr:
            if curr not in seen:
                seen.add(curr)
                curr = curr.next
            else:
                return curr

        return None