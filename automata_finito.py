class AutomataFinito:

    _estados = []
    _estado_inicial = ""
    _estados_aceptacion = []
    _entradas = []
    _transiciones = {}
    
    def asignar_estados(self, estados):

        self._estados = estados
    
    def asignar_entradas(self, entradas):

        self._entradas = entradas
    
    def asignar_transiciones(self, transiciones):

        self._transiciones = transiciones
    
    def asignar_estados_aceptacion(self,estados_aceptacion):

        self._estados_aceptacion = estados_aceptacion
    
    def asignar_estado_inicial(self, estado_inicial):
        
        self._estado_inicial = estado_inicial
    
    def obtener_estados(self):

        return self._estados
        
    def obtener_entradas(self):
    
        return self._entradas
        
    def obtener_transiciones(self):
    
        return self._transiciones
        
    def obtener_estados_aceptacion(self):
    
        return self._estados_aceptacion
    
    def obtener_estado_inicial(self):

        return self._estado_inicial
  
