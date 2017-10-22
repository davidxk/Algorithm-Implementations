
public class ListMergeSort implements ListSortAlgorithm
{
	public ListNode sort(ListNode head)
	{
		if(head == null)
			return head;
		return m_sort(head);
	}
	private ListNode m_sort(ListNode head)
	{
		if(head.next == null)
			return head;
		ListNode slow = findMiddle(head);
		ListNode midd = slow.next;
		slow.next = null;

		head = m_sort(head);
		midd = m_sort(midd);
		return merge(head, midd);
	}
	private ListNode findMiddle(ListNode head)
	{
		ListNode slow = head, fast = head;
		while(fast.next != null && fast.next.next != null)
		{
			slow = slow.next;
			fast = fast.next.next;
		}
		return slow;
	}
	private ListNode merge(ListNode l1, ListNode l2)
	{
		ListNode dummy = new ListNode(-1);
		ListNode curr = dummy;
		while(l1 != null && l2 != null)
		{
			if(l1.val < l2.val)
			{
				curr.next = l1;
				l1 = l1.next;
			}
			else
			{
				curr.next = l2;
				l2 = l2.next;
			}
			curr = curr.next;
		}
		curr.next = (l1 != null ? l1 : l2);
		return dummy.next;
	}
}
