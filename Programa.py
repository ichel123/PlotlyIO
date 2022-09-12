#Autor: Ichel Delgado

import pandas as pd
import plotly.express as px
from tkinter import *
from PIL import ImageTk, Image

#Se crea la ventana donde se agregarán el resto de widgets de la interfaz gráfica
#Se establece un tamaño de ventana por defecto y se establece su nombre
root = Tk()
root.geometry("400x350")
root.title("Generador de gráficos")

#Título y subtitulo de la ventana
h1 = Label(root,text="Datos de violencia").pack()
h2 = Label(root,text="Departamento: Meta").pack()
#Se agrega una imagen a la ventana (escudo del Meta)
img = ImageTk.PhotoImage(Image.open("escudo_meta.jpg"))
label = Label(root,image=img)
label.pack()

#Se carga el archivo .csv de donde se tomarán los datos para graficar
data = pd.read_csv("osb_v-intrafamiliar.csv", encoding = 'latin-1',delimiter=',')
#Se crean variables para agregar a los menús desplegables y se les asignan unos valores por defecto, los cuales servirán para identificar el dato que se encontrará ahí
variable = StringVar(root)
variable.set("Tipo de violencia")
variable2 = StringVar(root)
variable2.set("Año")
#Se crean los botones con menús desplegables y se agregan a la ventana con la función .pack()
dropDown = OptionMenu(root, variable, "Intrafamiliar", "Abandono", "Economica","Emocional", "Fisica", "Negligencia", "Sexual", "Totales")
dropDown.pack()
dat = data['ano'].unique()
dropDown1 = OptionMenu(root, variable2, *dat)
dropDown1.pack()
#Se crea un método que se accionará cuando se de clic en el botón "verificar"
def verGrafico():
    #Si el usuario selecciona la opción para ver los datos de violencia totales, no se tomará en cuenta si se selecciona un año,
    # pues los datos se mostrarán como una sumatoria de todas los tipos de violencia para todo sexo durante cada año
    if(variable.get() == "Totales"):
        #Se crea la figura con los parámetros seleccionados y se muestra con la función .show()
        fig = px.scatter(data.groupby(['sexo'])['nocasos'].sum(),title="Cantidad de casos vs sexo de víctimas")
        fig.show()
    #Si selecciona alguna otrra opción, si se tomará en cuenta el año seleccionado, pues se sumarám todos los casos del tipo seleccionado
    #de ese año en específico y se mostrarán en el gráfico
    else:
        dataFrame = data[data['tipoviolencia'].str.contains(variable.get())&(data["ano"] == int(variable2.get()))]
        #Variable que establece el título que tendrá el gráfico dependiendo de las opciones seleccionadas por el usuario
        titulo = "Cantidad de casos de violencia " + str(variable.get()) + " VS sexo de víctimas en el año " + str(variable2.get())
        fig = px.bar(dataFrame.groupby(['sexo'])['nocasos'].sum(), title=titulo)
        fig.show()

#Se crea el botón que accionará el método verGrafico() y creará los gráficos
btnVer = Button(root,text="Verificar", command=verGrafico).pack()
root.mainloop()




