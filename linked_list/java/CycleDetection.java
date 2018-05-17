
class CycleDetection
{
	public boolean detectCycle(ListNode head)
	{
		ListNode fast = head, slow = head;
		while(fast != null && fast.next != null)
		{
			slow = slow.next;
			fast = fast.next.next;
			if(slow == fast)
				return true;
		}
		return false;
	}
	public boolean findCycle(ListNode head)
	{
		ListNode fast = head, slow = head;
		while(fast != null && fast.next != null)
		{
			slow = slow.next;
			fast = fast.next;
			if(slow == fast)
			{
				slow = head;
				while(slow != fast)
				{
					slow = slow.next;
					fast = fast.next;
				}
				return fast;
			}
		}
		return null;
	}
}
