class ManejoDeArchivo:

    def __init__(self):
        pass

    def obtenerTablaDeTransiciones(self, nombreDelArchivo):
        tablaDeTransiciones = []
        file1 = open(nombreDelArchivo, "r")
        lista = file1.readlines()
        for val in range(len(lista)):
            tablaDeTransiciones.append(lista[val].rstrip('\n').split(','))
        file1.close()
        return tablaDeTransiciones
