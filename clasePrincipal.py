import automataFinito as au
import manejoDeArchivo as ma

archivo = ma.ManejoDeArchivo()
tablaDeTransiciones = archivo.obtenerTablaDeTransiciones("archivo.txt")
print("Se muestra taba de transiciones: \n",tablaDeTransiciones)
automataFinito = au.AutomataFinito(tablaDeTransiciones)
numeroDeEstados = automataFinito.getNumeroDeEstados()
print("\nNumero de estados: ", numeroDeEstados)