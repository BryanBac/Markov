import numpy as np
from markov_functions import markov

matriz = np.array([[0.52, 0.3, 0.18], [0.23, 0.35, 0.42], [0.07, 0.24, 0.69]])
vector = np.array([0, 1, 0])
iteraciones = 3
print("Aquí están las probabilidades resultantes \n")
print(markov(vector, matriz, iteraciones))
