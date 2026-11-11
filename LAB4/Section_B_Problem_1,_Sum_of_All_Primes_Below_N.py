
import time

# METHOD 1: NAIVE PRIME SUMMATION

def sum_primes_naive(n):
    total = 0

    for x in range(2, n):
        is_prime = True

        for d in range(2, x):
            if x % d == 0:
                is_prime = False
                break

        if is_prime:
            total += x

    return total


print("FIRST METHOD: NAIVE")

test_cases = [(10, 17), (30, 129), (100, 1060), (1000, 76127)]

for n, expected in test_cases:
    got = sum_primes_naive(n)
    print(n, got, "PASS" if got == expected else "FAIL")

n = 50000
start = time.time()
result = sum_primes_naive(n)
end = time.time()
print(f"N = {n}, sum = {result}, time = {end - start:.4f} s")

n = 100000
start = time.time()
result = sum_primes_naive(n)
end = time.time()
print(f"N = {n}, sum = {result}, time = {end - start:.4f} s")


# METHOD 2: SQUARE ROOT OPTIMIZATION

def sum_primes_sqrt(n):
    total = 0

    for x in range(2, n):
        if x < 4:
            total += x
            continue

        if x % 2 == 0:
            continue

        is_prime = True
        d = 3

        while d * d <= x:
            if x % d == 0:
                is_prime = False
                break
            d += 2

        if is_prime:
            total += x

    return total


print("\nSECOND METHOD: SQRT")

for n, expected in test_cases:
    got = sum_primes_sqrt(n)
    print(n, got, "PASS" if got == expected else "FAIL")

n = 2000000
start = time.time()
result = sum_primes_sqrt(n)
end = time.time()
print(f"N = {n}, sum = {result}, time = {end - start:.4f} s")


# METHOD 3: SIEVE OF ERATOSTHENES

def sum_primes_sieve(n):
    if n <= 2:
        return 0

    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False

    p = 2

    while p * p < n:
        if is_prime[p]:
            for multiple in range(p * p, n, p):
                is_prime[multiple] = False
        p += 1

    return sum(x for x in range(n) if is_prime[x])


print("\nTHIRD METHOD: SIEVE")

for n, expected in test_cases:
    got = sum_primes_sieve(n)
    print(n, got, "PASS" if got == expected else "FAIL")

n = 2000000
start = time.time()
result = sum_primes_sieve(n)
end = time.time()
print(f"N = {n}, sum = {result}, time = {end - start:.4f} s")