from ListNode import ListNode

def median3(head):
    if head.next and head.next.next:
        return sorted([head.val, head.next.val, head.next.next.val])[1]
    return head.val

def list_partition(head):
    pivot = median3(head)
    s_head = s_ptr = ListNode(float("-inf"))
    l_head = l_ptr = ListNode(float("-inf"))
    p_head = p_ptr = ListNode(float("-inf"))
    while head:
        if head.val < pivot:
            s_ptr.next = head
            s_ptr = s_ptr.next
        elif head.val > pivot:
            l_ptr.next = head
            l_ptr = l_ptr.next
        else:
            p_ptr.next = head
            p_ptr = p_ptr.next
        head = head.next
    s_ptr.next, l_ptr.next, p_ptr.next = None, None, None
    return s_head.next, l_head.next, p_head.next, p_ptr
    

def list_q_sort(head):
    if head and head.next:
        left, center, pivot_start, pivot_end = list_partition(head)
        head, tail = pivot_start, pivot_end
        if left:
            small_start, small_end = list_q_sort(left)
            head = small_start
            small_end.next = pivot_start
        if center:
            large_start, large_end = list_q_sort(center)
            tail = large_end
            pivot_end.next = large_start
        return head, tail

    return head, head

def list_quick_sort(head):
    return list_q_sort(head)[0]
