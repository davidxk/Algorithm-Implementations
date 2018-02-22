import java.util.ArrayList;
import java.util.Collections;

// Java PriorityQueue does not support heapify
class Heap
{
	public static <T extends Comparable<T>> void percDown(ArrayList<T> array, int i, int size)
	{
		T x = array.get(i);
		int child;
		while(2 * i + 1 < size)
		{
			child = 2 * i + 1;
			if(child + 1 < size && array.get(child + 1).compareTo(array.get(child)) < 0)
				child++;
			if(x.compareTo(array.get(child)) > 0)
			{
				array.set(i, array.get(child));
				i = child;
			}
			else
				break;
		}
		array.set(i, x);
	}
	public static <T extends Comparable<T>> void heapify(ArrayList<T> array)
	{
		for(int i = array.size() / 2; i >= 0; i--)
			percDown(array, i, array.size());
	}
	public static <T extends Comparable<T>> void heappush(ArrayList<T> array, T elem)
	{
		array.add(elem);
		int i = array.size() - 1;
		int parent;
		while(i > 0)
		{
			parent = (i - 1) / 2;
			if(array.get(i).compareTo(array.get(parent)) < 0)
			{
				Collections.swap(array, i, parent);
				i = parent;
			}
			else
				break;
		}
	}
	public static <T extends Comparable<T>> T heappop(ArrayList<T> array)
	{
		T retval = array.get(0);
		array.set(0, array.get(array.size() - 1));
		array.remove(array.size() - 1);
		percDown(array, 0, array.size());
		return retval;
	}
}
