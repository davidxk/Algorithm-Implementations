# -*- coding: UTF-8 -*-

import functools

# For gcd(a, b) if a < b, in the first iteration
# - large = b
# - small = a % b = a
# Now the two variables are swapped, and large > small holds
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

# Try dividing with everything between [2, √n]
# - We really only need to try deviding with primes; except we don't know which
#   number is prime in [2, √n].
# - If we solve this problem by looking for all primes less than or equal to √n
#   we will end up with a solution of O(√n * n / log n) complexity.
#
# Time Complexity:  O(√n)
# Space Complexity: O(1)
def is_prime_naive(num):
    if num == 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# 6k ± 1 optimization: 3 times faster than testing [2,√n]
# - Skipping numbers in [2, √n] that are definitely not primes:
#   - 6k     (mod 6 == 0)
#   - 6k + 2 (mod 2 == 0)
#   - 6k + 3 (mod 3 == 0)
#   - 6k + 4 (mod 2 == 0)
# - Care must be taken with 2 3 5 7
#
# Time Complexity:  O(√n / 3)
# Space Complexity: O(1)
def is_prime(num):
    if num in (2, 3, 5, 7):
        return True
    elif num == 1 or num % 2 == 0 or num % 3 == 0:
        return False
    six_x = 6
    while True:
        if num % (six_x - 1) == 0 or num % (six_x + 1) == 0:
            return False
        if (six_x - 1) ** 2 > num:
            break
        six_x += 6
    return True

# Try dividing with everything between [2, √n]
# - Since primes are always smaller than any of their composites, they always
#   come ealier during the iteration.
# - If divisible, remove 1 instance of the prime through division
#
# Time Complexity:  O(√n)
# Space Complexity: O(log n)
def prime_factors(num):
    i = 2
    factors = []
    while i * i <= n:
        if n % i == 0:
            n //= i
            factors.append(i)
        else:
            i += 1
    if n > 1:
        factors.append(n)
    return factors

# Prime harmonic series 1/2 + 1/3 + 1/5 + 1/7 + ... asymptotically = log log n
# Time Complexity:  O(n log log n)
# Space Complexity: O(n)
def sieve_of_eratosthenes(n):
    is_composite = [False] * (n + 1)
    primes = []
    for num in range(2, n + 1):
        if not is_composite[num]:
            primes.append(num)
            for composite in range(num * num, n + 1, num):
                is_composite[composite] = True
    return primes
