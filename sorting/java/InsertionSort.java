
public class InsertionSort implements SortAlgorithm
{
	public void sort(int[] array)
	{
		int j;
		for(int i = 1; i < array.length; i++)
		{
			int x = array[i];
			for(j = i - 1; j >= 0; j--)
				if(array[j] > x)
					array[j + 1] = array[j];
				else
					break;
			array[j + 1] = x;
		}
	}
}
