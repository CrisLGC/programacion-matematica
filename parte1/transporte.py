import numpy as np

class ProblemaTransporte:
    def __init__(self, programadores, tareas, costos):
        self.programadores = programadores
        self.tareas = tareas
        self.costos = costos  # matriz de costos [N x M]
        self.N = len(programadores)
        self.M = len(tareas)
        self.asignaciones = []
        self.reporte = []

    def resolver_metodo_costo_minimo(self):
        capacidad = [p.capacidad for p in self.programadores]
        demanda = [t.demanda for t in self.tareas]
        C = self.costos.copy()
        total = 0

        while True:
            min_val = float('inf')
            min_i = min_j = -1

            for i in range(self.N):
                for j in range(self.M):
                    if capacidad[i] > 0 and demanda[j] > 0 and C[i][j] < min_val:
                        min_val = C[i][j]
                        min_i, min_j = i, j

            if min_i == -1:
                break

            asignar = min(capacidad[min_i], demanda[min_j])
            capacidad[min_i] -= asignar
            demanda[min_j] -= asignar
            total += asignar * C[min_i][min_j]

            self.asignaciones.append((min_i, min_j, asignar))
            self.reporte.append(
                f"Programador {min_i} → Tarea {min_j} | Cantidad: {asignar} | Costo: {C[min_i][min_j]} | Subtotal: {asignar * C[min_i][min_j]}"
            )

        return total

    def mostrar_resultado(self, costo_total):
        print("\nAsignaciones óptimas:")
        for linea in self.reporte:
            print(linea)
        print(f"\nCosto total mínimo: {costo_total}")
