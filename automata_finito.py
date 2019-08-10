class AutomataFinito:

    _estados = []
    _estados_aceptacion = []
    _entradas = []
    _transiciones = {}

    def __init__(self):
        pass
    
    def asignar_estados(self, estados):

        self._estados = estados
    
    def asignar_entradas(self, entradas):

        self._entradas = entradas
    
    def asignar_transiciones(self, transiciones):

        self._transiciones = transiciones
    
    def asignar_estados_aceptacion(self,estados_aceptacion):

        self._estados_aceptacion = estados_aceptacion
    
  
