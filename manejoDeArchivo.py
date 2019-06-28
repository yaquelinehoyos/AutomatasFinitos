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
        return tablaDeTransiciones


    def comprobarFormatoDelArchivo( self, lista ):
        if ( len( lista[0] ) != ( len( lista[1] ) - 2 ) ):
            print( "Verifique el archivo, el número de entradas no conincide con las transiciones" )
            exit()

        for val in range ( 2, len( lista ) ):
            anterior = val - 1
            if ( len( lista[val] ) != len( lista[anterior] ) ):
                print( "Verifique el archivo, existe un estado con más o menos transiciones que los demás" )
                exit()
        
        for val in range( 1, len( lista ) ):
            if ( (lista[val][-1] != '0') and (lista[val][-1] != '1') ):
                print( "Verifique el archivo, algún estado de aceptación es incorrecto" )
                exit()
        
