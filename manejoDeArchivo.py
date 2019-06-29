class ManejoDeArchivo:

    nombreArchivo = ''

    def __init__( self ):
        pass


    def obtenerTablaDeTransicionesDesdeArchivo( self, nombreDelArchivo, lineaNueva ):
        self.nombreArchivo = nombreDelArchivo
        tablaDeTransiciones = []
        file1 = open( self.nombreArchivo, "r" )
        lista = file1.readlines()
        for val in range( len( lista ) ):
            tablaDeTransiciones.append( lista[val].rstrip( '\n' ).split( ',' ) )
        file1.close()
        self.comprobarFormatoDelArchivo( tablaDeTransiciones, lineaNueva )
        listaDeEstados = self.buscarListaDeEstados( tablaDeTransiciones )
        self.comprobarTransicionesAEstadosCorrectos( tablaDeTransiciones, listaDeEstados, lineaNueva )
        return tablaDeTransiciones


    def comprobarFormatoDelArchivo( self, lista, lineaNueva ):
        if ( len( lista[0] ) != ( len( lista[1] ) - 2 ) ):
            print( "El número de entradas no conincide con las transiciones" )
            print( "verifique el archivo en la fila: 1 y por favor corregir" )
            exit()
        for val in range ( 2, len( lista ) ):
            anterior = val - 1
            if ( len( lista[val] ) != len( lista[anterior] ) ):
                if( lineaNueva ):
                    print( "El estado ingresado tiene más o menos transiciones que los demás" )
                    self.eliminarLineaNueva()
                else:
                    print( "Existe un estado con más o menos transiciones que los demás" )
                    print( "Verifique el archivo en la fila: ", (val+1), " y por favor corregir" )
                    exit()
        for val in range( 1, len( lista ) ):
            if ( (lista[val][-1] != '0') and (lista[val][-1] != '1') ):
                if( lineaNueva ):
                    print( "El estado de aceptación es incorrecto" )
                    self.eliminarLineaNueva()
                else:
                    print( "Algún estado de aceptación es incorrecto" )
                    print( "Verifique el archivo en la fila: ", (val+1), " y por favor corregir" )
                    exit()
        

    def buscarListaDeEstados( self, lista ):
        listaEstados = []
        for val in range( 1, len( lista ) ):
            listaEstados.append( lista[val][0] )
        return listaEstados


    def comprobarTransicionesAEstadosCorrectos( self, lista, listaEstados, lineaNueva ):
        for x in range( 1, len(lista) ):
            for y in range( 1, (len(lista[x]) - 1) ):
                if( listaEstados.count( lista[x][y] ) == 0 ):
                    if( lineaNueva ):
                        print( "Alguna de las transiciones de la linea nueva está incorrecta" )
                        self.eliminarLineaNueva()
                    else:
                        print( "Alguna de las transiciones está incorrecta" )
                        print( "Verifique el archivo en la fila: ", (x+1), " y por favor corregir" )
                        exit()

    
    def eliminarLineaNueva( self ):
        print( "\nLa linea ingresada no es válida" )
        #file1 = open( self.nombreArchivo, "r" )
        #lineasArchivo = file1.readlines()
        #lineasArchivo = lineasArchivo[:-1]
        #file1.close()
        #file2 = open( self.nombreArchivo, "w" )
        #file2.writelines( lineasArchivo )
        #file2.close()
        