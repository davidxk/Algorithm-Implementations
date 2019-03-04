The Boyer-Moore algorithm is considered as the most efficient string-matching algorithm in usual applications. A simplified version of it or the entire algorithm is often implemented in text editors for the «search» and «substitute» commands. 

The algorithm scans the characters of the pattern from right to left beginning with the rightmost one. In case of a mismatch (or a complete match of the whole pattern) it uses two precomputed functions to shift the window to the right. These two shift functions are called the **good-suffix shift** (also called matching shift) and the **bad-character shift** (also called the last occurrence shift).

The bad character rule says upon mismatch \\(P\\) is shifted so that the mismatch becomes a match. The good suffix rules says for the characters we did match, we want shift \\(P\\) such that we don't turn any of these matches into a mismatch. 

Bad character table ```bc[P[i]][char]``` is defined as the index of the last occurrence of ```char``` in ```P[:i]```. 

The suffix array here finds the smallest s where pattern[s:k] is a suffix of pattern[:]. In other words, it find the longest matching suffix of a substring (prefix) of the pattern, and saves its count of matching characters at the end of the substring. 

```python
def compute_bad_char(pattern):
	bc = {}
	for i in range(len(pattern) - 1):
		bc[pattern[i]] = len(pattern) - i + 1

def compute_suffix_array(pattern):
	matched = 0
	suffix = [m for i in range(len(pattern))]
	for i in range(len(pattern) - 2, -1, -1):
		g = i
		while g >= 0 and pattern[g] == pattern[g + len(pattern) - 1 - i]:
			g -= 1
		suffix[i] = i - g
	return suffix

def compute_good_suffix(pattern):
	gs = [len(pattern) for i in range(len(pattern))]
			
```
