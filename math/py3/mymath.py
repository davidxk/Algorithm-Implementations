
def gcd(large, small):
    while small:
        large, small = small, large % small
    return large
