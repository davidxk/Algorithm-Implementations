import java.util.Random;

public class RandomizedSelect implements SelectionAlgorithm
{
	private Random rand = new Random();
	private int random_pivot(int[] array, int left, int right)
	{
		int index = rand.nextInt(right - left + 1) + left;
		int tmp = array[index];
		array[index] = array[right];
		array[right] = tmp;
		return array[right];
	}
	private int partition(int[] array, int left, int right)
	{
		int pivot = random_pivot(array, left, right);
		int i = left, j = right - 1;
		while(true)
		{
			while(i <= right && array[i] < pivot) i++;
			while(left <= j  && pivot < array[j]) j--;
			if(i >= j)
			{
				int tmp = array[i];
				array[i] = array[right];
				array[right] = tmp;
				return i;
			}
			//int tmp = array[i];
			//array[i] = array[j];
			//array[j] = tmp;
			array[i] = array[i] ^ array[j] ^ (array[j] = array[i]);
			i++; j--;
		}
	}
	private int r_select(int[] array, int left, int right, int rank)
	{
		if(left == right)
			return array[left];
		int center = partition(array, left, right);
		int pivot_rank = center - left + 1;
		if(rank == pivot_rank)
			return array[center];
		else if(rank < pivot_rank)
			return r_select(array, left, center - 1, rank);
		else
			return r_select(array, center + 1, right, rank - pivot_rank);
	}
	public int select(int[] array, int rank)
	{
		return r_select(array, 0, array.length - 1, rank);
	}
}
