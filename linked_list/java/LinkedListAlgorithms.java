
public class LinkedListAlgorithms
{
	public static ListNode findMiddle(ListNode head)
	{
		if(head == null)
			return head;
		ListNode slow = head, fast = head;
		while(fast.next != null && fast.next.next != null)
		{
			slow = slow.next;
			fast = fast.next.next;
		}
		return slow;
	}
	public static ListNode reverse(ListNode head)
	{
		ListNode prev = null, curr = head, next;
		while(curr != null)
		{
			next = curr.next;
			curr.next = prev;
			prev = curr;
			curr = next;
		}
		return prev;
	}
}
