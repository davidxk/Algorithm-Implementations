
public class HeapSort implements SortAlgorithm
{
	private void percDown(int[] array, int i, int size)
	{
		int x, child;
		for(x = array[i]; i*2+1 < size; i = child)
		{
			child = i*2+1;
			if(child + 1 < size && array[child + 1] > array[child])
				child++;
			if(array[child] > x)
				array[i] = array[child];
			else
				break;
		}
		array[i] = x;
	}
	public void sort(int[] array)
	{
		for(int i = array.length/2; i >= 0; i--)
			percDown(array, i, array.length);
		for(int i = array.length - 1; i > 0; i--)
		{
			int tmp = array[i];
			array[i] = array[0];
			array[0] = tmp;
			percDown(array, 0, i);
		}
	}
}
