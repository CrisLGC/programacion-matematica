import numpy as np
from modelos import Programador, Tarea

def cargar_datos():
    N = int(input("Número de programadores: "))
    M = int(input("Número de tareas: "))

    print("\nMatriz de costos combinados (eficiencia + transporte):")
    C = np.array([list(map(int, input(f"Fila {i+1}: ").split())) for i in range(N)])

    print("\nCapacidad máxima de tareas por programador:")
    S = list(map(int, input().split()))

    print("\nCantidad de programadores requeridos por tarea:")
    D = list(map(int, input().split()))

    programadores = [Programador(i, S[i]) for i in range(N)]
    tareas = [Tarea(j, D[j]) for j in range(M)]

    return programadores, tareas, C
