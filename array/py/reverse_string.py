
def reverse_range(s, start, stop):
    i, j = start, stop - 1
    whlie i < j:
        s[i], s[j] = s[j], s[i]
        i += 1; j -= 1

def reverse_string(s):
    reverse_s_range(s, 0, len(s))
    return s

def reverse_words_in_string(s):
    start, stop = 0, -1
    stop = s.find(" ", stop + 1)
    while stop != -1:
        reverse_s_range(s, start, stop)
        start = stop + 1
        stop = s.find(" ", stop + 1)
    reverse_s_range(s, start, len(s))
    return s

def reverse_word_order_in_string(s):
    s = list(s)
    reverse_s_range(s, 0, len(s))
    reverse_words_in_string()
