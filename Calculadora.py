#Importamos math
import math
# Para limpiar consola
import os
# Calculadora cientifica

#Funciones Basicas
Opciones = ["\n1-Operaciones Basicas", "\n2-Operaciones con identidades trigonometricas", "\n3-Operaciones algebraicas"]

#Operacion Suma
def suma(a,b):
    os.system('cls')
    ecc= int(input("Escribe la suma: "))
    return a + b
#Operacion Resta
def resta(a,b):
    return a - b
#Operacion Multiplicacion
def mult(a,b):
    return a * b
#Operacion Division
def div(a,b):
    return a / b

#Bienvenida
print('\n"Calculadora Cientifica"')
#mostrar las opciones por medio de un for, esto se hace para ahorrar memoria y lineas de codico
for Opciones in Opciones:
    print(Opciones)
Operacion = input("\nOpcion: ")