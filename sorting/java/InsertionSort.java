
public class InsertionSort implements SortAlgorithm
{
	public void sort(int[] array)
	{
		for(int i = 1; i < array.length; i++)
		{
			int x = array[i];
			int j = i - 1;
			while(j >= 0 && x < array[j] )
			{
				array[j + 1] = array[j];
				j--;
			}
			array[j + 1] = x;
		}
	}
}
