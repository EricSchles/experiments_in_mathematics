Last time we looked at triplets who's lengths created right angle triangles.

As you may be aware, triangles and geometry are the basis for the first "application" of numbers.  This time, we'll take this further - how many of the triplets we looked at last time are unique?

To answer this question we must first define what uniqueness means in this context -

A triplet is considered unique if it's the same triplet as another triplet, but scaled up.  

So for instance a 3,4,5 triangle is one with sides, 3, 4 and 5.  But any triangle whose ratio is 3,4,5 and relative to a scale factor is also a "3,4,5" triangle.  So while we did find a lot of triplets that "work" for creating right angle triangles, how many of them are unique?  Not just scaled versions of the 3,4,5 triangle.

In order to do this, we'll need the prime factorization of every triplet we looked at.  If the prime factorization is the same, except for one term for all three in the triplet, then we know that the triplet is just a "scaled" version of another smaller triplet we've already found.

Let's write the code!

```
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
```

What this code does is check to see if the triplets that are generated have any common prime factors across all three numbers in the triplet.  If they do, then the triplet cannot be unique - it is a scaled up version of another triplet.  And therefore gets removed from the list.

Why not check a triplet before it's added to the list?  Well that's because it actually increases the run time of our algorithm from O(N^2) to O(N^3), which is much slower.  The checking algorithm runs in O(N) so it's better to upper bound our algorithm by O(N^2) than O(N^3).  
So - how did we get all the primes?  It turns out their is a procedure that is very old called the [sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes) which helps us out here.  

