# Floyd's tortoise and hare algorithm
# Time:  O(n)
# Space: O(1)

def cycle_detection(head):
    fast = slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return True
    return False

def cycle_finding(head):
    fast = slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            slow = head
            while fast != slow:
                slow = slow.next
                fast = fast.next
            return fast
    return None
