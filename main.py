import numpy as np
from markov_functions import markov

matriz = np.array([[0.8, 0.1, 0.1], [0.03, 0.95, 0.02], [0.2, 0.05, 0.75]])
vector = np.array([0.45, 0.25, 0.3])
print("Aquí están las probabilidades resultantes \n")
print(markov(vector, matriz, 2))
