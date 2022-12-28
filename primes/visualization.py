import numpy as np
import numpy.typing as npt
import matplotlib.pyplot as plt

import math
from primes import sieve_of_erathostenes

NDArrayInt = npt.NDArray[np.int_]
NDArrayFloat = npt.NDArray[np.float_]

def gauss_prime_counting_function(n: np.int_ = 10000) -> None:
    primes_less_than_or_equal_to_n: NDArrayInt = sieve_of_erathostenes(n)
    counter_of_primes: NDArrayInt = np.zeros(n + 1, dtype=np.int_)
    counter_of_primes[primes_less_than_or_equal_to_n] = 1
    for i in range(len(counter_of_primes) - 1, -1, -1):
        counter_of_primes[i] = np.sum(counter_of_primes[0:i+1])
    x_coordinates: NDArrayInt = np.arange(n + 1)
    y_coordinates: NDArrayInt = counter_of_primes
    plt.grid()
    plt.xlabel("X")
    plt.ylabel("Prime numbers less than X")
    plt.plot(x_coordinates, y_coordinates, 'y', label = "Counting function")
    plt.plot(x_coordinates, list(map(lambda i: i/math.log(i) if i != 0 else 0, np.arange(n + 1))), 'r', label="x/ln(x)")
    plt.plot(x_coordinates, list(map(lambda i: i/(math.log(i) - 1.08366) if i != 0 else 0, np.arange(n + 1))),'b', label="x/(ln(x) - 1.08366)")
    plt.legend()
    plt.show()

gauss_prime_counting_function()