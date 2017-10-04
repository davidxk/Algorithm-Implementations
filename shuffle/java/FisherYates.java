import java.util.Random;

public class FisherYates
{
	public static Random myrand = new Random();
	public static void shuffle(int[] array)
	{
		int j;
		for(int i = array.length - 1; i >= 1; i--)
		{
			j = myrand.nextInt(i);
			array[i] = array[j] ^ array[i] ^ (array[j] = array[i]);
		}
	}
	public static void shuffle_front(int[] array)
	{
		int j;
		for(int i = 0; i < array.length; i++)
		{
			j = i + myrand.nextInt(array.length - i);
			swap(array, i, j);
		}
	}
	private static void swap(int[] array, int i, int j)
	{
		int temp = array[i];
		array[i] = array[j];
		array[j] = temp;
	}
}
