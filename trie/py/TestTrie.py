import random
import unittest
from Trie import Trie


class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        self.case = ["A", "a", "aa", "aal", "aalii", "aam", "Aani", "aardvark",
                "aardwolf", "Aaron", "Aaronic", "Aaronite", "Aaronitic",
                "Aaru", "Ab", "Ababdeh", "Ababua", "abac", "abacay",
                "abacinate"]

    def testAddContains(self):
        words = set(self.case)
        length = len(words)/2
        setA = set()
        for i in range(length/2):
            setA.add(words.pop())
        setB = words
        for word in setA:
            self.trie.add(word)
        for word in setA:
            self.assertIn(word, self.trie)
        for word in setB:
            self.assertNotIn(word, self.trie)

    def testContainsPrefix(self):
        prefixes = set(["A", "a", "aa", "aal", "Aaron", "Ab", "aba", "abac"])
        others = ["abaciscus","abacist","aback","abactinal","Abe","abaction"]
        for word in set(self.case) - prefixes:
            self.trie.add(word)
        for prefix in prefixes:
            self.assertTrue( self.trie.containsPrefix(prefix) )
        for word in others:
            self.assertFalse( self.trie.containsPrefix(word) )

    def testRemove(self):
        for word in self.case:
            self.trie.add(word)
        while self.case:
            word = random.choice(self.case)
            self.case.remove(word)
            self.trie.remove(word)
            self.assertNotIn(word, self.trie)
            for word in self.case:
                self.assertIn(word, self.trie)

    def testRemoveRecursive(self):
        for word in self.case:
            self.trie.add(word)
        while self.case:
            word = random.choice(self.case)
            self.case.remove(word)
            self.trie.removeRecursive(word)
            self.assertNotIn(word, self.trie)
            for word in self.case:
                self.assertIn(word, self.trie)
    
    def testSearchPrefix(self):
        cases = ["a", "aa", "aam", "ab", "A", "Aa", "Aar", "Aba", "b", "Bb"]
        for word in set(self.case):
            self.trie.add(word)
        for prefix in cases:
            result = self.trie.searchPrefix(prefix)
            expect = filter(lambda word: word.startswith(prefix), self.case)
            self.assertEqual(set(result), set(expect))

if __name__ == "__main__":
    unittest.main()
