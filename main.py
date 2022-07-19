# Importamos los modulos que utilizaremos 
from webbrowser import get
import numpy as np
import pandas as pd

# Función para obtener el estado resultante de una transición
# param state: estado inicial
# param symbol: símbolo de transición
# param transition_matrix: matriz de transiciones
def transition(state, symbol, transition_matrix):
    value = transition_matrix[(transition_matrix['state'] == state) & (transition_matrix['symbol'] == symbol)]['δ(q,s)']
    return value.values[0]

# Función recursiva para obtener el estado final despues de darle al automata una cadena de símbolos
# param state: estado inicial
# param word: cadena de símbolos
# param transition_matrix: matriz de transiciones
def getFinalState(state,word,transition_matrix):
    n = len(word)
    if n == 0:
        return state
    else:
        symbol = int(word[0])
        qq = transition(state,symbol,transition_matrix)
        value = getFinalState(qq,word[1:],transition_matrix)
        return value

# estado, signo, δ(q,s)
# Automata para encontrar cantidad par de 0's y 1's 
# estado, 0 , 1
table = np.array([
    [0, 0, 1],
    [0, 1, 2], 
    [1, 0, 0], 
    [1, 1, 3], 
    [2, 0, 3],
    [2, 1, 0],
    [3, 0, 2],
    [3, 1, 1]])

tab = pd.DataFrame(table, columns=['state', 'symbol', 'δ(q,s)'])
cadena = "01010101"
print(getFinalState(0,cadena,tab))