import automataFinito as au
import manejoDeArchivo as ma

archivo = ma.ManejoDeArchivo()
archivo.leerTablaDeTransiciones("archivo.txt")
tablaDeTransiciones = archivo.getTablaDeTransiciones()
print("Se muestra taba de transiciones: \n",tablaDeTransiciones)
automataFinito = au.AutomataFinito(tablaDeTransiciones)
numeroDeEstados = automataFinito.getNumeroDeEstados()
print("\nNumero de estados: ", numeroDeEstados)