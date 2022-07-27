# Importamos los modulos que utilizaremos 
import numpy as np
import pandas as pd

#lista de estados
derivationList = []


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
        derivationList.append(f"δ({state},{symbol}) -> {qq}")
        value = getFinalState(qq,word[1:],transition_matrix)
        return value

# funcion para obtener los movimientos realizados por el automata
def derivation():
    for item in derivationList:
        print(item)
        
# Función para obtener si el automata termino en estado de aceptación
# param state: estado final
# param acceptance_states: estados de aceptación
def accepted(state,acceptance_states):
    return state in acceptance_states


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
cadena = "01001101"
acceptance_states = [0]
estadoFinal = getFinalState(0,cadena,tab)
print(f"termino en estado de aceptacion: {accepted(estadoFinal,acceptance_states)}")
print("\nδ(estado,simbolo) -> nuevo estado\n")
derivation()