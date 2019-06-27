class AutomataFinito:

    tablaDeTransiciones = []
    numeroDeEstados = 0

    def __init__(self, tablaDeTransiciones):
        self.tablaDeTransiciones = tablaDeTransiciones

    def getNumeroDeEstados(self):
        self.numeroDeEstados = len(self.tablaDeTransiciones) - 1
        return self.numeroDeEstados
 