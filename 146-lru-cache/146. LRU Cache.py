class ListNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.LRU = ListNode(-1, -1)
        self.MRU = ListNode(-1, -1)
        self.LRU.next = self.MRU
        self.MRU.prev = self.LRU

    def remove(self, node: ListNode) -> None:
        prev_from_node, next_from_node = node.prev, node.next
        prev_from_node.next = next_from_node
        next_from_node.prev = prev_from_node

    def insert_at_end(self, node: ListNode) -> None:
        mru_prev = self.MRU.prev
        mru_prev.next = node
        node.prev = mru_prev
        node.next = self.MRU
        self.MRU.prev = node

    def make_mru(self, node: ListNode) -> None:
        # remove the node from the list
        self.remove(node)
        # insert it at the end
        self.insert_at_end(node)

    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1
        # get the node pointer from the cache
        # update the node to be the MRU
        # return the val
        node = self.cache[key]
        self.make_mru(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # update the val & mark as MRU
            # early return
            node = self.cache[key]
            node.val = value
            self.make_mru(node)
            return
        
        # create node, insert in the cache & linked list
        node = ListNode(key, value)
        self.cache[key] = node
        self.insert_at_end(node)
        # check for cap overflow -> remove the LRU.next node from list and del from cache
        if len(self.cache) > self.cap:
            del self.cache[self.LRU.next.key]
            self.remove(self.LRU.next)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)