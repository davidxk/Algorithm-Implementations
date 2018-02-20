from LinkedList import ListNode

def findMiddle(head):
    fast = slow = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def list_merge_sort(head):
    return list_m_sort(head) if head else None

def list_m_sort(head):
    if head.next is None:
        return head

    slow = findMiddle(head)
    midd, slow.next = slow.next, None

    head = list_m_sort( head )
    midd = list_m_sort( midd )
    head = list_merge(head, midd)
    return head

def list_merge(l1, l2):
    curr = head = ListNode(float("-inf"))
    while l1 and l2:
        if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next

    curr.next = l1 or l2
    return head.next
