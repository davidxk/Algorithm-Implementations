import java.util.HashMap;

public class DisjointSet
{
	private HashMap<Integer, Integer> parent;
	private HashMap<Integer, Integer> height;
	public DisjointSet()
	{
		parent = new HashMap<Integer, Integer>();
		height = new HashMap<Integer, Integer>();
	}
	public void makeSet(int elem)
	{
		parent.put(elem, elem);
		height.put(elem, 0);
	}
	public int findSet(int elem)
	{
		if(parent.get(elem) != elem)
			parent.put(elem, findSet(parent.get(elem)));
		return parent.get(elem);
	}
	public void union(int elem1, int elem2)
	{
		int root1 = findSet(elem1), root2 = findSet(elem2);
		if(root1 != root2)
			link(root1, root2);
	}
	private void link(int root1, int root2)
	{
		if(height.get(root1) > height.get(root2))
		{
			parent.put(root2, root1);
			height.remove(root2);
		}
		else
		{
			if(height.get(root1) == height.get(root2))
				height.put(root2, height.get(root2) + 1);
			parent.put(root1, root2);
			height.remove(root1);
		}
	}
}
