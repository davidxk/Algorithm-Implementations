import functools

def gcd(large, small):
    while small:
        large, small = small, large % small
    return large

# Extended Euclidean Algorithm
# r = gcd(a, b) is the Bezout identity
# s, t are the Bezout coefficents where a*s + b*t = r
def egcd(a, b):
    r, nr = a, b
    s, ns = 1, 0
    t, nt = 0, 1
    while nr != 0:
        quotient = r // nr
        r, nr = nr, r - quotient * nr
        s, ns = ns, s - quotient * ns
        t, nt = nt, t - quotient * nt
    return r, s, t

# Modular multiplicative inverse
def mod_inv(a, n):
    _, s, _ = egcd(a, n)
    return s % n

# The moduli must be pairwise coprime
def chinese_remainder_theorem(moduli, remainders):
    prod = functools.reduce(lambda a, b: a * b, moduli)
    x = 0
    for i, mi in enumerate(moduli):
        Mi = prod // mi
        MiInv = mod_inv(Mi, mi)
        x += remainders[i] * Mi * MiInv
    x %= prod
    return x

def frac_ceiling(quotient, denominator):
    return 1 + (quotient - 1) // denominator
