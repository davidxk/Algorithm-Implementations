
public class TestFisherYates
{
	public static void main(String[] args)
	{
		int[] array = new int[100];
		for(int i = 0; i < 100; i++)
			array[i] = i;
		FisherYates.shuffle(array);
		for(int i = 0; i < 100; i++)
			System.out.print(array[i] + " ");
		System.out.println();

		for(int i = 0; i < 100; i++)
			array[i] = i;
		FisherYates.shuffle_front(array);
		for(int i = 0; i < 100; i++)
			System.out.print(array[i] + " ");
		System.out.println();
	}
}
