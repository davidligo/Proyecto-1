from tkinter import *
from tkinter import filedialog as FileDialog
from io import open
import os.path

ruta = "" # La utilizaremos para almacenar la ruta del fichero

def analizarJS(contenido):
    estado = 0
    texto.delete(1.0, "end")
    fila = 1
    columna = 0
    tamanioContenido = len(contenido)
    valor = ""
    for x in range(tamanioContenido):
        if estado == 0:
            valor = ""
            if contenido[x] == '/':
                estado = 1 
                valor = valor + contenido[x]
                
            elif contenido[x] == ' ':
                columna = columna + 1       
                text2.insert(END, " ")
               
               
            elif contenido[x] ==  '\t':
                columna = columna + 1
                text2.insert(END, "\t")
                
            elif contenido[x] == '\n':
                columna = 0
                fila = fila + 1
                text2.insert(END, "\n")
                
            elif  contenido[x] ==  '\r':
                pass 
            
        elif estado == 1:
            if contenido[x] == '/':  # comentario de 1 linea
                estado = 2
                columna = columna + 1
                valor = valor + contenido[x]
            elif contenido[x] == '*': # comentario multi linea
                estado = 3
                columna = columna + 1
                valor = valor + contenido[x]
            else:
                estado = 0  # aceptacion para simbolo / que seria un operador
                x=x-1 # regresamos en 1 para volver a leer el simbolo
                
                
                
            
    print("nada")
    
def analizarCSS(contenido):
    print("nada")
    
def analizarHTML(contenido):
    print("nada")    

def nuevo():
    global ruta
    mensaje.set("Nuevo fichero")
    ruta = ""
    texto.delete(1.0, "end")
    root.title("Mi editor")

def abrir():
    global ruta
    mensaje.set("Abrir fichero")
    ruta = FileDialog.askopenfilename(
        initialdir='.', 
        filetypes=(("Ficheros de texto", "*.js *.css *.html"),),
        title="Abrir un fichero de texto")

    if ruta != "":
        fichero = open(ruta, 'r')
        contenido = fichero.read()
        texto.delete(1.0,'end')
        texto.insert('insert', contenido)
        fichero.close()
        root.title(ruta + " - Mi editor")

def guardar():
    mensaje.set("Guardar fichero")
    if ruta != "":
        contenido = texto.get(1.0,'end-1c')
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero guardado correctamente")
    else:
        guardar_como()

def guardar_como():
    global ruta
    mensaje.set("Guardar fichero como")

    fichero = FileDialog.asksaveasfile(title="Guardar fichero", 
        mode="w", defaultextension=".js")

    if fichero is not None:
        ruta = fichero.name
        contenido = texto.get(1.0,'end-1c')
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero guardado correctamente")
    else:
        mensaje.set("Guardado cancelado")
        ruta = ""
        
def posTextoClick(event):
    mensaje.set(texto.index(CURRENT))
    
def posTextoKey(event):
    mensaje.set(texto.index(CURRENT))    
        
        
def analisis():
    if ruta != "":
        contenido = texto.get(1.0,'end-1c')
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero guardado correctamente")
    else:
        guardar_como() 
    nombre, extension = os.path.splitext(ruta)
    contenido = texto.get(1.0,'end-1c')
    if extension == ".js":
        analizarJS(contenido)
        
    elif extension == ".css":
        analizarCSS(contenido)
        
    elif extension == ".html":
        analizarHTML(contenido)
    else:
        print() # error de extension 
            
    
    
    
    
    
    

# Configuracion de la raiz
root = Tk()
root.title("Mi editor")
#asdf_asdf_asdf_asdf = Tk()

# Menu superior
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo", command=nuevo)
filemenu.add_command(label="Abrir", command=abrir)
filemenu.add_command(label="Guardar", command=guardar)
filemenu.add_command(label="Guardar como", command=guardar_como)
filemenu.add_separator()
filemenu.add_command(label="Ejecutar Analisis", command=analisis)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)
menubar.add_cascade(menu=filemenu, label="Archivo")

# Caja de texto central
texto = Text(root)
texto.pack(fill="both", expand=1)
texto.config(bd=0, padx=6, pady=4, font=("Consolas",12))

# Monitor inferior
mensaje = StringVar()
mensaje.set(texto.index(CURRENT))
monitor = Label(root, textvar=mensaje, justify='left')
monitor.pack(side="left")
root.bind('<Button-1>', posTextoClick)
root.bind('<Key>', posTextoKey)
root.config(menu=menubar)

# Finalmente bucle de la apliacion
root.mainloop()