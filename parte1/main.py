from utilidades import cargar_datos
from transporte import ProblemaTransporte

def main():
    programadores, tareas, C = cargar_datos()
    problema = ProblemaTransporte(programadores, tareas, C)
    costo_total = problema.resolver_metodo_costo_minimo()
    problema.mostrar_resultado(costo_total)

if __name__ == "__main__":
    main()
