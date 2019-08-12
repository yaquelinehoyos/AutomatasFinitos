class Archivo:

    _archivo = []
    _lista_tabla_transicion = []

    def cargar_archivo(self,ruta_completa,modo):

        self._archivo = open(ruta_completa,modo)
    
    def obtener_lista_tabla_transicion(self):

        if not self._lista_tabla_transicion:
            self._lista_tabla_transicion = self._archivo.read().splitlines()
        
        return self._lista_tabla_transicion
    
