import java.util.*;

class MajorityVote
{
	public static int majorityVote(int[] nums)
	{
		int candy = -1, count = 0;
		for(int num: nums)
			if(count == 0)
			{
				candy = num;
				count = 1;
			}
			else if(num == candy)
				count++;
			else
				count--;
		if(countOccurrence(nums, candy) > nums.length / 2)
			return candy;
		return -1;
	}
	public static List<Integer> majorityVoteGeneral(int[] nums, int k)
	{
		List<Integer> result = new ArrayList<Integer>();
		if(nums.length < k)
		{
			Set<Integer> dedup = new HashSet<Integer>();
			for(int num: nums)
				dedup.add(num);
			result.addAll(dedup);
			return result;
		}
		Map<Integer, Integer> count = new HashMap<Integer, Integer>();
		for(int num: nums)
		{
			if(count.containsKey(num) || count.size() < k - 1)
				count.put(num, count.getOrDefault(num, 0));
			else
			{
hasZero:
				{
					for(int key: count.keySet())
						if(count.get(key) == 0)
						{
							count.remove(key);
							count.put(num, 1);
							break hasZero;
						}
					for(int key: count.keySet())
						count.put(key, count.get(key) - 1);
				}
			}
		}
		for(int key: count.keySet())
			if(countOccurrence(nums, key) > nums.length / k)
				result.add(key);
		return result;
	}
	private static int countOccurrence(int nums[], int target)
	{
		int count = 0;
		for(int num: nums)
			if(target == num)
				count++;
		return count;
	}
}
