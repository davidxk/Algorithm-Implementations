import java.util.Random;
import java.util.Arrays;

public class TestBinarySearch
{
	public static final int size = 1000;
	public static Random myrand = new Random();
	public static int[] setUp(int size)
	{
		int[] array = new int[size];
		int i, target;
		for(i = 0; i < size; i++)
			array[i] = myrand.nextInt();
		return array;
	}
	public static void testBinarySearch()
	{
		int[] array = new int[size];
		for(int i = 0; i < size; i++)
			array[i] = i;
		for(int i = 0; i < 100; i++)
		{
			int target = myrand.nextInt() % (size * 2);
			if(target >= size)
				assert BinarySearch.search(array, target) == -1;
			else
				assert BinarySearch.search(array, target) == target;
		}
	}
	public static void testLower()
	{
		int[] array = setUp(size);
		Arrays.sort(array);
		int lower = 0;
		for(int i = 0; i < 100; i++)
		{
			int target = myrand.nextInt();
			for(int j = 0; j < size; j++)
				if(array[j] >= target)
				{
					lower = j - 1;
					break;
				}
			assert BinarySearch.lower(array, target) == lower;
		}
	}
	public static void testHigher()
	{
		int[] array = setUp(size);
		Arrays.sort(array);
		int upper = 0;
		for(int i = 0; i < 100; i++)
		{
			int target = myrand.nextInt();
			for(int j = size - 1; j >= 0; j--)
				if(array[j] <= target)
				{
					upper = j + 1;
					break;
				}
			assert BinarySearch.higher(array, target) == upper;
		}
	}
	public static void main(String[] args)
	{
	}
}
