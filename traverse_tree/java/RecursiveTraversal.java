import java.util.ArrayList;
import java.lang.Integer;
import java.util.List;

public class RecursiveTraversal implements TraversalMethods
{
	public List<Integer> preorderTraversal(TreeNode root)
	{
		List<Integer> result = new ArrayList<Integer>();
		preorderHelper(root, result);
		return result;
	}
	private void preorderHelper(TreeNode root, List<Integer> result)
	{
		if(root != null)
		{
			result.add(root.val);
			preorderHelper(root.left, result);
			preorderHelper(root.right, result);
		}
	}
	public List<Integer> inorderTraversal(TreeNode root)
	{
		List<Integer> result = new ArrayList<Integer>();
		inorderHelper(root, result);
		return result;
	}
	private void inorderHelper(TreeNode root, List<Integer> result)
	{
		if(root != null)
		{
			inorderHelper(root.left, result);
			result.add(root.val);
			inorderHelper(root.right, result);
		}
	}
	public List<Integer> postorderTraversal(TreeNode root)
	{
		List<Integer> result = new ArrayList<Integer>();
		postorderHelper(root, result);
		return result;
	}
	private void postorderHelper(TreeNode root, List<Integer> result)
	{
		if(root != null)
		{
			postorderHelper(root.left, result);
			postorderHelper(root.right, result);
			result.add(root.val);
		}
	}
}
