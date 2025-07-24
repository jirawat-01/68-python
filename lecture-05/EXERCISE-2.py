def genrate_primes(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) +1):
            if num % i ==0:
                return False
        return True
    primes = [str(i) for i in range(2, n) if is_prime(i)]
    return ",".join(primes)

print(genrate_primes(10))
print(genrate_primes(20))
print(genrate_primes(1))
print(genrate_primes(2))