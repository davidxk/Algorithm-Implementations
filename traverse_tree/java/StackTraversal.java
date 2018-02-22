import java.lang.Integer;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class StackTraversal implements TraversalMethods
{
	public List<Integer> preorderTraversal(TreeNode root)
	{
		List<Integer> result = new ArrayList<Integer>();
		ArrayDeque<TreeNode> stack = new ArrayDeque<TreeNode>();
		TreeNode curr = root;
		while(curr != null || stack.peekFirst() != null)
		{
			while(curr != null)
			{
				result.add(curr.val);
				stack.addFirst(curr);
				curr = curr.left;
			}
			curr = stack.pollFirst();
			curr = curr.right;
		}
		return result;
	}
	public List<Integer> inorderTraversal(TreeNode root)
	{
		List<Integer> result = new ArrayList<Integer>();
		ArrayDeque<TreeNode> stack = new ArrayDeque<TreeNode>();
		TreeNode curr = root;
		while(curr != null || stack.peekFirst() != null)
		{
			while(curr != null)
			{
				stack.addFirst(curr);
				curr = curr.left;
			}
			curr = stack.pollFirst();
			result.add(curr.val);
			curr = curr.right;
		}
		return result;
	}
	public List<Integer> postorderTraversal(TreeNode root)
	{
		class MyPair {
			public TreeNode node; public boolean visited;
			public MyPair(TreeNode node, boolean visited) {
				this.node = node; this.visited = visited;
			}
		}

		List<Integer> result = new ArrayList<Integer>();
		ArrayDeque<MyPair> stack = new ArrayDeque<MyPair>();
		TreeNode curr = root;
		while(curr != null || stack.peekFirst() != null)
		{
			while(curr != null)
			{
				stack.addFirst(new MyPair(curr, false));
				curr = curr.left;
			}
			MyPair stackTop = stack.peek();
			if(stackTop.visited == false)
			{
				stackTop.visited = true;
				curr = stackTop.node.right;
			}
			else
			{
				stack.pop();
				result.add(stackTop.node.val);
			}
		}
		return result;
	}
}
