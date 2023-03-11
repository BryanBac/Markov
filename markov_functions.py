import numpy as np


def multiply(vector: np.ndarray, matriz: np.ndarray):
    r1: np.ndarray = vector.dot(matriz)
    return r1;


def pot(m1: np.ndarray, value: int):
    r1: np.ndarray = np.linalg.matrix_power(m1, value)
    return r1


def markov(vector: np.ndarray, m1: np.ndarray, value: int):
    matriz = pot(m1, value)
    result = multiply(vector, matriz)
    return result
