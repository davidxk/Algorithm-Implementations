#include <vector>
#include <unordered_map>

class TrieNode
{
public:
	TrieNode(char x): character(x) { }
	std::unordered_map<char, TrieNode*> children;
	char character;
	bool isLeaf;
};

class Trie
{
public:
	Trie() { root = new TrieNode('!'); }
	void insert(const std::string& word);
	bool search(const std::string& word);
	bool startWith(const std::string& prefix);
	~Trie();
private:
	TrieNode* root;
	void deleteSubtree(TrieNode* root);
};
