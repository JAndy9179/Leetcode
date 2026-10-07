"""
思路:

题目要求 get() 和 put() 方法的时间复杂度都为 O(1), 则需要:
    1. 定义一个字典, 这样 get() 的时候直接用 self.cache[key] 就能快速查找节点的 value
    2. LRU 只需要操作开头和结尾的元素, 因此需要定义一个双向链表, 并用两个指针分别指向虚拟的头尾节点, 这样就可以快速拿到头节点后面和尾节点前面的元素
    3. 此时还有个问题, 就是访问一个元素后, 需要将其添加到头结点的后面, 如何能够快速找到这个节点呢？这里使用 self.cache[key] 直接存储对应的节点, 而非节点的 value, 这样可以用 O(1) 时间找到节点, 并用 Q(1) 时间移动节点到头部
"""


class DLinkNode:
    def __init__(self, key=-1, val=-1, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        # 定义容量
        self.capacity = capacity
        self.current_cap = 0

        # 定义存储结构
        self.cache = dict()
        self.head = DLinkNode()
        self.tail = DLinkNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _delete_node(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
        node.next = None
        node.prev = None

    def _add_to_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def _move_to_head(self, node):
        self._delete_node(node)
        self._add_to_head(node)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._move_to_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._move_to_head(node)
        else:
            if self.current_cap == self.capacity:
                del_node = self.tail.prev
                self.cache.pop(del_node.key, None)
                self._delete_node(del_node)
                self.current_cap -= 1
            node = DLinkNode(key=key, val=value)
            self.cache[key] = node
            self._add_to_head(node)
            self.current_cap += 1