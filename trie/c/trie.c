#include "trie.h"
#include <stdlib.h>
#include <string.h>

void trie_node_init(TrieNode* node, char x)
{
	node->character = x;
	node->isLeaf = 0;
	int i;
	for(i = 0; i < 26; i++)
		node->children[i] = NULL;
}

void trie_init(Trie* trie)
{
	trie->root = (TrieNode*) malloc(sizeof(TrieNode));
	trie_node_init(trie->root, '!');

	trie->insert = trie_insert;
	trie->search = trie_search;
	trie->startWith = trie_start_with;
	trie->destroy = trie_destroy;
}

void trie_insert(Trie* trie, const char* word)
{
	TrieNode* root = trie->root;
	int i;
	TrieNode* node = NULL;
	for(i = 0; i < strlen(word); i++)
	{
		if(root->children[word[i] - 'a'] == NULL)
		{
			node = (TrieNode*) malloc(sizeof(TrieNode));
			trie_node_init(node, word[i]);
			root->children[word[i] - 'a'] = node;
		}
		root = root->children[word[i] - 'a'];
	}
	root->isLeaf = 1;
}

int trie_search(Trie* trie, const char* word)
{
	TrieNode* root = trie->root;
	int i;
	for(int i = 0; i < strlen(word); i++)
	{
		if(root->children[word[i] - 'a'] == NULL)
			return 0;
		root = root->children[word[i] - 'a'];
	}
	return root->isLeaf == 1;
}

int trie_start_with(Trie* trie, const char* prefix)
{
	TrieNode* root = trie->root;
	int i;
	for(int i = 0; i < strlen(prefix); i++)
	{
		if(root->children[prefix[i] - 'a'] == NULL)
			return 0;
		root = root->children[prefix[i] - 'a'];
	}
	return 1;
}

void trie_free_subtree(TrieNode* root)
{
	int i;
	for(i = 0; i < 26; i++)
		if(root->children[i])
			trie_free_subtree(root->children[i]);
	free(root);
}

void trie_destroy(Trie* trie)
{
	trie_free_subtree(trie->root);
}
