from ListNode import ListNode

def median3(head):
    if head.next and head.next.next:
        a, b, c = sorted([head.val, head.next.val, head.next.next.val])
        head.val, head.next.val, head.next.next.val = b, a, c
    return head.val

def partition(head):
    pivot = median3(head)
    s_ptr = s_head = ListNode(float("-inf"))
    l_ptr = l_head = ListNode(float("-inf"))
    p_ptr, head = head, head.next
    while head:
        if head.val < pivot:
            s_ptr.next = head
            s_ptr = s_ptr.next
        else:
            l_ptr.next = head
            l_ptr = l_ptr.next
        head = head.next
    s_ptr.next, l_ptr.next, p_ptr.next = None, None, None
    return s_head.next, p_ptr, l_head.next

def q_sort(head):
    if head and head.next:
        left, center, right = partition(head)
        left_tail, right_tail = None, None
        if left:
            left, left_tail = q_sort(left)
            left_tail.next = center
        if right:
            right, right_tail = q_sort(right)
            center.next = right
        return left or center, right_tail or center
    return head, head

def list_quick_sort_(head):
    return q_sort(head)[0]
