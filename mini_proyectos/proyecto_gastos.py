"""Primer desafio de Mini proyecto: Hacer una aplicación en consola que 
 permita agregar, mostrar y sumar los gastos ingresados por el usuario:"""

gastos = {}

def agregar_gastos(gastos, nombre, monto):
    gastos[nombre] = monto
         
def mostrar_gastos(gastos):
    if gastos:
        print("Gastos:")
        for nombre, monto in gastos.items():
            print(f"Nombre: {nombre} || Valor: ${monto}")
    else:
        print("La lista esta vacia!")        



def total_gastos(gastos):
    if gastos:
        montos = gastos.values()
        suma_gastos = sum(montos)
        print(f"La suma total gastada es de: ${suma_gastos}")
    else:
        print("La lista esta vacia!")

def menu():
    print("\nBienvenido a la app para agregar, sumar y listar gastos en consola")
    while True:
        print("-" * 70)
        print("Menu Principal:")
        print("1- Agregar gastos")
        print("2- Mostrar gastos")
        print("3- Mostrar total gastado")
        print("4- Salir del programa")
        print("-" * 70)
        opcion = int(input("Seleccione una opción para continuar: "))
        
        match opcion:
            case 1:
                while True:
                    print("-" * 70)
                    nombre = input("\nIngrese el nombre del gasto: ")
                    monto = int(input(f"Ingrese el monto de {nombre}: $ "))
                    agregar_gastos(gastos, nombre, monto)
                    print(f"El gasto: {nombre} fue agregado con éxito!")
                    seguir = input("Desea seguir agregando productos? (si/no): ")
                    if seguir.lower() == "si":
                        continue
                    elif seguir.lower() == "no":
                        break
            case 2:
                mostrar_gastos(gastos)
            case 3:
                total_gastos(gastos)
            case 4:
                print("\nGracias por usar el programa! Hasta pronto :) ")
                print("-" * 70)
                break
            case _:
                print("\nOpción no válida! Por favor intente nuevamente")
                print("-" * 70)            



menu()