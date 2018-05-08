class TrieNode:
    def __init__(self, x):
        self.char = x
        self.children = {}
        self.isLeaf = False

class Trie:
    def __init__(self):
        self.root = TrieNode("root")

    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode(char)
            curr = curr.children[char]
        curr.isLeaf = True

    def search(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.isLeaf

    def startsWith(self, prefix):
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True

    def delete(self, word):
        def helper(root, word, i):
            if i == len(word) and root.isLeaf:
                root.isLeaf = False
                return len(root.children) == 0
            if word[i] in root.children and \
                    helper(root.children[word[i]], word, i + 1):
                root.children.pop(word[i])
                if len(root.children) == 0 and not root.isLeaf:
                    return True
            return False
        helper(self.root, word, 0)
