class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyHashSet:
    def __init__(self):
        self.data = [ListNode(0) for i in range(10**4)]

    def add(self, key: int) -> None:
        # calculate the index in the data array
        idx = key % (10 ** 4)
        # access ListNode at that index
        node = self.data[idx]
        # get to the end of the linked list
        while node.next:
            # already seen key -> we don't allow duplicates
            if node.next.val == key: return
            node = node.next
        # insert the new node at the end
        node.next = ListNode(key)

    def remove(self, key: int) -> None:
        idx = key % (10 ** 4)
        node = self.data[idx]
        while node.next:
            # removing the key value node by skipping the next pointer
            # early return if the key was deleted
            if node.next.val == key:
                node.next = node.next.next
                return
            node = node.next

    def contains(self, key: int) -> bool:
        idx = key % (10 ** 4)
        node = self.data[idx]
        while node.next:
            if node.next.val == key: return True
            node = node.next
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)