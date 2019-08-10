class ManejoDeArchivo:

    nombreArchivo = ''
    rompeCiclos = False     # Esta variable nos sirve como bandera para eliminar sólo la fila incorrecta

    # Constructor
    def __init__( self ):
        pass


    # El siguiente método se llama desde la clase principal para verificar que el archivo tenga el formato correcto
    def obtenerTablaDeTransicionesDesdeArchivo( self, nombreDelArchivo, lineaNueva ):
        self.nombreArchivo = nombreDelArchivo
        self.rompeCiclos = False
        tablaDeTransiciones = []
        file1 = open( self.nombreArchivo, "r" )
        lista = file1.readlines()   # El método readlines() nos devuelve una lista
        file1.close()
        for val in range( len( lista ) ):
            tablaDeTransiciones.append( lista[val].rstrip( '\n' ).split( ',' ) )    # Quitamos los saltos de línea y las comas
        self.comprobarFormatoDelArchivo( tablaDeTransiciones, lineaNueva )
        listaDeEstados = self.buscarListaDeEstados( tablaDeTransiciones )
        self.comprobarTransicionesAEstadosCorrectos( tablaDeTransiciones, listaDeEstados, lineaNueva )
        return tablaDeTransiciones


    # En el siguiente método verificamos que el número de entradas sean correctas
    def comprobarFormatoDelArchivo( self, lista, lineaNueva ):
        if ( len( lista[0] ) != ( len( lista[1] ) - 2 ) ):     
            print( "El número de entradas no conincide con las transiciones" )
            print( "verifique el archivo en la fila: 1 y por favor corregir" )
            exit()
        self.comprobarNumeroDeTransiciones( lista, lineaNueva )
        self.comprobarEstadosDeAceptacion( lista, lineaNueva )


    # En el siguiente método comprobamos que se tenga el mismo número de columnas
    # sin contar la primera fila que son las entradas
    def comprobarNumeroDeTransiciones(self, lista, lineaNueva):
        for val in range ( 2, len( lista ) ):
            anterior = val - 1
            if ( len( lista[val] ) != len( lista[anterior] ) ):
                if( lineaNueva ):
                    if( self.rompeCiclos ):
                        break
                    else:
                        print( "\nLa linea ingresada no es válida" )
                        self.eliminarLineaNueva()
                        break
                else:
                    print( "Existe un estado con más o menos transiciones que los demás" )
                    print( "Verifique el archivo en la fila: ", (val+1), " y por favor corregir" )
                    exit()
            

    # El siguiente método comprueba que la última columna (Columna de estados de aceptación) contenga sólo 0 ó 1
    def comprobarEstadosDeAceptacion( self, lista, lineaNueva ):
        for val in range( 1, len( lista ) ):
            if ( (lista[val][-1] != '0') and (lista[val][-1] != '1') ):
                if( lineaNueva ):
                    if( self.rompeCiclos ):
                        break
                    else:
                        print( "\nLa linea ingresada no es válida" )
                        self.eliminarLineaNueva()
                        break
                else:
                    print( "Algún estado de aceptación es incorrecto" )
                    print( "Verifique el archivo en la fila: ", (val+1), " y por favor corregir" )
                    exit()


    # En este método guardamos los estados en una lista
    def buscarListaDeEstados( self, lista ):
        listaEstados = []
        for val in range( 1, len( lista ) ):
            listaEstados.append( lista[val][0] )
        return listaEstados


    # En este método verificamos que las transiciones se hagan a estados correctos.
    # Miramos la matriz sin la primera fila (fila de entradas), sin la última columna (estados de acpetación)
    # Y sin la primera columna que son los estados; verificamos entonces que esa matriz contenga valores 
    # existentes en la lista que guarda los estados
    def comprobarTransicionesAEstadosCorrectos( self, lista, listaEstados, lineaNueva ):
        for x in range( 1, len(lista) ):
            for y in range( 1, (len(lista[x]) - 1) ):
                if( listaEstados.count( lista[x][y] ) == 0 ):
                    if( lineaNueva ):
                        if( self.rompeCiclos ):
                            break
                        else:
                            print( "\nLa linea ingresada no es válida" )
                            self.eliminarLineaNueva()
                            break
                    else:
                        print( "Alguna de las transiciones está incorrecta" )
                        print( "Verifique el archivo en la fila: ", (x+1), " y por favor corregir" )
                        exit()

    
    # Este método es llamado sólo en caso de que se agregue una nueva fila y la fila esté errónea
    def eliminarLineaNueva( self ):
        self.rompeCiclos = True
        file1 = open( self.nombreArchivo, "r" )
        lineasArchivo = file1.readlines()
        lineasArchivo = lineasArchivo[:-1]      # Se elimina la última fila ingresada
        lineasArchivo[-1] = lineasArchivo[-1].strip()       # Borramos el salto de línea
        file1.close()
        file2 = open( self.nombreArchivo, "w" )
        file2.writelines( lineasArchivo )   # Reescribimos el archivo de nuevo, esta vez sin la línea errónea 
        file2.close()
        