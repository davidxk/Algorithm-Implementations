#include <vector>
#include <unordered_map>
using namespace std;

class TrieNode
{
public:
	TrieNode(char x): character(x) { }
	unordered_map<char, TrieNode*> children;
	char character;
	bool isLeaf;
};

class Trie
{
public:
	Trie() { root = new TrieNode('!'); }
	void insert(const string& word);
	bool search(const string& word);
	bool startWith(const string& prefix);
	~Trie();
private:
	TrieNode* root;
	void deleteSubtree(TrieNode* root);
};
