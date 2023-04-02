# For even length
# O O $
#sf
# ^ s f
#
# For odd length
# O O O $
#sf
# ^ s f
# ^   s   f
# Time:  O(n)
# Space: O(1)

# For even length
# O O $
# s f
#
# For odd length
# O O O $
# s f
#   s   f
# Time:  O(n)
# Space: O(1)

def find_middle(head):
    fast = slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
