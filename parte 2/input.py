from server import Server
from request import Request

def obtener_entradas():
    servidores = []
    solicitudes = []
    print("Ingrese el número de servidores:")
    n_serv = int(input())
    for i in range(n_serv):
        print(f"\nServidor {i+1}:")
        id = input("ID: ")
        cpu = int(input("Capacidad CPU: "))
        mem = int(input("Capacidad Memoria: "))
        servidores.append(Server(id, cpu, mem))

    print("\nIngrese el número de solicitudes:")
    n_sol = int(input())
    for j in range(n_sol):
        print(f"\nSolicitud {j+1}:")
        id = input("ID: ")
        cpu_req = int(input("Requiere CPU: "))
        mem_req = int(input("Requiere Memoria: "))
        prioridad = int(input("Prioridad (mayor = más urgente): "))
        solicitudes.append(Request(id, cpu_req, mem_req, prioridad))

    print("\nIngrese la matriz de costos (tiempo estimado por asignación):")
    costos = []
    for i in range(n_serv):
        print(f"Costos para el servidor {servidores[i].id} (separados por espacio):")
        fila = list(map(float, input().split()))
        costos.append(fila)

    return servidores, solicitudes, costos