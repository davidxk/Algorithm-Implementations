import java.util.Random;

public class TestThreeWayPartition
{
	public static void testPartition()
	{
		Random myrand = new Random();
		final int size = 100;
		int[] array = new int[size];
		int[] cnt = { 0, 0, 0 };
		int num = 0;
		for(int i = 0; i < size; i++)
		{
			num = myrand.nextInt(3);
			array[i] = num;
			cnt[num] += 1;
		}
		ThreeWayPartition.partition(array);
		for(int i = 0; i < size; i++)
		{
			if(array[i] != 0 && array[i - 1] > array[i])
				System.out.println("Partition Error: order");
			cnt[array[i]]--;
		}
		if(!(array[0] == array[1] && array[1] == array[2] && array[2] == 0))
			System.out.println("Partition Error: swap");
	}
	public static void main(String[] args)
	{
		for(int i = 0; i < 100; i++)
			testPartition();
	}
}
