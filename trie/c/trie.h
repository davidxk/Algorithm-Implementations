typedef struct trie_node
{
	char character;
	int isLeaf;
	struct trie_node* children[26];
} TrieNode;

typedef struct trie
{
	TrieNode* root;
	void (*insert)(struct trie* trie, const char* word);
	int (*search)(struct trie* trie, const char* word);
	int (*startWith)(struct trie* trie, const char* word);
	void (*destroy)(struct trie* trie);
} Trie;

void trie_node_init(TrieNode* node, char x);
void trie_init(Trie* trie);
void trie_insert(Trie* trie, const char* word);
int trie_search(Trie* trie, const char* word);
int trie_start_with(Trie* trie, const char* prefix);
void trie_destroy(Trie* trie);
