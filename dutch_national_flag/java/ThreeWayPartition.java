// Remember the swap(a, b) in java is a = b ^ a ^ (b = a)

public class ThreeWayPartition
{
	static public void partition(int[] array)
	{
		int head = 0, tail = array.length - 1;
		int i = 0;
		while(i <= tail)
		{
			if(array[i] == 0)
			{
				array[i] = array[head] ^ array[i] ^ (array[head] = array[i]);
				i++; head++;
			}
			else if(array[i] == 2)
			{
				array[i] = array[tail] ^ array[i] ^ (array[tail] = array[i]);
				tail--;
			}
			else
				i++;
		}
	}
}
