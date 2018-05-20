
public class QuickSort implements SortAlgorithm
{
	public void insertionSort(int[] array, int left, int right)
	{
		int j;
		for(int i = left + 1; i < right + 1; i++)
		{
			int x = array[i];
			for(j = i - 1; j >= left; j--)
				if(array[j] > x)
					array[j + 1] = array[j];
				else
					break;
			array[j + 1] = x;
		}
	}
	public void sort(int[] array)
	{
		q_sort(array, 0, array.length - 1);
	}
	private void q_sort(int[] array, int left, int right)
	{
		if(right - left > 10)
		{
			int center = partition(array, left, right);
			q_sort(array, left, center - 1);
			q_sort(array, center + 1, right);
		}
		else
			insertionSort(array, left, right);
	}
	private int partition(int[] array, int left, int right)
	{
		int pivot = median3(array, left, right);
		int i = left + 1, j = right - 1;
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
	private int median3(int[] array, int left, int right)
	{
		int center = (left + right) / 2;
		int[] tmp = { array[left], array[center], array[right] };
		insertionSort(tmp, 0, 2);
		array[left] = tmp[0];
		array[center] = tmp[2];
		array[right] = tmp[1];
		return array[right];
	}
}
