package main

// UNTESTED

// TrieNode is a node in a Trie
type TrieNode struct {
	Children map[rune]*TrieNode
	IsLeaf   bool
}

// Trie is a prefix tree
type Trie struct {
	Root *TrieNode
}

// Insert adds a word in the Trie
func (t *Trie) Insert(word string) {
	curr := t.Root
	for _, char := range word {
		if _, ok := curr.Children[char]; !ok {
			curr.Children[char] = &TrieNode{}
		}
		curr = curr.Children[char]
	}
	curr.IsLeaf = true
}

// Search finds if a word in the Trie
func (t *Trie) Search(word string) bool {
	curr := t.Root
	for _, char := range word {
		if _, ok := curr.Children[char]; !ok {
			return false
		}
		curr = curr.Children[char]
	}
	return curr.IsLeaf
}

// StartWith returns if there are words in the Trie that starts with the prefix
func (t *Trie) StartWith(prefix string) bool {
	curr := t.Root
	for _, char := range prefix {
		if _, ok := curr.Children[char]; !ok {
			return false
		}
		curr = curr.Children[char]
	}
	return true
}
