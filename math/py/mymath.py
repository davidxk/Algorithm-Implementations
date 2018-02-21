
def gcd(big, small):
    while small:
        big, small = small, big % small
    return big
