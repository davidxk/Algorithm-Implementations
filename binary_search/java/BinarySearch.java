
public class BinarySearch
{
	public static int search(int[] array, int target)
	{
		int left = 0, right = array.length - 1, center = 0;
		while(left <= right)
		{
			center = left + (right - left) / 2;
			if(array[center] == target)
				return center;
			else if(array[center] < target)
				left = center + 1;
			else
				right = center - 1;
		}
		return -1;
	}
	public static int lower(int[] array, int target)
	{
		int left = 0, right = array.length - 1, center = 0;
		while(left <= right)
		{
			center = left + (right - left) / 2;
			if(array[center] == target)
				right = center - 1;
			else if(array[center] < target)
				left = center + 1;
			else
				right = center - 1;
		}
		return right;
	}
	public static int higher(int[] array, int target)
	{
		int left = 0, right = array.length - 1, center = 0;
		while(left <= right)
		{
			center = left + (right - left) / 2;
			if(array[center] == target)
				left = center + 1;
			if(array[center] < target)
				left = center + 1;
			else
				right = center - 1;
		}
		return left;
	}
}
