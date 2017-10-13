import java.util.Random;

public class TestRMQSegmentTree
{
	private static Random myrand = new Random();
	public static void testQuery()
	{
		final int size = 100;
		int[] array = new int[size];
		int left, right;
		int minimum;
		for(int i = 0; i < size; i++)
			array[i] = myrand.nextInt(size);
		RMQSegmentTree rmq = new RMQSegmentTree(array);
		for(int i = 0; i < size; i++)
		{
			left = myrand.nextInt(size / 2);
			right = myrand.nextInt(size);
			minimum = Integer.MAX_VALUE;
			for(int j = left; j <= right; j++)
				if(array[j] < minimum)
					minimum = array[j];
			assert rmq.query(left, right) == minimum;
		}
	}
	public static void testUpdate()
	{
		final int size = 100;
		int[] array = new int[size];
		int left, right;
		int minimum;
		for(int i = 0; i < size; i++)
			array[i] = myrand.nextInt(size);
		RMQSegmentTree rmq = new RMQSegmentTree(array);

		int index = myrand.nextInt(size), delta = -myrand.nextInt(50);
		array[index] += delta;
		rmq.update(index, delta);
		for(int i = 0; i < size; i++)
		{
			left = myrand.nextInt(size / 2);
			right = myrand.nextInt(size);
			minimum = Integer.MAX_VALUE;
			for(int j = left; j <= right; j++)
				if(array[j] < minimum)
					minimum = array[j];
			assert rmq.query(left, right) == minimum;
		}
	}
	public static void main(String[] args)
	{
		testQuery();
		testUpdate();
	}
}
