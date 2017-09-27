#include "Trie.h"

#include <iostream>
using namespace std;

void Trie::insert(const string& word)
{
	TrieNode* curr = root;
	for(int i = 0; i < word.length(); i++)
	{
		if(curr->children.find(word.at(i)) == curr->children.end())
			curr->children.emplace(word.at(i), new TrieNode(word.at(i)));
		curr = curr->children[word.at(i)];
	}
	curr->isLeaf = true;
}

bool Trie::search(const string& word)
{
	TrieNode* curr = root;
	for(int i = 0; i < word.size(); i++)
	{
		if(curr->children.find(word[i]) == curr->children.end())
			return false;
		curr = curr->children[word[i]];
	}
	return curr->isLeaf == true;
}

bool Trie::startWith(const string& prefix)
{
	TrieNode* curr = root;
	for(int i = 0; i < prefix.size(); i++)
	{
		if(curr->children.find(prefix[i]) == curr->children.end())
			return false;
		curr = curr->children[prefix[i]];
	}
	return true;
}

void Trie::deleteSubtree(TrieNode* root)
{
	for(auto it = root->children.begin(); it != root->children.end(); it++)
		deleteSubtree(it->second);
	delete root;
}

Trie::~Trie()
{
	deleteSubtree(this->root);
}
