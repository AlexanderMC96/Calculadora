# import functions as math   (para añadir alias "math" delante de la funcion)
# from functions_math import suma, resta, multiplicacion, division, potencia
# from functions import *
import os
import functions_math as math

def menu():
    print("Bienvenido a su calculadora principal, a continuación le muestro el menu de opciones:\n")

    print("1) Sumar")
    print("2) Restar")
    print("3) Multiplicar")
    print("4) Dividir")
    print("5) Potencia")
    print("6) Raiz cuadrada")
    print("0) Salir")
    print()
def cleaning():
    while True:
        clean = str(input('Desea limpiar la pantalla (Y/N): '))
        if clean == 'Y':
            os.system('cls')
            break
        elif clean =='N':
            print("Vale...")
            break
        else:
            print('Error: Valor no válido')
def main():
    while True:
        while True:
            menu()
            try:
                opcion = int(input("Ingrese una opcion del menú: "))
                break
            except ValueError:
                print("ERROR: Valor no válido.")
        print()
        
        if opcion == 0:
            break
        if opcion >= 1 and opcion<= 5:
            while True:
                try:
                    numero1 = float(input("Ingrese el primero número: "))
                    break
                except ValueError:
                    print("ERROR: Valor no válido")
            while True:
                try:
                    numero2 = float(input("Ingrese el segundo número: "))
                    break
                except ValueError:
                    print("ERROR: Valor no válido")
                 
        if opcion == 1:
            resultado = math.suma(numero1, numero2)
            print(f"{numero1} + {numero2} = {resultado}")
            cleaning()
        elif opcion == 2:
            resultado = math.resta(numero1, numero2)
            print(f"{numero1} - {numero2} = {resultado}")
            cleaning()
        elif opcion == 3:
            resultado = math.multiplicacion(numero1, numero2)
            print(f"{numero1} * {numero2} = {resultado:.2f}")
            cleaning()
        elif opcion == 4:
            resultado = math.division(numero1, numero2)
            print(f"{numero1} / {numero2} = {resultado:.2f}")
            cleaning()
        elif opcion == 5:
            resultado = math.potencia(numero1, numero2)
            print(f"{numero1} ** {numero2} = {resultado:.2f}")
            cleaning()
        elif opcion == 6:
            while True:
                try:
                    numero = float(input("Ingrese el número radicando: "))
                    break
                except ValueError:
                    print("ERROR: Valor no válido")
            resultado = math.raiz_cuadrada(numero)
            print(f"{numero} ** 0.5 = {resultado:.2f}")
            cleaning()
        print("\n")

    print("Gracias por usar su calculadora *-*")
            
if __name__ == '__main__':
    main()