class ManejoDeArchivo:

    def __init__( self ):
        pass


    def obtenerTablaDeTransicionesDesdeArchivo( self, nombreDelArchivo ):
        tablaDeTransiciones = []
        file1 = open( nombreDelArchivo, "r" )
        lista = file1.readlines()
        for val in range( len( lista ) ):
            tablaDeTransiciones.append( lista[val].rstrip( '\n' ).split( ',' ) )
        file1.close()
        self.comprobarFormatoDelArchivo( tablaDeTransiciones )
        listaDeEstados = self.comprobarListaDeEstados( tablaDeTransiciones )
        self.comprobarTransicionesAEstadosCorrectos( tablaDeTransiciones, listaDeEstados )
        return tablaDeTransiciones


    def comprobarFormatoDelArchivo( self, lista ):
        if ( len( lista[0] ) != ( len( lista[1] ) - 2 ) ):
            print( "El número de entradas no conincide con las transiciones" )
            print( "verifique el archivo en la fila: 1" )
            exit()
        for val in range ( 2, len( lista ) ):
            anterior = val - 1
            if ( len( lista[val] ) != len( lista[anterior] ) ):
                print( "Existe un estado con más o menos transiciones que los demás" )
                print( "Verifique el archivo en la fila: ", val )
                exit()
        for val in range( 1, len( lista ) ):
            if ( (lista[val][-1] != '0') and (lista[val][-1] != '1') ):
                print( "Algún estado de aceptación es incorrecto" )
                print( "Verifique el archivo en la fila: ", val )
                exit()
        

    def comprobarListaDeEstados( self, lista ):
        listaEstados = []
        for val in range( 1, len( lista ) ):
            listaEstados.append( lista[val][0] )
        return listaEstados


    def comprobarTransicionesAEstadosCorrectos( self, lista, listaEstados ):
        for x in range( 1, len(lista) ):
            for y in range( 1, (len(lista[x]) - 1) ):
                if( listaEstados.count( lista[x][y] ) == 0 ):
                    print( "Alguna de las transiciones está incorrecta" )
                    print( "Verifique el archivo en la fila: ", x )
                    exit()
                