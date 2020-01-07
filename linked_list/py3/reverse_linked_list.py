#      O -> O -> O -> $
# prev curr nxt
#                O -> $
#                prev curr
# Time:  O(n)
# Space: O(1)

def reverse_linked_list(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev
