# https://stackoverflow.com/questions/15285534/isprime-function-for-python-language
def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n % 2 == 0: return False
    if n < 9: return True
    if n % 3 == 0: return False
    r = int(n ** 0.5)
    # since all primes > 3 are of the form 6 * n ± 1
    # start with f = 5 (which is prime)
    # and test f, f + 2 for being prime
    # then loop by 6.
    f = 5
    while f <= r:
        if n % f == 0: return False
        if n % (f + 2) == 0: return False
        f += 6
    return True

def prime_list(n):
    primes = []
    for i in range(1, n + 1):
        if is_prime(i):
            primes += [i]
    return primes

print(sum(prime_list(10000)))