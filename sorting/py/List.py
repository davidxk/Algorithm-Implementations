from ListNode import ListNode

class List:
    def __init__():
        self.head = None

    def is_empty(self):
        return self.head == None

    def insert_after(self, prev, value):
        node = ListNode(value)
        node.next = prev.next
        prev.next = node

    def delete(self, node):
        ptr = self.head
        while ptr.next != node:
            ptr = ptr.next
        prev = ptr
        prev.next = node.next
        node = None

    def find(self, value):
        ptr = self.head
        while ptr and ptr.val != value:
            ptr = ptr.next
        if ptr.val == value:
            return ptr
        return None

