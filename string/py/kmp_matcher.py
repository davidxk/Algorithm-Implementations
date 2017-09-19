
def kmp_matcher(text, pattern):
    pi = compute_prefix_function(pattern)
    matched = 0
    for i, char in enumerate(text):
        while matched > 0 and pattern[matched] != text[i]:
            matched = pi[matched - 1]
        if pattern[matched] == text[i]:
            matched += 1
        if matched == len(pattern):
            return i - len(pattern) + 1
    return -1

def compute_prefix_function(pattern):
    pi = [0] * len(pattern)
    matched = 0
    for i in range(1, len(pattern)):
        while matched > 0 and pattern[i] != pattern[matched]:
            matched = pi[matched - 1]
        if pattern[i] == pattern[matched]:
            matched += 1
        pi[i] = matched
    return pi

if __name__ == '__main__':
    print kmp_matcher("hello world", "or")
    print kmp_matcher("mississippi", "issip")
    print kmp_matcher("bbaa", "aab")
