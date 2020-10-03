from tkinter import *
from tkinter import messagebox
import tkinter as tk


def muestra_informacion():
    """
Mostrar al usuario las opciones disponibles
"""
    textOpciones.set("Los coronavirus son una extensa familia de virus que pueden causar enfermedades tanto en animales como en humanos. \nEn los humanos, se sabe que varios coronavirus causan infecciones respiratorias que pueden ir desde el resfriado común hasta enfermedades más graves como el síndrome respiratorio de Oriente Medio (MERS) y el síndrome respiratorio agudo severo (SRAS). \n El coronavirus que se ha descubierto más recientemente causa la enfermedad por coronavirus COVID-19. \n * información obtenida de https://www.who.int/es/emergencies/diseases/novel-coronavirus-2019/advice-for-public/q-a-coronaviruses ")
    desabilitaEvaluacion()

def muestra_recomendaciones():
    textOpciones.set("Hay varias precauciones que se pueden adoptar para reducir la probabilidad de contraer o propagar la COVID‑19: \n\n Lávese las manos a fondo y con frecuencia usando un desinfectante a base de alcohol o con agua y jabón. \n Mantenga una distancia mínima de un metro entre usted y los demás. \n Evite ir a lugares concurridos. \n Evite tocarse los ojos, la nariz y la boca. \n Mantener una buena higiene respiratoria. \n Permanezca en casa y aíslese incluso si presenta síntomas leves como tos, dolor de cabeza y fiebre ligera hasta que se recupere. \n Si tiene fiebre, tos y dificultad para respirar, busque atención médica, pero en la medida de lo posible llame por teléfono con antelación y siga las indicaciones de la autoridad sanitaria local.  \n * Información obtenida de https://www.who.int/es/emergencies/diseases/novel-coronavirus-2019/advice-for-public/q-a-coronaviruses")
    desabilitaEvaluacion()
  
def changeTextOpcion_evaluacion():
    textOpciones.set("")
    abilitaEvaluacion()
  
def mide_temperatura(val_temp):
    if val_temp <= 37:
        return(0)
    elif val_temp > 37 and val_temp <= 37.8:
        return(1)
    else:
        return(2)
  
def evaluar_sintomas(val_temp,val_cansancio,val_dolor,val_tos):
    
    num_sintomas = 0
    val_fiebre = mide_temperatura(val_temp)
  
    if val_fiebre == 0:
       txt_temp="\n\nSu temperatura es normal";
    elif val_fiebre == 1:
        txt_temp="\n\nSe encuentra en estado febril,deberá revisar la temperatura constantemente"
    else:
        txt_temp="\n\nUsted presenta fiebre elevada"
        num_sintomas = num_sintomas + 1
    
    val_escala = mide_escala(val_cansancio)
    if val_escala == 3:
        txt_cans="\n\nEl nivel de cansancio leve no es un síntoma de covid"
    elif val_escala == 4 :
        txt_cans="\n\nEl cansancio moderado no es un síntoma de Covid"
    else:
        txt_cans="\n\nEl cansancio constante representa un síntoma de Covid"
        num_sintomas = num_sintomas + 1
        
    val_escala = mide_escala(val_dolor)
    if val_escala == 3:
        txt_dolor="\n\nEl nivel de dolor leve no es un síntoma de covid"
    elif val_escala == 4 :
        txt_dolor="\n\nEl dolor moderado no es un síntoma de Covid"
    else:
        txt_dolor="\n\nEl dolor constante representa un síntoma de Covid"
        num_sintomas = num_sintomas + 1
        
    if val_tos == 1 :
        text_tos="\n\nLa tos seca representa un sintoma de Covid"
        num_sintomas = num_sintomas + 1
        
    textFinal="\n\n El número de síntomas comunes que presenta es : "  + str(num_sintomas)
    textOpciones.set(txt_temp+txt_cans+txt_dolor+text_tos+textFinal)
        
def mide_escala(val_escala) :
    if val_escala >= 0 and  val_escala <=1 :
        return(3)
    elif val_escala >= 2 and val_escala <=3 :
        return(4)
    else:
        return(5)
    

def cmdEvaluar():
     evaluar_sintomas(float(entry_temp.get()), val_cansancio.get(),val_dolor.get(),val_tos.get())

def desabilitaEvaluacion():
    
    entry_temp["state"] = DISABLED
    radio_cansancio1["state"] = DISABLED
    radio_cansancio2["state"] = DISABLED
    radio_cansancio3["state"] = DISABLED
    radio_cansancio4["state"] = DISABLED
    radio_cansancio5["state"] = DISABLED
    radio_dolor1["state"] = DISABLED
    radio_dolor2["state"] = DISABLED
    radio_dolor3["state"] = DISABLED
    radio_dolor4["state"] = DISABLED
    radio_dolor5["state"] = DISABLED
    radio_si ["state"] = DISABLED
    radio_no["state"] = DISABLED

    button_revisar["state"] = DISABLED
    Bguardar["state"] = DISABLED
    canvas_temperaturas.delete("all")

    
def abilitaEvaluacion():
    
    entry_temp["state"] = NORMAL
    radio_dolor1["state"] = NORMAL
    radio_dolor2["state"] = NORMAL
    radio_dolor3["state"] = NORMAL
    radio_dolor4["state"] = NORMAL
    radio_dolor5["state"] = NORMAL
    radio_cansancio1["state"] = NORMAL
    radio_cansancio2["state"] = NORMAL
    radio_cansancio3["state"] = NORMAL
    radio_cansancio4["state"] = NORMAL
    radio_cansancio5["state"] = NORMAL
    radio_si ["state"] = NORMAL
    radio_no["state"] = NORMAL

    button_revisar["state"] = NORMAL
    Bguardar["state"] = NORMAL
    canvas_temperaturas.delete("all")
    
def graficar_temperatura():
    i = 0
    canvas_temperaturas.delete("all")
    print(lista_temperatura)
    
    while (i< len(lista_temperatura)):
        canvas_temperaturas.create_rectangle(20 * i, 80 - (80 - (39 -float( lista_temperatura[i])) * 20), 20 * i +15, 80, fill="blue")
        i+=1

# El ciclo servirá para graficar los valores de temperatura que el usuario vaya agregando
#  Las gráficas sólo aparecen cuando se oprime el botón de graficar y permanecen desabilitadas si se oprimen otras opciones del menú
# Para determinar el ancho de las gráficas, mi escala es 1 grado por cada 20 puntos de la gráfica, teniendo como valor máximo el 39 y mínimo el 35

def guardar_temperatura():
    lista_temperatura.append(entry_temp.get())
    messagebox.showinfo("", "Registro correctamente guardado en la lista")

# En la versión anterior tenía una lista predefinida y en esta entrega estoy creando una lista que se irá llenando mediante la entrada de datos de temperatura
#Esta lista la estoy leyendo en el método de la entrega anterior 

"""

 ========  main frame ========================================
"""
  
root = Tk()
root.geometry("900x550+10+10") # width x height + x_offset + y_offset
root.title("Bienvenido al portal de apoyo sobre COVID 19")
textOpciones = tk.StringVar()
textOpciones.set("Presiona alguna de las opciones que deseas conocer")
        
panelPrincipal = PanedWindow(height=550)
panelPrincipal.pack(fill=BOTH)

lista_temperatura = []

"""

 ========  panel menú principal ========================================
 """

panelBotones = PanedWindow(panelPrincipal, orient=VERTICAL,width=200)
panelPrincipal.add(panelBotones)

labelBotones = LabelFrame(panelBotones, text="Opciones disponibles")
labelBotones.pack(fill="both", expand="yes")
panelBotones.add(labelBotones)

BOpc1 = Button(labelBotones, text ="1.- Información", command = muestra_informacion)
BOpc1.pack( side = TOP, anchor=W, fill=X ,expand=YES) 
#labelBotones.add(BOpc1)


BOpc2 = Button(labelBotones, text ="2.- Recomendaciones", command = muestra_recomendaciones)
BOpc2.pack( side = TOP, anchor=W, fill=X, expand=YES) 
#labelBotones.add(BOpc2)

BOpc3 = Button(labelBotones, text ="3.- Evaluación Diagnóstica", command = changeTextOpcion_evaluacion)
BOpc3.pack( side = TOP, anchor=W, fill=X, expand=YES) 
#labelBotones.add(BOpc3)

BOpc4 = Button(labelBotones, text ="Salir", command=quit)
BOpc4.pack( side = BOTTOM) 
#labelBotones.add(BOpc4)

"""

 ========  panel de información ========================================
 """

info_panel = PanedWindow(panelPrincipal, orient=VERTICAL)
panelPrincipal.add(info_panel)

label_info = LabelFrame(info_panel, text="")
label_info.pack(fill="both", expand="yes")
info_panel.add(label_info)

info_label= Label(label_info, text="", textvariable=textOpciones,wraplength=280)
info_label.pack()

canvas_temperaturas = Canvas(label_info, width=220, height=100)
canvas_temperaturas.pack(side=BOTTOM)


Bgraficar = Button(label_info, text ="Graficar datos de temperatura", command = graficar_temperatura)
Bgraficar.pack( side = BOTTOM) 


"""

 ========  panel de evaluación diagnóstica ========================================
 """

test_panel= PanedWindow(panelPrincipal, orient=VERTICAL)
panelPrincipal.add(test_panel)


label_test = LabelFrame(test_panel, text="")
label_test.pack(fill="both", expand="yes")
test_panel.add(label_test)

label_temperatura= Label(label_test, text="Temperatura:")
label_temperatura.pack(side=TOP)

entry_temp= Entry(label_test, width=4)
entry_temp.pack(side=TOP)
entry_temp.focus_force()
Bguardar= Button(label_test, text ="Guardar registro de temperatura", command = guardar_temperatura)
Bguardar.pack( side = TOP) 


label_cansancio= Label(label_test, text="\n\n¿Cuánto es el cansancio que siente?")
label_cansancio.pack(side=TOP)

val_cansancio = IntVar()
radio_cansancio1 = Radiobutton(label_test, text="No Presente", variable=val_cansancio, value=1)
radio_cansancio1.pack()
radio_cansancio2 = Radiobutton(label_test, text="Poco", variable=val_cansancio, value=2)
radio_cansancio2.pack()
radio_cansancio3 = Radiobutton(label_test, text="Moderado", variable=val_cansancio, value=3)
radio_cansancio3.pack()
radio_cansancio4 = Radiobutton(label_test, text="Mucho", variable=val_cansancio, value=4)
radio_cansancio4.pack()
radio_cansancio5 = Radiobutton(label_test, text="Extremo", variable=val_cansancio, value=5)
radio_cansancio5.pack()


label_dolorcabeza= Label(label_test, text="\n\n¿Cuánto es el dolor de cabeza y/o cuerpo que siente?")
label_dolorcabeza.pack(side=TOP)

val_dolor = IntVar()
radio_dolor1 = Radiobutton(label_test, text="No Presente", variable=val_dolor, value=1)
radio_dolor1.pack()
radio_dolor2 = Radiobutton(label_test, text="Poco", variable=val_dolor, value=2)
radio_dolor2.pack()
radio_dolor3 = Radiobutton(label_test, text="Moderado", variable=val_dolor, value=3)
radio_dolor3.pack()
radio_dolor4 = Radiobutton(label_test, text="Mucho", variable=val_dolor, value=4)
radio_dolor4.pack()
radio_dolor5 = Radiobutton(label_test, text="Extremo", variable=val_dolor, value=5)
radio_dolor5.pack()

label_tos= Label(label_test, text="\n\n¿Ha presentado tos seca recientemente?")
label_tos.pack(side=TOP)

val_tos = IntVar()
radio_si = Radiobutton(label_test, text="Si", variable=val_tos, value=1)
radio_si.pack()
radio_no = Radiobutton(label_test, text="No", variable=val_tos, value=2)
radio_no.pack()

button_revisar = Button(label_test,text="Evaluar Síntomas", command=cmdEvaluar)
button_revisar.pack(side=BOTTOM)

desabilitaEvaluacion()








mainloop()


# La biblioteca que ocuparé será para cambiar el formato del programa a uno gráfico, que consta de ventanas y objetos como etiquetas
# Esta biblioteca sirve para crear los frames que se ven en el programa, lo cual da un mejor orden y presentación al programa
# La biblioteca tkinter es una multiplataforma que sirve para crear interfaces gráficas de usuario
# Para el proyecto estoy ocupando principalmente la biblioteca para crear paneles,botones,labels y campos de entrada
