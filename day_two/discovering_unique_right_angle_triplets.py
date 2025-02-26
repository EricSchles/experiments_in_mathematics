import math
import json

def get_primes(N: int) -> list:        
    sieve = {}
    integer = 2

    while integer <= N:
        if integer not in sieve:
            yield integer
            sieve[integer * integer] = [integer]
        else:
            for prime in sieve[integer]:
                sieve.setdefault(prime + integer, []).append(prime)
            del sieve[integer]
        integer += 1

def get_prime_factors(n):
    prime_factors = []
    primes_upto_n = get_primes(n)
    for prime in primes_upto_n:
        if n % prime == 0:
            prime_factors.append(prime)
    return prime_factors

def get_unique_triplets(triplets):
    unique_triplets = []
    for triplet in triplets:
        prime_factors = []
        for elem in triplet:
            prime_factors.append(list(get_prime_factors(elem)))

        scaled = False
        for prime in prime_factors[0]:
            if (prime in prime_factors[1]) and (prime in prime_factors[2]):
                scaled = True
                break
        if not scaled:
            unique_triplets.append(triplet)
    return unique_triplets
            
    
if __name__ == '__main__':
    triplets = []
    for i in range(1, 1001):
        for j in range(1, 1001):
            result = i**2 + j**2
            result_square_root = math.sqrt(result)
            if int(result_square_root) == result_square_root:
                triplets.append(
                    (i,j,result_square_root)
                )

    triplets = list(set(triplets))
    triplets = get_unique_triplets(triplets)
    json.dump(triplets, open("triplets.json", "w"))
