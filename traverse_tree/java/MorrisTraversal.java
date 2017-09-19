import java.lang.Integer;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class MorrisTraversal implements TraversalMethods
{
	public List<Integer> preorderTraversal(TreeNode root)
	{
		List<Integer> result = new ArrayList<Integer>();
		TreeNode cur = root, node = null;
		while(cur != null)
		{
			if(cur.left == null)
			{
				result.add(cur.val);
				cur = cur.right;
			}
			else
			{
				node = cur.left;
				while(node.right != null && node.right != cur)
					node = node.right;

				if(node.right == null)
				{
					result.add(cur.val);
					node.right = cur;
					cur = cur.left;
				}
				else
				{
					node.right = null;
					cur = cur.right;
				}
			}
		}
		return result;
	}
	public List<Integer> inorderTraversal(TreeNode root)
	{
		List<Integer> result = new ArrayList<Integer>();
		TreeNode cur = root, node = null;
		while(cur != null)
		{
			if(cur.left == null)
			{
				result.add(cur.val);
				cur = cur.right;
			}
			else
			{
				node = cur.left;
				while(node.right != null && node.right != cur)
					node = node.right;

				if(node.right == null)
				{
					node.right = cur;
					cur = cur.left;
				}
				else
				{
					node.right = null;
					result.add(cur.val);
					cur = cur.right;
				}
			}
		}
		return result;
	}
	public List<Integer> postorderTraversal(TreeNode root)
	{
		List<Integer> result = new ArrayList<Integer>();

		TreeNode dummy = new TreeNode(-1);
		dummy.left = root;
		TreeNode cur = dummy, node = null;
		while(cur != null)
		{
			if(cur.left == null)
			{
				cur = cur.right;
			}
			else
			{
				node = cur.left;
				while(node.right != null && node.right != cur)
					node = node.right;

				if(node.right == null)
				{
					node.right = cur;
					cur = cur.left;
				}
				else
				{
					backTrack(cur.left, node, result);
					node.right = null;
					cur = cur.right;
				}
			}
		}
		return result;
	}
	public void backTrack(TreeNode from, TreeNode to, List<Integer> result)
	{
		List<Integer> reverse = new ArrayList<Integer>();
		TreeNode cur = from;
		while(cur != to)
		{
			reverse.add(cur.val);
			cur = cur.right;
		}
		reverse.add(to.val);
		Collections.reverse(reverse);
		result.addAll(reverse);
	}
}
