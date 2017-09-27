import java.util.HashMap;

public class Trie
{
	public class TrieNode
	{
		public char character; 
		public HashMap<Character, TrieNode> children;
		public boolean isLeaf;
		public TrieNode(char x)
		{
			character = x;
			children = new HashMap<Character, TrieNode>();
			isLeaf = false;
		}
	}

	public TrieNode root;
	public Trie()
	{
		this.root = new TrieNode('!');
	}
	public void insert(String word)
	{
		TrieNode root = this.root;
		for(int i = 0; i < word.length(); i++)
		{
			if(!root.children.containsKey(word.charAt(i)))
				root.children.put(word.charAt(i), new TrieNode(word.charAt(i)));
			root = root.children.get(word.charAt(i));
		}
		root.isLeaf = true;
	}
	public boolean search(String word)
	{
		TrieNode root = this.root;
		for(int i = 0; i < word.length(); i++)
		{
			if(!root.children.containsKey(word.charAt(i)))
				return false;
			root = root.children.get(word.charAt(i));
		}
		return root.isLeaf;
	}
	public boolean startWith(String prefix)
	{
		TrieNode root = this.root;
		for(int i = 0; i < prefix.length(); i++)
		{
			if(!root.children.containsKey(prefix.charAt(i)))
				return false;
			root = root.children.get(prefix.charAt(i));
		}
		return true;
	}
}
