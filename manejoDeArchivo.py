class ManejoDeArchivo:

    tablaDeTransiciones = []

    def __init__(self):
        pass

    def leerTablaDeTransiciones(self, nombreDelArchivo):
        file1 = open(nombreDelArchivo, "r")
        lista = file1.readlines()
        for val in range(len(lista)):
            self.tablaDeTransiciones.append(lista[val].rstrip('\n').split(','))
        file1.close()
    
    def getTablaDeTransiciones(self):
        return self.tablaDeTransiciones
