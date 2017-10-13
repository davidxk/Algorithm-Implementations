import java.lang.Math;

public class RMQSegmentTree
{
	private int length;
	private int[] tree;
	public RMQSegmentTree(int array[])
	{
		this.length = array.length;
		int x = (int) (Math.log(this.length) / Math.log(2) + 1);
		int size = (int) Math.pow(2, x) * 2;
		this.tree = new int[size];
		build(0, array, 0, this.length - 1);
	}
	private void build(int index, int[] array, int left, int right)
	{
		if(left >= right)
		{
			tree[index] = array[left];
			return;
		}
		int center = left + (right - left) / 2;
		build(2 * index + 1, array, left, center);
		build(2 * index + 2, array, center + 1, right);
		tree[index] = Math.min(tree[2 * index + 1], tree[2 * index + 2]);
	}
	public int query(int left, int right)
	{
		return queryUtil(0, left, right, 0, this.length - 1);
	}
	private int queryUtil(int index, int qLeft, int qRight, int left, int right)
	{
		if(qLeft <= left && right <= qRight)
			return tree[index];

		if(right < qLeft || qRight < left)
			return Integer.MAX_VALUE;

		int center = left + (right - left) / 2;
		return Math.min(queryUtil(2 * index + 1, qLeft, qRight, left, center),
				queryUtil(2 * index + 2, qLeft, qRight, center + 1, right));
	}
	public void update(int index, int delta)
	{
		int left = 0, right = this.length - 1;
		int i = 0;
		while(left < right)
		{
			int center = left + (right - left) / 2;
			if(index <= center)
			{
				right = center;
				i = 2 * i + 1;
			}
			else
			{
				left = center + 1;
				i = 2 * i + 2;
			}
		}
		tree[i] += delta;
		while(i > 0)
		{
			i = (i - 1) / 2;
			tree[i] = Math.min(tree[2 * i + 1], tree[2 * i + 2]);
		}
	}
}
