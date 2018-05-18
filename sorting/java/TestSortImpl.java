import java.util.ArrayList;
import java.util.Random;

public class TestSortImpl
{
	private static int N = 5000;
	private static boolean checkMonotonic(int[] array)
	{
		for(int i = 1; i < array.length; i++)
			if(array[i - 1] > array[i])
				return false;
		return true;
	}
	private static boolean checkSortImpl(SortAlgorithm func)
	{
		Random rand = new Random();
		int[] a = new int[ N ];
		for(int i = 0; i < a.length; i++)
			a[i] = rand.nextInt(N);

		func.sort(a);
		return checkMonotonic(a);
	}
	public static void main(String[] argv)
	{
		ArrayList<SortAlgorithm> funcs = new ArrayList<SortAlgorithm>();
		funcs.add( new BubbleSort() );
		funcs.add( new InsertionSort() );
		funcs.add( new MergeSort() );
		funcs.add( new QuickSort() );
		funcs.add( new HeapSort() );
		for(SortAlgorithm func: funcs)
			if(!checkSortImpl(func))
				System.out.println("WA: " + func.toString());
	}
}
