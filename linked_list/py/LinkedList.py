class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def getLinkedList(array):
    if not array:
        return None
    curr = head = ListNode(array[0])
    for i in range(1, len(array)):
        curr.next = ListNode(array[i])
        curr = curr.next
    return head

def getArray(head):
    curr = head
    array = []
    while curr:
        array.append(curr.val)
        curr = curr.next
    return array
