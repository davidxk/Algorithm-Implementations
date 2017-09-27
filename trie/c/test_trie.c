#include <assert.h>

#include "trie.h"

void test_insert_search()
{
	char* setA[24] = { "A", "a", "aa", "aal", "aalii", "aam", "Aani",
		"aardvark", "aardwolf", "Aaron", "Aaronic", "Aaronical", "Aaronite",
		"Aaronitic", "Aaru", "Ab", "aba", "Ababdeh", "Ababua", "abac", "abaca",
		"abacate", "abacay", "abacinate"
	};
	char* setB[24] = { "B", "b", "ba", "baa", "baahling", "Baal", "baal",
		"Baalath", "Baalish", "Baalism", "Baalist", "Baalite", "Baalitical",
		"Baalize", "Baalshem", "baar", "Bab", "baba", "babacoote", "babai",
		"babasco", "babassu", "babaylan", "Babbie"
	};
	Trie trie;
	trie_init(&trie);
	int i;
	for(i = 0; i < 24; i++)
		trie.insert(&trie, setA[i]);
	for(i = 0; i < 24; i++)
		assert(trie.search(&trie, setA[i]));
	for(i = 0; i < 24; i++)
		assert(!trie.search(&trie, setB[i]));
}

void test_start_with()
{
	char* words[13] = { "aalii",  "aam",  "Aani", "aardvark", "aardwolf",
		"Aaronic", "Aaronite", "Aaronitic", "Aaru", "Ababdeh", "Ababua",
		"abacay", "abacinate"
	};
	char* prefixes[8] = {"A","a","aa","aal","Aaron","Ab","aba","abac"};
	char* others[6] = {
		"abaciscus","abacist","aback","abactinal","Abe","abaction"
	};
	Trie trie;
	trie_init(&trie);
	int i;
	for(i = 0; i < 13; i++)
		trie.insert(&trie, words[i]);
	for(i = 0; i < 8; i++)
		assert(trie.startWith(&trie, prefixes[i]));
	for(i = 0; i < 6; i++)
		assert(!trie.startWith(&trie, others[i]));
}

int main()
{
	test_insert_search();
	test_start_with();
	return 0;
}
