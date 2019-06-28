class AutomataFinito:

    tablaDeTransiciones = []
    entradas = []
    numeroDeEstados = 0

    def __init__( self, tablaDeTransiciones ):                    #Constructor del automata finito
        self.tablaDeTransiciones = tablaDeTransiciones          
        self.entradas = self.tablaDeTransiciones[0]               #Hallamos las entradas posibles que están en la posición 0 
        self.tablaDeTransiciones.remove( self.entradas )          #Borramos la posición 0 que no hace parte de las transiciones          
        self.numeroDeEstados = len( self.tablaDeTransiciones )    
    
    def obtenerTablaDeTransiciones( self ):
        return self.tablaDeTransiciones
        
    def obtenerEntradas( self ):
        return self.entradas

    def obtenerNumeroDeEstados( self ):
        return self.numeroDeEstados
