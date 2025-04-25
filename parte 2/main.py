from input import obtener_entradas
from optimizer import AssignmentOptimizer

# Obtener entradas desde consola
servidores, solicitudes, costos = obtener_entradas()

# Resolver el problema
optimizador = AssignmentOptimizer(servidores, solicitudes, costos)
optimizador.construir_modelo()
asignaciones = optimizador.resolver()
costo_total = optimizador.obtener_costo_total()

# Mostrar resultados
print("\nAsignaciones óptimas:")
for servidor, solicitud in asignaciones:
    print(f" - {solicitud} asignada a {servidor}")

print(f"\nCosto total ponderado: {costo_total:.2f}")
