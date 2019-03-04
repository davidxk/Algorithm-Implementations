class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def getLinkedList(array):
    head = ListNode(array[0])
    ptr = head
    for i in range(1, len(array)):
        ptr.next = ListNode(array[i])
        ptr = ptr.next
    return head

def getArray(head):
    ptr = head
    arr = []
    while ptr:
        try:
            arr.append(ptr.val)
        except:
            print ptr
        ptr = ptr.next
    return arr
