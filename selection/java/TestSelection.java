import java.util.ArrayList;
import java.util.Arrays;
import java.util.Random;

public class TestSelection
{
	private static Random myrand = new Random();
	private static boolean checkSelection(int[] array, int rank, int retval)
	{
		Arrays.sort(array);
		return retval == array[rank - 1];
	}
	private static boolean testRandomCases(SelectionAlgorithm func)
	{
		final int n = 5000;
		int[] array = new int[n];
		for(int i = 0; i < 1000; i++)
		{
			for(int j = 0; j < array.length; j++)
				array[j] = myrand.nextInt(2 * n);
			int[] clone = array.clone();
			int rank = 1 + myrand.nextInt(array.length);
			int retval = func.select(array, rank);
			if(!checkSelection(array, rank, retval))
			{
				System.out.println(Arrays.toString(clone));
				System.out.println("at rank# " + rank);
				System.out.println(retval);
				System.out.println(array[rank - 1]);
				return false;
			}
		}
		return true;
	}
	private static boolean testSmallCases(SelectionAlgorithm func)
	{
		int retval, expect;
		for(int i = 1; i < 50; i++)
		{
			int[] testcase = new int[i];
			for(int j = 0; j < i; j++)
				testcase[j] = j;
			for(int j = 1; j <= i; j++)
				if(func.select(testcase, j)!= j - 1)
					return false;
			for(int j = i - 1; j >= 0; j--)
				testcase[j] = j;
			for(int j = 1; j <= i; j++)
				if(func.select(testcase, j)!= i - j)
					return false;
		}
		return true;
	}
	private static boolean testStaticCases(SelectionAlgorithm func)
	{
		int[][] cases = {
			{27, 62, 40, 39, 68, 11, 97, 94, 91, 98, 40, 1, 70, 8, 78, 14, 3, 95, 38, 0, 53, 65, 63, 20, 28, 14, 89, 33, 70, 59, 37, 42, 69, 4, 96, 42, 37, 50, 71, 84, 27, 33, 18, 73, 24, 98, 14, 92, 84, 9}, { 40, 92, 26, 22, 18, 89, 15, 0, 28, 17, 10, 99, 76, 41, 27, 10, 23, 0, 95, 83, 70, 10, 73, 78, 43, 26, 84, 74, 84, 75, 59, 67, 76, 60, 82, 52, 18, 34, 3, 37, 70, 27, 28, 74, 82, 64, 44, 39, 74, 30 }, { 65, 80, 30, 85, 84, 22, 18, 39, 99, 29, 64, 48, 4, 3, 3, 57, 83, 31, 45, 99, 27, 29, 75, 21, 90, 73, 78, 24, 41, 26, 63, 99, 89, 84, 36, 8, 82, 94, 45, 59, 34, 62, 53, 80, 24, 73, 44, 67, 79, 71 }, { 86, 99, 77, 60, 35, 69, 49, 31, 21, 22, 28, 47, 32, 27, 71, 3, 89, 10, 73, 72, 47, 47, 35, 81, 26, 88, 23, 81, 50, 31, 32, 30, 60, 11, 1, 81, 13, 83, 75, 26, 48, 99, 93, 49, 23, 97, 23, 45, 82, 93 }
		};
		int[] ranks = { 25, 47, 25, 38 };
		int[] expect = { 42, 89, 57, 81 };
		for(int i = 0; i < cases.length; i++)
			if(func.select(cases[i], ranks[i]) != expect[i])
				return false;
		return true;
	}
	public static void main(String[] argv)
	{
		ArrayList<SelectionAlgorithm> funcs = new ArrayList<SelectionAlgorithm>();
		funcs.add(new RandomizedSelect());
		funcs.add(new BFPRTSelect());
		for(SelectionAlgorithm func: funcs)
			if(!testStaticCases(func))
				System.out.println("WA: static " + func.toString());
			else if(!testSmallCases(func) && !testRandomCases(func))
				System.out.println("WA: " + func.toString());
			else
				System.out.println(func.toString() + " done");
	}
}
