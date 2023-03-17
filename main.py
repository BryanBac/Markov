import numpy as np
from markov_functions import markov

matriz = np.array([[0.1, 0.3, 0.6], [0.2, 0.2, 0.6], [0.2, 0.4, 0.4]])
vector = np.array([1, 0, 0])
iteraciones = 7
print("Aquí están las probabilidades resultantes \n")
markov(vector, matriz, iteraciones)
# Debo solucionar algun error en la formula