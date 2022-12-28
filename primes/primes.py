import numpy as np
import numpy.typing as npt
import matplotlib.pyplot as plt
import math

NDArrayInt = npt.NDArray[np.int_]
NDArrayFloat = npt.NDArray[np.float_]

""" Checks if a natural number n is prime using brute force check. """
def brute_force_is_prime(n: np.int_) -> bool:
    if n == 1: return False
    if n == 2: return True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

""" Use de sieve of Eratosthenes to find all prime numbers less then n. """
def sieve_of_erathostenes(n: np.int_) -> NDArrayInt:
    primes: NDArrayInt = []
    marked: NDArrayInt = np.zeros(n + 1, dtype=np.int_)
    for i in range(2, n + 1):
        if not marked[i]:
            marked[i] = 1
            primes.append(i)
            for j in range(i*i, n + 1, i):
                marked[j] = 1
    return np.array(primes)

def miller_rabin(n: np.int_) -> bool:
    pass