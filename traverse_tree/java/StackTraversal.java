
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
		TreeNode cur = root;
		while(cur != null || stack.peekFirst() != null)
		{
			while(cur != null)
			{
				result.add(cur.val);
				stack.addFirst(cur);
				cur = cur.left;
			}
			cur = stack.pollFirst();
			cur = cur.right;
		}
		return result;
	}
	public List<Integer> inorderTraversal(TreeNode root)
	{
		List<Integer> result = new ArrayList<Integer>();
		ArrayDeque<TreeNode> stack = new ArrayDeque<TreeNode>();
		TreeNode cur = root;
		while(cur != null || stack.peekFirst() != null)
		{
			while(cur != null)
			{
				stack.addFirst(cur);
				cur = cur.left;
			}
			cur = stack.pollFirst();
			result.add(cur.val);
			cur = cur.right;
		}
		return result;
	}
	public List<Integer> postorderTraversal(TreeNode root)
	{
		List<Integer> result = new ArrayList<Integer>();
		ArrayDeque<TreeNode> stack = new ArrayDeque<TreeNode>();
		TreeNode cur = root;
		while(cur != null || stack.peekFirst() != null)
		{
			while(cur != null)
			{
				result.add(cur.val);
				stack.addFirst(cur);
				cur = cur.right;
			}
			cur = stack.pollFirst();
			cur = cur.left;
		}
		Collections.reverse(result);
		return result;
	}
}
