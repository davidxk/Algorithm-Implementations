
public class BubbleSort implements SortAlgorithm
{
	public void sort(int[] array)
	{
		boolean swapped = false;
		do
		{
			swapped = false;
			for(int i = 1; i < array.length; i++)
				if(array[i - 1] > array[i])
				{
					int tmp = array[i - 1];
					array[i - 1] = array[i];
					array[i] = tmp;
					swapped = true;
				}
		} while(swapped);
	}
}
