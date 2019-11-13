
public class BFPRTSelect implements SelectionAlgorithm
{
	public void insertion_sort(int[] array, int left, int right)
	{
		for(int i = left + 1; i < right + 1; i++)
		{
			int x = array[i];
			int j = i - 1;
			while(j >= left && array[j] > x)
			{
				array[j + 1] = array[j];
				j--;
			}
			array[j + 1] = x;
		}
	}
	public int median5(int[] array, int left, int right)
	{
		insertion_sort(array, left, right);
		return (left + right) / 2;
	}
	public int median_of_medians(int[] array, int left, int right)
	{
		if(right - left < 5)
			return median5(array, left, right);
		int subright, index, gid;
		for(int i = left; i < right + 1; i += 5)
		{
			subright = i + 4;    // 1 + 4 == 5
			if(subright > right)
				subright = right;
			index = median5(array, i, subright);
			gid = left + (i - left) / 5;
			array[gid] = array[gid]^array[index]^(array[index] = array[gid]);
		}
		return m_select(array, left, left + (right - left + 1) / 5,
				(right - left) / 10 + 1);
	}
	public int partition(int[] array, int left, int right)
	{
		int index = median_of_medians(array, left, right);
		int pivot = array[index];
		array[index] = array[index]^array[right]^(array[right] = array[index]);
		int i = left, j = right - 1;
		while(true)
		{
			while(array[i] < pivot) i++;
			while(pivot < array[j] && i < j) j--;
			if(i >= j)
			{
				array[i] = array[i] ^ array[right] ^ (array[right] = array[i]);
				return i;
			}
			array[i] = array[i] ^ array[j] ^ (array[j] = array[i]);
			i++; j--;
		}
	}
	public int m_select(int[] array, int left, int right, int rank)
	{
		if(left == right)
			return left;
		int center = partition(array, left, right);
		int pivot_rank = center - left + 1;
		if(rank == pivot_rank)
			return center;
		else if(rank < pivot_rank)
			return m_select(array, left, center - 1, rank);
		else
			return m_select(array, center + 1, right, rank - pivot_rank);
	}
	public int select(int[] array, int rank)
	{
		int index = m_select(array, 0, array.length - 1, rank);
		return array[index];
	}
}
