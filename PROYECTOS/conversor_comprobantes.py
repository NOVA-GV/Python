from pypdf import PdfReader,PdfWriter
import tkinter
from tkinter import ttk,filedialog
from pdf2image import convert_from_path
from PIL import Image
import os
from time import sleep

class Aplication():
    def AbrirArchivo(self,ventana):
        archivo = filedialog.askopenfilenames(parent=ventana,title="Abrir",initialdir="C:/",filetypes=(("Formato de documento Portable",
        "*.pdf"),("Todos los archivos","*.*")))
        self.archdir = ventana.tk.splitlist(archivo)
        #print(self.archdir)

    def ElegirRuta(self):
        ruta = filedialog.askdirectory(title="Guardar",initialdir="C:/")
        self.output = ruta

    def pdfgroup_to_pdf(files,output_path):
        writer = PdfWriter()
        for file in files:
            reader = PdfReader(file)
            for page in reader.pages:
                writer.add_page(page)
        temp_pdfimg = os.path.join(output_path, "temp_pdf.pdf")
        with open(temp_pdfimg, "wb") as temp_out:
            writer.write(temp_out)
        return temp_pdfimg

    def pdf_to_img(temp_pdfimg,output_path,img_paths):
        imgs = convert_from_path(temp_pdfimg)
        for i, image in enumerate(imgs):
            image_path= os.path.join(output_path, f"page {i + 1}.png")
            image.save(image_path, "PNG")
            img_paths.append(image_path)
    
    def img_to_pdf(output_path, img_paths):
        output_pdf = os.path.join(output_path, "resultado_final.pdf")
        final_writer = PdfWriter()
        for i in range(0,len(img_paths),4):
            new_page = Image.new("RGB",(2480,3508),"white")
            positions = [(0,0),(1240,0),(0,1754),(1240,1754)]
            for j in range(4):
                if i+j < len(img_paths):
                    img = Image.open(img_paths[i + j])
                    img.thumbnail((1240,1754))
                    new_page.paste(img,positions[j])
            temp_path = os.path.join(output_path+"/temp", f"temp_page_{i // 4 + 1}.pdf")
            new_page.save(temp_path, "PDF")
            temp_reader = PdfReader(temp_path)
            final_writer.add_page(temp_reader.pages[0])
        with open(output_pdf, "wb") as f_out:
            final_writer.write(f_out)
        try:
            os.path.exists(output_pdf)
        except:
            print("toy esperando ...")
            sleep(5.0)

    def delete_folder(path):
        files = os.listdir(path)
        for file in files:
            file_path= os.path.join(path,file)
            if os.path.isfile(file_path):
                os.remove(file_path)
        os.rmdir(path)

    def pdfconverter(self,files,output_path):
        os.makedirs(output_path + "/temp")
        #GENERA UN UNICO PDF EN BASE A LOS PDFS ENVIADOS
        temp_pdfimg = Aplication.pdfgroup_to_pdf(files,output_path + "/temp")
        #####################################
        #CONVIERTE TODAS LAS PAGINAS DEL PDF EN IMAGENES
        Aplication.pdf_to_img(temp_pdfimg,output_path+"/temp",self.img_paths)
        #####################################
        #CARGA TODAS LAS IMAGENES A UN SOLO PDF
        Aplication.img_to_pdf(output_path,self.img_paths)
        # BORRA TODOS LOS ARCHIVOS TEMPORALES
        Aplication.delete_folder(output_path+"/temp")
        



    def __init__(self,ventana):
        ####VENTANA####
        self.ventana = ventana
        self.ventana.config(bg="gray")
        self.ventana.geometry("860x500+550+250")
        #self.ventana.resizable(False,False)
        self.ventana.title("Script comprobantes")
    
        ####TEXTO####
        etiqueta = tkinter.Label(ventana, text= "script comprobantes", font="bold")
        etiqueta.pack()

        self.entrada = tkinter.Entry(ventana,bg="seagreen1")
        self.entrada.pack()
        self.entrada.insert(0, "C:/Users/Guillermo/Documents/PROYECTOS")

        ####VARIABLES####
        self.archdir = str()
        self.output = self.entrada.get()
        self.img_paths = []

        ####BOTONES####
        boton_examinar_abrir = tkinter.Button(ventana, text="Elegir Archivo", font="bold", command=lambda:self.AbrirArchivo(self.ventana), padx=30,pady=7.5)
        boton_examinar_abrir.pack(side="left")

        self.entrada.insert(0,self.archdir)

        boton_examinar_guardar = tkinter.Button(ventana, text="Ruta de guardado", font="bold", command=lambda:self.ElegirRuta(), padx=30,pady=7.5)
        boton_examinar_guardar.pack(side="right")

        boton_convertir = tkinter.Button(ventana, text="Convertir", font="bold", command=lambda:self.pdfconverter(self.archdir,self.output), padx=30,pady=7.5)
        boton_convertir.pack(side="bottom")


# MAIN
ventana = tkinter.Tk()
app = Aplication(ventana)
ventana.mainloop()
