import automataFinito as af
import manejoDeArchivo as ma

archivo = ma.ManejoDeArchivo()
tablaDeTransiciones = archivo.obtenerTablaDeTransicionesDesdeArchivo( "archivo.txt" )
automataFinito = af.AutomataFinito( tablaDeTransiciones )

print( "\nTabla de transiciones: \n", automataFinito.obtenerTablaDeTransiciones() )
print( "\nNumero de estados: ", automataFinito.obtenerNumeroDeEstados() )
print( "\nEntradas: ", automataFinito.obtenerEntradas() )