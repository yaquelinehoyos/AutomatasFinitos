import automataFinito as af
import manejoDeArchivo as ma

archivo = ma.ManejoDeArchivo()
nombreDelArchivo = "archivo.txt"

booleanoAuxiliar = True     # Esta variable nos será útil si el usuario desea ingresar varias filas
bandera = False             # Esta variable nos indica si se ingresó una nueva fila al archivo
tablaDeTransiciones = archivo.obtenerTablaDeTransicionesDesdeArchivo( nombreDelArchivo, bandera )
print( "Esta es la tabla ingresada: ", tablaDeTransiciones )

while( booleanoAuxiliar ):
    pregunta = input( "\n¿Desea ingresar una nueva fila? y/n: \n" )
    if( pregunta == 'y' ):
        bandera = True
        file1 = open( nombreDelArchivo, "a" )
        nuevaFila = input( "\nIngrese la nueva fila\n" )
        file1.write( "\n" + nuevaFila )         # Añadimos la nueva fila al archvio
        file1.close()
    elif( pregunta == 'n' ):
        bandera = False
        booleanoAuxiliar = False
    # En la siguiente línea se verifica de nuevo el archivo en caso de que se haya agregado una nueva fila al archivo
    tablaDeTransiciones = archivo.obtenerTablaDeTransicionesDesdeArchivo( nombreDelArchivo, bandera )

    
automataFinito = af.AutomataFinito( tablaDeTransiciones )
print( "\nTabla de transiciones: \n", automataFinito.obtenerTablaDeTransiciones() )
print( "\nNumero de estados: ", automataFinito.obtenerNumeroDeEstados() )
print( "\nEntradas: ", automataFinito.obtenerEntradas() )