"""
思路: 创建 TNode 结构, 其中包含 is_end(该节点是不是作为某个 word 的结束位置), 以及 next(共 26 个插槽, 默认为空)

tips: 这里有个黑科技, 就是用 ord(c) 得到当前字母的 ASCII 编码, 然后通过 ord(c) - ord('a') 在 next 中查找对应位置的插槽是否为空

insert: 若 curr.next[idx] 不为空说明存储了相同前缀的 word, 只需要让 curr 继续前进即可; 若 curr.next[idx] 为空, 则需要先建新节点, 并让 curr.next[idx] 指向它, 再让 curr 前进即可

search: 需要严格判断路径是否存在, 以及最终 curr 停留的位置的 is_end 是否为 True. 若 is_end 为 False 同样需要返回 False, 因为此时只存过前缀为当前 word 的单词, 而并非存过 word 本身

startsWith: 相比 search 宽松许多, 只需判断路径是否存在即可
"""


class TNode:
    def __init__(self, is_end = False):
        self.is_end = is_end
        self.next = [None for _ in range(26)]


class Trie:
    def __init__(self):
        self.head = TNode()

    def insert(self, word: str) -> None:
        curr = self.head
        for c in word:
            idx = ord(c) - ord('a')
            if curr.next[idx] is None:
                # 创建新节点, 并让 curr.next[idx] 指向它, 同时更新 curr 的位置
                node = TNode()
                curr.next[idx] = node
                curr = node
            else:
                curr = curr.next[idx]

        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self.head
        for c in word:
            idx = ord(c) - ord('a')
            if curr.next[idx] is None:
                return False
            curr = curr.next[idx]

        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        curr = self.head
        for c in prefix:
            idx = ord(c) - ord('a')
            if curr.next[idx] is None:
                return False
            curr = curr.next[idx]

        return True
