from automata_finito import AutomataFinito
import re

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

        for fila in range(1,len(tabla_transiciones)): 
            elementos_fila = self.__obtener_elementos_fila( tabla_transiciones[fila] )
            estado = elementos_fila[0]
            transiciones_estado = []

            for columna in range(1,len(elementos_fila) - 1):
                entrada = entradas[columna - 1]
                estado_destino = elementos_fila[columna]
                if re.match('{.+}',estado_destino) is None:
                    transiciones_estado.append((entrada,estado_destino))
                else:
                    estados_destino = elementos_fila[columna][1:len(elementos_fila[columna]) - 1]
                    estados_destino = self.__cadena_sep_por_coma_a_lista( estados_destino )
                    for posicion in range(len(estados_destino)):
                        estado_destino = estados_destino[posicion]
                        transiciones_estado.append((entrada,estado_destino))

            transiciones[estado] = transiciones_estado            

        return transiciones
    
    def __cadena_sep_por_coma_a_lista(self, cadena):

        return cadena.split(",")

    def __obtener_elementos_fila(self, fila_tabla_transiciones):

        elementos_separdos_por_coma = self.__cadena_sep_por_coma_a_lista(fila_tabla_transiciones)
        elementos_fila = []
        es_elemento_entre_llaves = False
        elementos_entre_llaves = ""

        for posicion_fila in range(len(elementos_separdos_por_coma)):
            elemento = elementos_separdos_por_coma[posicion_fila]
            if re.match('{.+',elemento) is not None:
                es_elemento_entre_llaves = True
                if elementos_entre_llaves == "":
                    elementos_entre_llaves = elementos_entre_llaves + elemento
                else:
                    elementos_entre_llaves = elementos_entre_llaves + "," + elemento
            elif re.match('.+}',elemento) is not None:
                es_elemento_entre_llaves = False
                if elementos_entre_llaves == "":
                    elementos_entre_llaves = elementos_entre_llaves + elemento
                else:
                    elementos_entre_llaves = elementos_entre_llaves + "," + elemento
                elementos_fila.append(elementos_entre_llaves)
                elementos_entre_llaves = ""
            elif re.match(r'\w',elemento) is not None:
                if es_elemento_entre_llaves == True:
                    if elementos_entre_llaves == "":
                        elementos_entre_llaves = elementos_entre_llaves + elemento
                    else:
                        elementos_entre_llaves = elementos_entre_llaves + "," + elemento
                else:
                    elementos_fila.append(elemento)
        
        return elementos_fila
