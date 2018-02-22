import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.ArrayDeque;
import java.util.Random;
import java.lang.Integer;

public class TestTraversal
{
	private static Random myrand = new Random();
	private static int pickAndTake(List<Integer> pool, int size)
	{
		int randPick = myrand.nextInt(size);
		int result = pool.get(randPick);
		pool.set(randPick, pool.get(size - 1));
		return result;
	}
	public static TreeNode generateRandomTree(int size)
	{
		List<Integer> pool = new ArrayList<Integer>();
		for(int i  = 0; i < size; i++)
			pool.add(i);
		Collections.shuffle(pool);

		TreeNode root = new TreeNode(pickAndTake(pool, size--));
		ArrayDeque<TreeNode> queue = new ArrayDeque<TreeNode>();
		queue.addLast(root);
		for(int i  = 1; i < size - 1; i++)
		{
			TreeNode node = queue.pollFirst();
			if(myrand.nextFloat() < 0.7)
			{
				node.left = new TreeNode(pickAndTake(pool, size--));
				queue.addLast(node.left);
				i++;
			}
			if(myrand.nextFloat() < 0.7 || queue.peekFirst() == null)
			{
				node.right = new TreeNode(pickAndTake(pool, size--));
				queue.addLast(node.right);
				i++;
			}
		}
		return root;
	}
	public static boolean testTraversalMethod(TraversalMethods impl, int size)
	{
		TreeNode root = generateRandomTree(size);
		String tag[] = { "preorder", "inorder", "postorder" };
		RecursiveTraversal rcur = new RecursiveTraversal();

		List<List<Integer>> ans = new ArrayList<List<Integer>>();
		ans.add( rcur.preorderTraversal(root) );
		ans.add( rcur.inorderTraversal(root) );
		ans.add( rcur.postorderTraversal(root) );

		ArrayList<List<Integer>> ret = new ArrayList<List<Integer>>();
		ret.add( impl.preorderTraversal(root) );
		ret.add( impl.inorderTraversal(root) );
		ret.add( impl.postorderTraversal(root) );

		for(int i = 0; i < 3; i++)
		{
			if(ret.get(i).size() != ans.get(i).size())
			{
				System.out.println(tag[i] + " answer length error");
				return false;
			}
			for(int j = 0; j < ans.get(i).size(); j++)
				if(ret.get(i).get(j).compareTo(ans.get(i).get(j)) != 0)
				{
					System.out.println(tag[i] + " result error");
					return false;
				}
		}
		return true;
	}
	public static void main(String[] argv)
	{
		TraversalMethods impls[] = {
			new StackTraversal(), new MorrisTraversal() };
		for(TraversalMethods impl: impls)
		{
			int cases = 500;
			for(int i = 0; i < cases; i++)
				if(!testTraversalMethod(impl, 200))
				{
					System.out.println("WA: " + impl);
					break;
				}
		}
	}
}
