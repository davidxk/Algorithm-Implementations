#include "Trie.h"

#include <iostream>
#include <cassert>

void test_insert_search()
{
	string setA[] = { "A", "a", "aa", "aal", "aalii", "aam", "Aani",
		"aardvark", "aardwolf", "Aaron", "Aaronic", "Aaronical", "Aaronite",
		"Aaronitic", "Aaru", "Ab", "aba", "Ababdeh", "Ababua", "abac", "abaca",
		"abacate", "abacay", "abacinate"
	};
	string setB[] = { "B", "b", "ba", "baa", "baahling", "Baal", "baal",
		"Baalath", "Baalish", "Baalism", "Baalist", "Baalite", "Baalitical",
		"Baalize", "Baalshem", "baar", "Bab", "baba", "babacoote", "babai",
		"babasco", "babassu", "babaylan", "Babbie"
	};
	Trie trie;
	for(const string& word: setA)
		trie.insert(word);
	for(const string& word: setA)
		assert(trie.search(word));
	for(const string& word: setB)
		assert(not trie.search(word));
}

void test_start_with()
{
	std::string words[] = { "aalii",  "aam",  "Aani", "aardvark", "aardwolf",
		"Aaronic", "Aaronite", "Aaronitic", "Aaru", "Ababdeh", "Ababua",
		"abacay", "abacinate"
	};
	std::string prefixes[] = {"A","a","aa","aal","Aaron","Ab","aba","abac"};
	std::string others[] = {
		"abaciscus","abacist","aback","abactinal","Abe","abaction"
	};
	Trie trie;
	for(const string& word: words)
		trie.insert(word);
	for(const string& prefix: prefixes)
		assert(trie.startWith(prefix));
	for(const string& word: others)
		assert(not trie.startWith(word));
}

int main()
{
	test_insert_search();
	test_start_with();
	return 0;
}
