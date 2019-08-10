class Archivo:

    _archivo = []

    def cargar_archivo(self,ruta_completa,modo):

        self._archivo = open(ruta_completa,modo)
    
    def obtener_lista_tabla_transicion(self):

        return self._archivo.read().splitlines()
    
