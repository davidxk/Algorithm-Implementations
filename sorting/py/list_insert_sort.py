from ListNode import ListNode

def list_insert_sort(head):
    # Add dummy head
    node = ListNode(float("-inf"))
    node.next = head
    head = node
    # Start from head.next
    iPtr, jPtr = head, head
    while iPtr.next:
        if iPtr.val < iPtr.next.val:
            iPtr = iPtr.next
            continue
        jPtr = head
        while jPtr.next.val < iPtr.next.val:
            jPtr = jPtr.next
        # Delete from linked list
        x = iPtr.next
        iPtr.next = iPtr.next.next
        # Insert into linked list
        x.next = jPtr.next
        jPtr.next = x
    return head.next
