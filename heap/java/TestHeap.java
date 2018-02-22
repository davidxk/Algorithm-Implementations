import java.util.ArrayList;
import java.util.Arrays;
import java.util.Random;

class TestHeap
{
	public static Random myrand = new Random();
	public static void testHeapify()
	{
		final int N = 1000;
		int[] array = new int[N]; 
		ArrayList<Integer> heap = new ArrayList<Integer>();
		for(int i = 0; i < N; i++)
		{
			array[i] = myrand.nextInt(N);
			heap.add(array[i]);
		}
		Arrays.sort(array);
		Heap.heapify(heap);
		for(int i = 0; i < N; i++)
			if(array[i] != Heap.heappop(heap))
				System.out.println("Heapify Error!");
	}
	public static void testHeappush()
	{
		final int N = 1000;
		int[] array = new int[N]; 
		ArrayList<Integer> heap = new ArrayList<Integer>();
		for(int i = 0; i < N; i++)
		{
			array[i] = myrand.nextInt(N);
			Heap.heappush(heap, array[i]);
		}
		Arrays.sort(array);
		for(int i = 0; i < N; i++)
			if(array[i] != Heap.heappop(heap))
				System.out.println("Heapify Error!");
	}
	public static void main(String[] argv)
	{

	}
}
