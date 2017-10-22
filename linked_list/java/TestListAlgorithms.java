import java.util.Random;
import java.util.Arrays;

public class TestListAlgorithms
{
	private static Random myrand = new Random();
	public static void testFindMiddle(int size)
	{
		int[] array = new int[size];
		for(int i = 0; i < size; i++)
			array[i] = i;
		ListNode head = ListNode.getLinkedList(array);
		ListNode middle = LinkedListAlgorithms.findMiddle(head);
		assert middle.val == (size - 1) / 2;
	}
	public static void testReverse()
	{
		final int size = 100;
		int[] array = new int[size];
		ListNode head = ListNode.getLinkedList(array);
		ListNode reversed = LinkedListAlgorithms.reverse(head);
		ListNode curr = reversed;
		for(int i = size - 1; i >= 0; i--)
		{
			assert curr.val == array[i];
			curr = curr.next;
		}
	}
	public static void testListSortImpl(ListSortAlgorithm func)
	{
		final int size = 100;
		int[] array = new int[size];
		for(int i = 0; i < size; i++)
			array[i] = myrand.nextInt();
		ListNode head = ListNode.getLinkedList(array);
		head = func.sort(head);
		ListNode curr = head;
		Arrays.sort(array);
		for(int i = 0; i < size; i++)
		{
			assert array[i] == curr.val;
			curr = curr.next;
		}
	}
	public static void main(String[] argv)
	{
		testFindMiddle(100);
		testFindMiddle(99);
		testReverse();
		testListSortImpl(new ListMergeSort());
	}
}
