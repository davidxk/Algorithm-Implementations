import java.util.Random;

public class QuickSelect implements SelectionAlgorithm
{
	private Random rand = new Random();
	private void insertion_sort(int[] array, int left, int right)
	{
		int j, x;
		for(int i = left + 1; i < right + 1; i++)
		{
			x = array[i];
			j = i - 1;
			for(j = i - 1; j >= left && array[j] > x; j--)
				array[j + 1] = array[j];
			array[j + 1] = x;
		}
	}
	private int median3(int[] array, int left, int right)
	{
		int center = (left + right) / 2;
		int tmp[] = { array[left], array[center], array[right] };
		insertion_sort(tmp, 0, 2);
		array[left] = tmp[0];
		array[center] = tmp[2];
		array[right] = tmp[1];
		return array[right];
	}
	private int partition(int[] array, int left, int right)
	{
		int pivot = median3(array, left, right);
		int i = left, j = right - 1;
		while(true)
		{
			while(array[i] < pivot) i++;
			while(pivot < array[j]) j--;
			if(i >= j)
			{
				array[i] = array[right] ^ array[i] ^ (array[right] = array[i]);
				return i;
			}
			array[i] = array[j] ^ array[i] ^ (array[j] = array[i]);
			i++; j--;
		}
	}
	private void q_select(int[] array, int left, int right, int rank)
	{
		if(right - left < 10)
		{
			insertion_sort(array, left, right);
			return;
		}
		int center = partition(array, left, right);
		if(rank < center)
			q_select(array, left, center - 1, rank);
		else if(rank > center)
			q_select(array, center + 1, right, rank);
	}
	public int select(int[] array, int rank)
	{
		q_select(array, 0, array.length - 1, rank - 1);
		return array[rank - 1];
	}
}
