# Time:  O(n) text
# Space: O(k) pattern

def kmp_matcher(pattern, text):
    pi = compute_prefix_function(pattern)
    matched = 0
    for i in range(len(text)):
        while matched > 0 and pattern[matched] != text[i]:
            matched = pi[matched - 1]
        if pattern[matched] == text[i]:
            matched += 1
        if matched == len(pattern):
            return i + 1 - len(pattern)
    return -1

# pi is a jump table indicating which index in pattern you should match next 
# pi[i] = how many you have matched given you have matched pattern[0 .. i]
# In other words, where to jump when you are at character pattern[i]
# Since we know pattern[0 .. i] won't work because pattern[i + 1] doesn't match
# We never jump at index 0 because there is no more character behind it
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
