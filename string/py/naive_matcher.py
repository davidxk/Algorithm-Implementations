# Time:  O(nk)
# Space: O(1)

def naive_matcher(pattern, text):
    for i in range(len(text) - len(pattern) + 1):
        for j in range(len(pattern)):
            if text[i + j] != pattern[j]:
                break
        else:
            return i
    return -1
