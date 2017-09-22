import java.util.Random;

public class TestBinaryIndexedTree
{
	public static Random myrand = new Random();
	public static void testGetSum()
	{
		final int LENGTH = 100;
        int[] array = new int[LENGTH];
		for(int i = 0; i < LENGTH; i++)
			array[i] = myrand.nextInt(100);
		BinaryIndexedTree bit = new BinaryIndexedTree(array);
		int sum, right;
		for(int cnt = 0; cnt < 100; cnt++)
		{
			right = myrand.nextInt(LENGTH);
			sum = 0;
			for(int i = 0; i <= right; i++)
				sum += array[i];
			assert sum == bit.getSum(right);
		}
	}
	public static void testUpdate()
	{
		final int LENGTH = 100;
        int[] array = new int[LENGTH];
		for(int i = 0; i < LENGTH; i++)
			array[i] = myrand.nextInt(100);
		BinaryIndexedTree bit = new BinaryIndexedTree(array);
		int sum, right;
		int index, delta;
		for(int cnt = 0; cnt < 100; cnt++)
		{
			index = myrand.nextInt(LENGTH);
			delta = myrand.nextInt(LENGTH);
			array[index] += delta;
			bit.update(index, delta);

			right = myrand.nextInt(LENGTH);
			sum = 0;
			for(int i = 0; i <= right; i++)
				sum += array[i];
			assert sum == bit.getSum(right);
		}
	}
	public static void testRange()
	{
		final int LENGTH = 100;
        int[] array = new int[LENGTH];
		for(int i = 0; i < LENGTH; i++)
			array[i] = myrand.nextInt(100);
		BinaryIndexedTree bit = new BinaryIndexedTree(array);
		int sum, left, right;
		for(int cnt = 0; cnt < 100; cnt++)
		{
			left = myrand.nextInt(LENGTH/2);
			right = left + myrand.nextInt(LENGTH/2);
			sum = 0;
			for(int i = left; i <= right; i++)
				sum += array[i];
			assert sum == bit.getRange(left, right);
		}
	}
	public static void main(String[] args)
	{
		testGetSum();
		testUpdate();
		testRange();
	}
}
