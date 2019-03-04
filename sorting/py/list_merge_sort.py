from ListNode import ListNode

def list_merge_sort(head):
    if head is None or head.next is None:
        return head

    fast, slow = head, head
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
    midd, slow.next = slow.next, None

    head = list_merge_sort( head )
    midd = list_merge_sort( midd )
    head = list_merge(head, midd)
    return head

def list_merge(list_a, list_b):
    head = ListNode(float("-inf"))
    ptr, l1, l2 = head, list_a, list_b
    while l1 and l2:
        if l1.val < l2.val:
            ptr.next = l1
            l1 = l1.next
        else:
            ptr.next = l2
            l2 = l2.next
        ptr = ptr.next

    ptr.next = l1 or l2
    return head.next
    
        
