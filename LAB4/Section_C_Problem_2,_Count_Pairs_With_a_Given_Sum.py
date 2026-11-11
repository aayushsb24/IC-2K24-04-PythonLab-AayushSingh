
import random
import time


# METHOD 1: NAIVE APPROACH

def count_pairs_naive(nums, target):
    count = 0
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                count += 1

    return count


# METHOD 2: OPTIMIZED APPROACH USING HASH MAP

def count_pairs_optimized(nums, target):
    count = 0
    seen = {}

    for x in nums:
        complement = target - x

        if complement in seen:
            count += seen[complement]

        seen[x] = seen.get(x, 0) + 1

    return count


# NAIVE VERSION

print("Naive version")

for N in [5000, 50000]:
    random.seed(42)
    arr = [random.randint(1, 20000) for _ in range(N)]
    target = 20000

    start = time.time()
    result = count_pairs_naive(arr, target)
    end = time.time()

    print(f"N = {N}, pairs found = {result}, time = {end - start:.4f} s")


# OPTIMIZED VERSION

print()
print("Optimized version")

random.seed(42)
N = 50000
arr = [random.randint(1, 20000) for _ in range(N)]
target = 20000

start = time.time()
result = count_pairs_optimized(arr, target)
end = time.time()

print(f"N = {N}, pairs found = {result}, time = {end - start:.4f} s")