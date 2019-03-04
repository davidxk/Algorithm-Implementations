import java.util.TreeSet;

public class TestTreeSet
{
	public static void testTreeSet()
	{
		TreeSet<Integer> tree = new TreeSet<Integer>();
		tree.add(3);
		tree.add(6);
		for(int i = 0; i < 10; i++)
			System.out.println("Floor " + i + " is " + tree.floor(i));
		for(int i = 0; i < 10; i++)
			System.out.println("Ceiling " + i + " is " + tree.ceiling(i));
	}
	public static void main(String[] args)
	{
		testTreeSet();
	}
}
