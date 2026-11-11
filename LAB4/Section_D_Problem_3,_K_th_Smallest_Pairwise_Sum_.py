
import random
import time


# METHOD 1: NAIVE APPROACH

def kth_smallest_sum_naive(arr, k):
    sums = []
    n = len(arr)

    for i in range(n):
        for j in range(i + 1, n):
            sums.append(arr[i] + arr[j])

    sums.sort()
    return sums[k - 1]


# METHOD 2: OPTIMIZED APPROACH USING BINARY SEARCH

def count_pairs_leq(arr, v):
    n = len(arr)
    count = 0
    left, right = 0, n - 1

    while left < right:
        if arr[left] + arr[right] <= v:
            count += right - left
            left += 1
        else:
            right -= 1

    return count


def kth_smallest_sum_optimized(arr, k):
    arr = sorted(arr)
    n = len(arr)

    lo = arr[0] + arr[1]
    hi = arr[n - 2] + arr[n - 1]

    while lo < hi:
        mid = (lo + hi) // 2

        if count_pairs_leq(arr, mid) >= k:
            hi = mid
        else:
            lo = mid + 1

    return lo


# GENERATE RANDOM INPUT

random.seed(42)

N = 5000
arr = [random.randint(1, 100000) for _ in range(N)]
K = 1000000


# NAIVE VERSION

print("Naive version")

start = time.time()
result_naive = kth_smallest_sum_naive(arr, K)
end = time.time()

print(f"N = {N}, K = {K}, result = {result_naive}, time = {end - start:.4f} s")


# OPTIMIZED VERSION

print()
print("Optimized version")

start = time.time()
result_opt = kth_smallest_sum_optimized(arr, K)
end = time.time()

print(f"N = {N}, K = {K}, result = {result_opt}, time = {end - start:.4f} s")