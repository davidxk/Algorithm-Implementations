
def find_middle(head):
    if not head:
        return None

    fast = slow = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow
