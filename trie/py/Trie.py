class TrieNode:
    def __init__(self, x):
        self.char = x
        self.children = {}
        self.isLeaf = False

class Trie:
    def __init__(self):
        self.root = TrieNode("root")

    def insert(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode(char)
            cur = cur.children[char]
        cur.isLeaf = True

    def search(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return cur.isLeaf

    def startsWith(self, prefix):
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return False
            cur = cur.children[char]
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
