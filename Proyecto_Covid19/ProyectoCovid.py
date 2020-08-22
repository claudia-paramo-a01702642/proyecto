
def imprimir_menu():
    """
Mostrar al usuario las opciones disponibles
"""
    print("\n\n")
    print("1. Información.")
    print("2. Esadística.")
    print("3. Recomendaciones.")
    print("4. Evaluacion diagnóstica.")
 
def muestra_informacion():
    """
Mostrar al usuario las opciones disponibles
"""
    print("Info sobre Covid.")

def muestra_estadisticas():
    """
Mostrar al usuario las opciones disponibles
"""
    print("Estadisticas sobre Covid.")

def muestra_recomendaciones():
    """
Mostrar al usuario las opciones disponibles
"""
    print("Recomendaciones sobre Covid.")


"""
 ========  parte principal del programa ========================================
 """
print("Bienvenido al portal de apoyo sobre Covid-19")

opcion_salir = "S"

pausa = input("\n\nPresiona Enter para conocer las opciones")

while opcion_salir == "S" :

    imprimir_menu()

    opcion_menu = input("\n\n¿Que opción le gustaria consultar?")
    

    if opcion_menu == "1" :
        muestra_informacion()

    if opcion_menu == "2" :
        muestra_estadisticas()

    if opcion_menu == "3" :
        muestra_recomendaciones()
        
    opcion_salir = input("\n\n¿Tienes alguna duda adicional? \nPresiona S o cualquier otra tecla para salir")

print("Gracias por participar! hasta luego")



