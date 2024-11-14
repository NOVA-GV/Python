import base64
#import os
import tkinter
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont

class Aplicacion:
    def AbrirArchivo(self):
        archivo = filedialog.askopenfilename(title="Abrir",initialdir="C:/",filetypes=(("Archivos de texto",
        "*.txt"),("Archivos separados por comas","*.csv"),("Mapa de Bits","*.bmp"),("Todos los archivos","*.*")))
        self.archdir = archivo

    def ElegirRuta(self):
        ruta = filedialog.askdirectory(title="Guardar",initialdir="C:/")
        self.output = ruta

    def b64_to_png(self,nombre_archivo,ruta_salida):
        #Toma como parametro un archivo .txt codificado en base64 y devuelve un png
        with open(nombre_archivo,"r") as file:
            base64_str = file.read()
        img = base64.b64decode(base64_str)
        output = ruta_salida + "/output.png"
        with open(output,"wb") as file:
            file.write(img)
    
    def ascii_to_png(self,nombre_archivo,ruta_salida):
        with open(nombre_archivo,"r") as file:
            ascii_text = file.read()
        W,H = (3000,3000)
        img = Image.new("RGBA",(W,H),"white")
        draw = ImageDraw.Draw(img)
        font = ImageFont.load_default()
        bbox = draw.textbbox((0, 0), ascii_text, font=font)
        w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
        draw.text(((W-w)/2,(H-h)/2), ascii_text, fill="black")
        output = ruta_salida + "/output.png"
        img.save(output,"PNG")

    def __init__(self,ventana):
        ####VENTANA####
        self.ventana = ventana
        self.ventana.config(bg="gray")
        self.ventana.geometry("560x200")
        #self.ventana.resizable(False,False)
        self.ventana.title("B64 to PNG Converter")
    
        ####TEXTO####
        etiqueta = tkinter.Label(ventana, text= "B64 to PNG Converter", font="bold")
        etiqueta.pack()

        ####VARIABLES####
        self.archdir = str()
        self.output = str()

        ####BOTONES####
        boton_examinar_abrir = tkinter.Button(ventana, text="Elegir Archivo", font="bold", command=lambda:self.AbrirArchivo(), padx=30,pady=7.5)
        #boton_examinar_abrir.place(x=25, y=70)
        boton_examinar_abrir.pack(side="left")
        boton_examinar_guardar = tkinter.Button(ventana, text="Ruta de guardado", font="bold", command=lambda:self.ElegirRuta(), padx=30,pady=7.5)
        #boton_examinar_guardar.place(x=340, y=70)
        boton_examinar_guardar.pack(side="right")
        boton_convertir = tkinter.Button(ventana, text="Convertir", font="bold", command=lambda:self.b64_to_png(self.archdir,self.output), padx=30,pady=7.5)
        #boton_convertir.place(x=210,y=150)
        boton_convertir.pack(side="bottom")


############################################MAIN########################################
ventana = tkinter.Tk()
app = Aplicacion(ventana)
ventana.mainloop()
    #arch = "Ejercicios Relkou//imagen.txt"
    #b64_to_png(arch)


    # with open("Ejercicios Relkou//imagen.txt","r") as file:
    #     base64_str = file.read()
    # img = base64.b64decode(base64_str)
    # with open("Ejercicios Relkou//output.png","wb") as file:
    #     file.write(img)