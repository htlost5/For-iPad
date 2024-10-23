def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(limit):
    primes = []
    for num in range(2, limit):
        if is_prime(num):
            primes.append(num)
    return primes

# 非常に大きな制限を設定して、計算を重くする
large_limit = 10**10
primes = find_primes(large_limit)
print(f"Found {len(primes)} primes up to {large_limit}.")