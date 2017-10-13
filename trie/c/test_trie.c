#include <assert.h>

#include "trie.h"

void test_insert_search()
{
	char* setA[24] = { "a", "a", "aa", "aal", "aalii", "aam", "aani",
		"aardvark", "aardwolf", "aaron", "aaronic", "aaronical", "aaronite",
		"aaronitic", "aaru", "ab", "aba", "ababdeh", "ababua", "abac", "abaca",
		"abacate", "abacay", "abacinate"
	};
	char* setB[24] = { "b", "b", "ba", "baa", "baahling", "baal", "baal",
		"baalath", "baalish", "baalism", "baalist", "baalite", "baalitical",
		"baalize", "baalshem", "baar", "bab", "baba", "babacoote", "babai",
		"babasco", "babassu", "babaylan", "babbie"
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
	trie.destroy(&trie);
}

void test_start_with()
{
	char* words[13] = { "aalii",  "aam",  "aani", "aardvark", "aardwolf",
		"aaronic", "aaronite", "aaronitic", "aaru", "ababdeh", "ababua",
		"abacay", "abacinate"
	};
	char* prefixes[8] = {"a","a","aa","aal","aaron","ab","aba","abac"};
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
	trie.destroy(&trie);
}

int main()
{
	test_insert_search();
	test_start_with();
	return 0;
}
