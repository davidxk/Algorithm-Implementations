
public class ListNode
{
	public int val;
	public ListNode next;
	public ListNode(int x) { val = x; next = null; }
	public static ListNode getLinkedList(int[] array)
	{
		if(array.length == 0)
			return null;
		ListNode head = new ListNode(array[0]);
		ListNode curr = head;
		for(int i = 1; i < array.length; i++)
		{
			curr.next = new ListNode(array[i]);
			curr = curr.next;
		}
		return head;
	}
	public static int[] getArray(ListNode head)
	{
		ListNode curr = head;
		int cnt = 0;
		while(curr != null)
		{
			curr = curr.next;
			cnt++;
		}
		int[] array = new int[cnt];
		for(int i = 0; i < cnt; i++)
		{
			array[i] = curr.val;
			curr = curr.next;
		}
		return array;
	}
}
