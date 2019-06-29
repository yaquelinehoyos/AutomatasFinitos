import automataFinito as af
import manejoDeArchivo as ma

archivo = ma.ManejoDeArchivo()
nombreDelArchivo = "archivo.txt"

booleanoAuxiliar = True
bandera = False
while( booleanoAuxiliar ):
    tablaDeTransiciones = archivo.obtenerTablaDeTransicionesDesdeArchivo( nombreDelArchivo, bandera ) 
    automataFinito = af.AutomataFinito( tablaDeTransiciones )

    print( "\nTabla de transiciones: \n", automataFinito.obtenerTablaDeTransiciones() )
    print( "\nNumero de estados: ", automataFinito.obtenerNumeroDeEstados() )
    print( "\nEntradas: ", automataFinito.obtenerEntradas() )

    pregunta = input( "\n¿Desea ingresar una nueva fila? y/n: \n" )
    if( pregunta == 'y' ):
        bandera = True
        file1 = open( nombreDelArchivo, "a" )
        nuevaFila = input( "\nIngrese la nueva fila\n" )
        file1.write( "\n" + nuevaFila )
        file1.close()
    elif( pregunta == 'n' ):
        booleanoAuxiliar = False
