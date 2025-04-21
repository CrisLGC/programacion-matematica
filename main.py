import numpy as np
from collections import defaultdict

def cargar_datos():
    modo = input("¿Deseas ingresar los datos por consola o desde un archivo? (c/a): ").strip().lower()
    if modo == 'a':
        ruta = input("Ingresa la ruta del archivo: ")
        with open(ruta, 'r') as f:
            N, M = map(int, f.readline().split())
            C = [list(map(int, line.strip().split())) for line in f]
    else:
        N = int(input("Número de programadores: "))
        M = int(input("Número de tareas: "))
        print(f"Ingrese la matriz de costos/eficiencia ({N} filas, {M} columnas):")
        C = [list(map(int, input(f"Fila {i+1}: ").split())) for i in range(N)]

    return np.array(C), N, M

def asignar_tareas_normal(C, N, M, maximizar=False):
    asignaciones = []
    total = 0

    for j in range(M):
        valores_tarea = C[:, j]
        idx = np.argmax(valores_tarea) if maximizar else np.argmin(valores_tarea)
        asignaciones.append((idx, j))
        total += C[idx][j]

    return asignaciones, total

def asignar_tareas_con_limite(C, N, M, max_tareas, maximizar=False):
    tareas_por_programador = defaultdict(int)
    asignaciones = []
    total = 0
    tareas_asignadas = [False] * M

    for _ in range(M):
        mejor_prog = None
        mejor_tarea = None
        mejor_valor = -float('inf') if maximizar else float('inf')

        for tarea in range(M):
            if tareas_asignadas[tarea]:
                continue

            for prog in range(N):
                if tareas_por_programador[prog] < max_tareas:
                    valor = C[prog][tarea]
                    if (maximizar and valor > mejor_valor) or (not maximizar and valor < mejor_valor):
                        mejor_valor = valor
                        mejor_prog = prog
                        mejor_tarea = tarea

        if mejor_prog is not None and mejor_tarea is not None:
            asignaciones.append((mejor_prog, mejor_tarea))
            tareas_asignadas[mejor_tarea] = True
            tareas_por_programador[mejor_prog] += 1
            total += C[mejor_prog][mejor_tarea]

    return asignaciones, total

def main():
    C, N, M = cargar_datos()

    modo = input("¿Deseas minimizar costo o maximizar eficiencia? (min/max): ").strip().lower()
    maximizar = modo == 'max'

    usar_restriccion = input("¿Deseas aplicar un límite máximo de tareas por programador? (s/n): ").strip().lower()
    if usar_restriccion == 's':
        max_tareas = int(input("¿Cuál es el número máximo de tareas por programador?: "))
        asignaciones, total = asignar_tareas_con_limite(C, N, M, max_tareas, maximizar)
    else:
        asignaciones, total = asignar_tareas_normal(C, N, M, maximizar)

    print("\nAsignaciones óptimas (Programador → Tarea):")
    for prog, tarea in asignaciones:
        print(f"Programador {prog} → Tarea {tarea}")

    etiqueta = "eficiencia total alcanzada" if maximizar else "costo total de asignación"
    print(f"\n{etiqueta.capitalize()}: {total}")

if __name__ == "__main__":
    main()
