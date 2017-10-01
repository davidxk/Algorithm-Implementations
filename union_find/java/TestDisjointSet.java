
public class TestDisjointSet
{
	public static void testUnionFind()
	{
		DisjointSet ds = new DisjointSet();
		for(int i = 0; i < 100; i++)
		{
			ds.makeSet(i);
			ds.union(i, i % 5);
		}
		for(int i = 0; i < 100; i++)
			for(int j = 0; j < 100; j++)
				if((i % 5 == j % 5) != (ds.findSet(i) == ds.findSet(j)))
					System.out.println("Error in Union-Find");
	}
	public static void main(String[] args)
	{
		testUnionFind();
	}
}
