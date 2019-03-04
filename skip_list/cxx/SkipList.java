import java.lang.Math;
import java.util.ArrayList;
import java.util.List;

public class SkipList
{
	public class SkipNode
	{
		public int value;
		public List<SkipNode> nextNodes;
		public SkipNode(int value)
		{
			this.value = value;
			nextNodes = new ArrayList<SkipNode>();
		}
		public int level()
		{
			return nextNodes.size()-1;
		}
	}

	private SkipNode head;
	private int maxLevel;
	private int size;
	private static double probability = 0.5;

	public SkipList()
	{
		size = 0;
		maxLevel = 0;
		// a SkipNode with value null marks the beginning
		head = new SkipNode(Integer.MIN_VALUE);
		// null marks the end
		head.nextNodes.add(null); 
	}
	public boolean add(int value)
	{
		if(contains(value))
			return false;
		size++;
		// random number from 0 to maxLevel+1 (inclusive)
		int level = 0; 
		while(Math.random() < probability)
			level++;
		while(level > maxLevel)
		{
			head.nextNodes.add(null);
			maxLevel++;
		}
		SkipNode newNode = new SkipNode(value);
		SkipNode current = head;
		do
		{
			current = findNext(e,current,level);
			newNode.nextNodes.add(0,current.nextNodes.get(level));
			current.nextNodes.set(level,newNode);
		} while (level-- > 0);
		return true;
	}
}
