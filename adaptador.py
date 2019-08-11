from automata_finito import AutomataFinito

class ArchivoAdaptador:

    def pasar_a_automata_finito( self, Archivo ):

        tabla_transiciones = Archivo.obtener_lista_tabla_transicion()

        entradas = self.obtener_entradas_desde_archivo( tabla_transiciones )
        estados = self.obtener_estados_desde_archivo( tabla_transiciones )
        estado_inicial = self.obtener_estado_inicial_desde_archivo( tabla_transiciones )
        estados_aceptacion = self.obtener_estados_aceptacion_desde_archivo( tabla_transiciones )
        transiciones = self.obtener_transiciones_desde_archivo( tabla_transiciones )

        #TODO: Validador.
        
        automata_finito = AutomataFinito()
        automata_finito.asignar_estados( estados )
        automata_finito.asignar_estado_inicial( estado_inicial )
        automata_finito.asignar_estados_aceptacion( estados_aceptacion )
        automata_finito.asignar_entradas( entradas )
        automata_finito.asignar_transiciones( transiciones )

        return automata_finito

    def obtener_estados_desde_archivo(self, tabla_transiciones):
        
        #Estado: son el PRIMER elemento de cada linea de la tabla de transiciones a partir de la fila 2.
        estados = [] 

        for linea in range(1,len(tabla_transiciones)): 
            lista = self.__cadena_sep_por_coma_a_lista(tabla_transiciones[linea])
            estado = lista[0]
            estados.append(estado)

        return estados
    
    def obtener_estados_aceptacion_desde_archivo(self, tabla_transiciones):
        
        #Estado aceptacion: son el ULTIMO elemento de cada linea de la tabla de transiciones a partir de la fila 2.
        estados_aceptacion = [] 

        for linea in range(1,len(tabla_transiciones)): 
            lista = self.__cadena_sep_por_coma_a_lista(tabla_transiciones[linea])
            posicion_es_estado_aceptacion = len(lista) - 1
            es_estado_aceptacion = lista[posicion_es_estado_aceptacion]
            if es_estado_aceptacion == "1":
                posicion_estado = 0
                estado = lista[posicion_estado]
                estados_aceptacion.append( estado )

        return estados_aceptacion 
        
    def obtener_estado_inicial_desde_archivo(self, tabla_transiciones):

        segunda_linea = self.__cadena_sep_por_coma_a_lista(tabla_transiciones[1])
        estado_inicial = segunda_linea[0]

        return estado_inicial
    
    def obtener_entradas_desde_archivo(self, tabla_transiciones):
        
        entradas = self.__cadena_sep_por_coma_a_lista(tabla_transiciones[0])
        return entradas

    def obtener_transiciones_desde_archivo(self, tabla_transiciones):
        
        transiciones = {}
        entradas = self.obtener_entradas_desde_archivo( tabla_transiciones )

        for linea in range(1,len(tabla_transiciones)): 
            lista = self.__cadena_sep_por_coma_a_lista(tabla_transiciones[linea])
            estado = lista[0]
            transiciones_estado = []

            for columna in range(1,len(lista) - 1):
                estado_destino = lista[columna]
                entrada = entradas[columna - 1]
                transiciones_estado.append((entrada,estado_destino))

            transiciones[estado] = transiciones_estado            

        return transiciones
    
    def __cadena_sep_por_coma_a_lista(self, cadena):

        return cadena.split(",")

