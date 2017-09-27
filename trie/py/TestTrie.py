import random
import unittest
from Trie import Trie


class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        self.case = ["A", "a", "aa", "aal", "aalii", "aam", "Aani", "aardvark", "aardwolf", "Aaron", "Aaronic", "Aaronite", "Aaronitic", "Aaru", "Ab", "Ababdeh", "Ababua", "abac", "abacay", "abacinate"]

    def testInsertSearch(self):
        words = set(self.case)
        length = len(words)/2
        setA = set()
        for i in range(length/2):
            setA.add(words.pop())
        setB = words
        for word in setA:
            self.trie.insert(word)
        for word in setA:
            self.assertTrue( self.trie.search(word) )
        for word in setB:
            self.assertFalse( self.trie.search(word) )

    def testStartWith(self):
        prefixes = set(["A", "a", "aa", "aal", "Aaron", "Ab", "aba", "abac"])
        others = ["abaciscus","abacist","aback","abactinal","Abe","abaction"]
        for word in set(self.case) - prefixes:
            self.trie.insert(word)
        for prefix in prefixes:
            self.assertTrue( self.trie.startsWith(prefix) )
        for word in others:
            self.assertFalse( self.trie.startsWith(word) )

    def testDelete(self):
        for word in self.case:
            self.trie.insert(word)
        while self.case:
            word = random.choice(self.case)
            self.case.remove(word)
            self.trie.delete(word)
            self.assertFalse( self.trie.search(word) )
            for word in self.case:
                self.assertTrue( self.trie.search(word) )

if __name__ == "__main__":
    unittest.main()
