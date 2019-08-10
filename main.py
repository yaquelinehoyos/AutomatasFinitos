import os
import platform
import sys

from archivo import Archivo
from adaptador import ArchivoAdaptador
from automata_finito import AutomataFinito

automata_finito = AutomataFinito()

def get_clear_command_by_os():

	switcher = { 'Linux': "clear", 'Windows': "cls", 'Darwin': "clear" }
	return switcher[ platform.system() ]

def display_tittle_bar():
	
	os.system(get_clear_command_by_os())

	print("\t********************************************************************************")
	print("\t***  Laboratorio teoría de Lenguajes 201901 - Practica 1: Autómatas finitos  ***")
	print("\t********************************************************************************")

def get_user_choice():

	print ("Selecciona una opción")

	print ("\t1 - Cargar archivo con tabla de transición")
	print ("\t2 - Determinar tipo autómata finito")
	print ("\t3 - Convertir a deterministico")
	print ("\t4 - Simplificar")
	print ("\t5 - Comprobar")
	print ("\tq - Salir")
	
	return input("inserta un numero valor >> ")

choice = ''
display_tittle_bar()

while choice != 'q':

	choice = get_user_choice()

	display_tittle_bar()

	if choice == "1":

		print ("")

		archivo = Archivo()
		archivo.cargar_archivo("archivo.txt","r")
		
		archivo_adaptador = ArchivoAdaptador()
		automata_finito = archivo_adaptador.pasar_a_automata_finito(archivo)
		
		input("Has pulsado la opción 1...\npulsa una tecla para continuar")

	elif choice == "2":

		print ("")
		input("Has pulsado la opción 2...\npulsa una tecla para continuar")

	elif choice == "3":

		print ("")q
		input("Has pulsado la opción 3...\npulsa una tecla para continuar")
		
	elif choice == "4":

		print ("")
		input("Has pulsado la opción 4...\npulsa una tecla para continuar")
	
	elif choice == "5":

		print ("")
		input("Has pulsado la opción 5...\npulsa una tecla para continuar")

	elif choice == "q":

		print("...Hasta luego")		

	else:

		print (""
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")


	


