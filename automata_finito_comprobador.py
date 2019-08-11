
class AutomataFinitoComprobador:

    def comprobar(self, automata_finito, secuencia):
        
        estado_actual = automata_finito.obtener_estado_inicial()
        transiciones = automata_finito.obtener_transiciones()

        for posicion in range(len(secuencia)):
            entrada = secuencia[posicion]
            transiciones_estado_actual = transiciones[estado_actual]
            siguiente_estado = self.__siguiente_estado(transiciones_estado_actual,entrada)
            estado_actual = siguiente_estado
        
        estados_aceptacion = automata_finito.obtener_estados_aceptacion()
        es_estado_de_aceptacion = self.__es_estado_de_aceptacion( estados_aceptacion, estado_actual )
        
        return es_estado_de_aceptacion

    def __siguiente_estado(self, transiciones_estado_actual, entrada):
        
        for posicion in range(len(transiciones_estado_actual)):
            transicion = transiciones_estado_actual[posicion]
            entrada_transicion = transicion[0]
            estado_transicion = transicion[1]
            if entrada_transicion == entrada:
                siguiente_estado = estado_transicion

        return siguiente_estado

    def __es_estado_de_aceptacion( self, estados_aceptacion, estado_actual ):

        if estado_actual in estados_aceptacion:
            es_estado_de_aceptacion = True
        else:
            es_estado_de_aceptacion = False
        
        return es_estado_de_aceptacion
