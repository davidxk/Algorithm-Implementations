
public class TestTrie
{
	public static void testInsertSearch()
	{
		String setA[] = { "A", "a", "aa", "aal", "aalii", "aam", "Aani",
			"aardvark", "aardwolf", "Aaron", "Aaronic", "Aaronical", "Aaronite",
			"Aaronitic", "Aaru", "Ab", "aba", "Ababdeh", "Ababua", "abac", "abaca",
			"abacate", "abacay", "abacinate"
		};
		String setB[] = { "B", "b", "ba", "baa", "baahling", "Baal", "baal",
			"Baalath", "Baalish", "Baalism", "Baalist", "Baalite", "Baalitical",
			"Baalize", "Baalshem", "baar", "Bab", "baba", "babacoote", "babai",
			"babasco", "babassu", "babaylan", "Babbie"
		};
		Trie trie = new Trie();
		for(int i = 0; i < setA.length; i++)
			trie.insert(setA[i]);
		for(int i = 0; i < setA.length; i++)
			if(trie.search(setA[i]) != true)
				System.out.println("Error in insert search");
		for(int i = 0; i < setB.length; i++)
			if(trie.search(setB[i]) == true)
				System.out.println("Error in insert search");
	}
	public static void testStartWith()
	{
		String words[] = { "aalii",  "aam",  "Aani", "aardvark", "aardwolf",
			"Aaronic", "Aaronite", "Aaronitic", "Aaru", "Ababdeh", "Ababua",
			"abacay", "abacinate"
		};
        String prefixes[] = {"A","a","aa","aal","Aaron","Ab","aba","abac"};
	 	String others[] = {
			"abaciscus","abacist","aback","abactinal","Abe","abaction"
		};
		Trie trie = new Trie();
		for(int i = 0; i < words.length; i++)
			trie.insert(words[i]);
		for(int i = 0; i < prefixes.length; i++)
			if(trie.startWith(prefixes[i]) != true)
				System.out.println("Error in start with");
		for(int i = 0; i < others.length; i++)
			if(trie.startWith(others[i]) != false)
				System.out.println("Error in start with");
	}
	public static void main(String[] args)
	{
		testInsertSearch();
		testStartWith();
	}
}
