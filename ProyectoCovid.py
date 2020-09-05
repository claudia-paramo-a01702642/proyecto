import tkinter as tk

def imprimir_menu():
    """
Mostrar al usuario las opciones disponibles
"""
    print("\n\n")
    print("1. Información.")
    print("2. Estadística.")
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
    print("\n\nRecomendaciones sobre Covid.")
    
def sintomas_comunes_covid():
    num_sintomas = 0
    print("\n\nCuál es su temperatura?")
    val_temp = float(input())
    val_fiebre = mide_temperatura(val_temp)
    if val_fiebre == 0:
        print("\n\nSu temperatura es normal")
    elif val_fiebre == 1:
        print("\n\nSe encuentra en estado febril,deberá revisar la temperatura constantemente")
    else:
        print("\n\nUsted presenta fiebre elevada")
        num_sintomas = num_sintomas + 1
    
    print("\n\nEn la escala del 0 al 5, donde 0 es  un malestar muy bajo o nulo y 5 es un malestar muy fuerte")
    print("\n\n¿Cuánto es el cansancio que siente?")
    nivel_sintomas = int(input())
    val_escala = mide_escala(nivel_sintomas)
    if val_escala == 3:
        print("\n\nEl nivel de cansancio leve no es un síntoma de covid")
    elif val_escala == 4 :
        print("\n\nEl cansancio moderado no es un síntoma de Covid")
    else:
        print("\n\nEl cansancio constante representa un síntoma de Covid")
        num_sintomas = num_sintomas + 1
        
    print("\n\nEn la escala del 0 al 5, donde 0 es  un malestar muy bajo o nulo y 5 es un malestar muy fuerte")
    print("\n\n¿Cuánto es el dolor de cabeza y/o cuerpo que siente?")
    nivel_sintomas = int(input())
    val_escala = mide_escala(nivel_sintomas)
    if val_escala == 3:
        print("\n\nEl nivel de dolor leve no es un síntoma de covid")
    elif val_escala == 4 :
        print("\n\nEl dolor moderado no es un síntoma de Covid")
    else:
        print("\n\nEl dolor constante representa un síntoma de Covid")
        num_sintomas = num_sintomas + 1
        
    print("\n\n¿Ha presentado tos seca recientemente?")
    print("\n\n S para representar que ha presentado y N para representar que no ha presentado el síntoma")
    val_tos = input()
    if val_tos == 'S' :
        num_sintomas = num_sintomas + 1
        
    print("\n\n El número de síntomas comunes que presenta es : %i " % (num_sintomas))
    return(num_sintomas)

       
       
def mide_escala(val_escala) :
    if val_escala >= 0 and  val_escala <=1 :
        return(3)
    elif val_escala >= 2 and val_escala <=3 :
        return(4)
    else:
        return(5)
    


def mide_temperatura(val_temp):
    if val_temp <= 37:
        return(0)
    elif val_temp > 37 and val_temp <= 37.8:
        return(1)
    else:
        return(2)
    

    
    




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
    
    if opcion_menu == "4" :
        num_sintomas = sintomas_comunes_covid()
        if num_sintomas >= 3 :
            print("\n\nSe recomienda consultar a un especialista, ya que presenta varios síntomas preocupantes")
            
        

        

        
    
        
    opcion_salir = input("\n\n¿Tienes alguna duda adicional? \nPresiona S o cualquier otra tecla para salir")

print("Gracias por participar! hasta luego")


 
root = tk.Tk()
root.title("Bienvenido al portal de apoyo sobre Covid-19")
label = tk.Label(root,text="1.Información", fg="black")
label.pack()
label2 = tk.Label(root,text="2. Estadística", fg="black")
label2.pack()
label3 = tk.Label(root,text="3. Recomendaciones", fg="black")
label3.pack()
label4 = tk.Label(root,text="4. Evaluacion diagnóstica", fg="black")
label4.pack()

label4 = tk.Label(root,text="Estare migrando a un programa con frames lo que tenia en consola", fg="black")
label4.pack()

button = tk.Button(root, text='Salir', width=25,command=quit)
button.pack()
root.mainloop()

# La biblioteca que ocuparé será para cambiar el formato del programa a uno gráfico, que consta de ventanas y objetos como etiquetas
# Puse como ejemplo algo sencillo de como sería la colocación de opciones de mi programa