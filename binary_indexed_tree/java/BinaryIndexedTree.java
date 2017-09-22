
public class BinaryIndexedTree
{
	public int[] tree; 
	public BinaryIndexedTree(int[] array)
	{
		tree = new int[array.length + 1];
		tree[0] = 0;
		for(int i = 0; i < array.length; i++)
			tree[i + 1] = array[i];
		for(int i = 1; i < tree.length; i++)
		{
			int j = i + (i & (-i));
			if(j < tree.length)
				tree[j] += tree[i];
		}
	}
	public int getSum(int i)
	{
		i += 1;
		int sum = 0;
		while(i > 0)
		{
			sum += tree[i];
			i -= i &(-i);
		}
		return sum;
	}
	public void update(int i, int delta)
	{
		i += 1;
		while(i < tree.length)
		{
			tree[i] += delta;
			i += i &(-i);
		}
	}
	public int getRange(int i, int j)
	{
		return getSum(j) - getSum(i - 1);
	}
}
