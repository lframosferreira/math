import numpy as np
import numpy.typing as npt
import matplotlib.pyplot as plt

NDArrayInt = npt.NDArray[np.int_]
NDArrayFloat = npt.NDArray[np.float_]

def generate_pythagorean_tryplets(span: int = 10) -> NDArrayInt:
    list_of_pythagorean_triples: NDArrayInt = []
    for i in range(-span, span + 1):
        for j in range(-span, span + 1):
            if i != j:
                pythagorean_triple = (i**2 - j**2, 2*i*j, i**2 + j**2)
                list_of_pythagorean_triples.append(pythagorean_triple)
    return np.array(list_of_pythagorean_triples)

def plot_pythagorean_triples() -> None:
    list_of_pythagorean_triples: NDArrayInt = generate_pythagorean_tryplets()
    x_coordinates: NDArrayInt = np.array([x for x, y, z in list_of_pythagorean_triples])
    y_coordinates: NDArrayInt = np.array([y for x, y, x in list_of_pythagorean_triples])
    plt.plot(x_coordinates, y_coordinates, 'y.', label="teste")
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.grid()
    plt.show()
