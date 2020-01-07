class TrieNode:
    def __init__(self, x):
        self.char = x
        self.children = {}
        self.isLeaf = False

class Trie:
    def __init__(self):
        self.root = TrieNode("root")

    def add(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode(char)
            curr = curr.children[char]
        curr.isLeaf = True

    def __contains__(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.isLeaf

    def searchPrefix(self, prefix):
        def dfs(node, buf, result):
            if node.isLeaf:
                result.append(str().join(buf))
            for char, child in node.children.items():
                buf.append(char)
                dfs(child, buf, result)
                buf.pop()
            return result
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return []
            curr = curr.children[char]
        return dfs(curr, list(prefix), [])

    def containsPrefix(self, prefix):
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True

    def remove(self, word):
        stack = []
        curr = self.root
        for char in word:
            if char not in curr.children:
                raise KeyError(char)
            stack.append((curr, char))
            curr = curr.children[char]
        if not curr.isLeaf:
            raise KeyError(char)
        # Explicitly use stack the way call stack is built
        curr.isLeaf = False
        child = curr
        while stack:
            curr, char = stack.pop()
            if child.isLeaf or len(child.children) > 0:
                break
            curr.children.pop(char)
            child = curr

    def removeRecursive(self, word):
        def helper(root, word, i):
            # From subtree 'root' del 'word[i:]', return if root should be del
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
