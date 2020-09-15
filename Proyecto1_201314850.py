from tkinter import *
from tkinter import filedialog as FileDialog
from io import open
from graphviz import Digraph
import os.path

ruta = "" # La utilizaremos para almacenar la ruta del fichero

import webbrowser



#dot = Digraph(comment='The Round Table')
#dot.node('A', 'King Arthur')
#dot.node('B', 'Sir Bedevere the Wise')
#dot.node('L', 'Sir Lancelot the Brave')

#dot.edges(['AB', 'AL'])
#dot.edge('B', 'L', constraint='false')

#dot.render('test-output/round-table.gv', view=True)

def jsReporteIdentificador(listaEstados, listaValores, tipoValor):
    dot = Digraph(comment='AFD de Palabra Reservada')
    tamanioListaEstados = len(listaEstados)
    dot.attr('node', shape='doublecircle')
    dot.node(repr(listaEstados[tamanioListaEstados-1]))
    dot.attr('node', shape='circle') 
    x=0
    while x<tamanioListaEstados-1:
        dot.edge(repr(listaEstados[x]), repr(listaEstados[x+1]), label=repr(listaValores[x]))
        x = x+1
    if tipoValor == 2:
        dot.render('test-output/Identificador.gv', view=True)
    elif tipoValor == 3:
        dot.render('test-output/CadenaDoble.gv', view=True)
    elif tipoValor == 3.5:
        dot.render('test-output/CadenaSimple.gv', view=True)
    elif tipoValor == 4:
        dot.render('test-output/Numero.gv', view=True)



def esPalabraReservada(palabra):
    if palabra == "var":
        return True
    elif palabra == "if":
        return True
    elif palabra == "else":
        return True
    elif palabra == "for":
        return True
    elif palabra == "while":
        return True  
    elif palabra == "do":
        return True
    elif palabra == "continue":
        return True    
    elif palabra == "break":
        return True
    elif palabra == "return":
        return True
    elif palabra == "true":
        return True
    elif palabra == "false":
        return True 
    elif palabra == "function":
        return True
    elif palabra == "constructor":
        return True    
    elif palabra == "class":
        return True
    elif palabra == "Math":
        return True  
    elif palabra == "pow":
        return True
    elif palabra == "console":
        return True  
    elif palabra == "log":
        return True
    elif palabra == "this":
        return True    
    else:
        return False
    
def obtenerColorTag(tipo):
    if tipo == 1:
        return "red"
    elif tipo == 2:
        return "green"
    elif tipo == 3 or tipo == 3.5:
        return "yellow"
    elif tipo == 4:
        return "blue"
    elif tipo == 5:
        return "gray"
    elif tipo == 6:
        return "orange"
    else:
        return "black"
    

def analizarJS(contenido):
    estado = 0
    texto.delete(1.0, "end")
    fila = 1
    columna = 0
    tamanioContenido = len(contenido)
    valor = ""
    inicioValorColum = 0
    inicioValorFila = 0
    tipovalor = 0
    contadorTag = 0
    print (contenido[tamanioContenido-2] + contenido[tamanioContenido-1])
    x=0
    listaValores = []
    listaEstados = []
    banderaPalabraR = False
    banderaCadenaDoble = False
    banderaCadenaSimple = False
    banderaNumero = False
    
    f = open('holamundo.html','wb')
    
    mensaje = """<html>
    <head></head>
    <body><p>Hola Mundo!</p></body>
    </html>"""
    
    f.write(mensaje)
    f.close()
    
    webbrowser.open_new_tab('holamundo.html')    
    
    
    while x <tamanioContenido:
        
        if (estado>0):
            listaEstados.extend([estado])
            listaValores.extend([contenido[x]])
        if estado == 0:
            listaEstados = [0]
            listaValores = [contenido[x]]
            valor = ""
            tipovalor = 0
            inicioValorColum = columna
            inicioValorFila = fila
            if contenido[x] == '/':
                estado = 1 
                columna = columna + 1
                valor = valor + contenido[x]
            elif contenido[x] == '=':
                estado = -1
                tipovalor = 6
                columna = columna + 1
                valor = valor + contenido[x]   
            elif contenido[x] == '"':  # cadena
                estado = 5
                columna = columna + 1
                valor = valor + contenido[x]   
            elif contenido[x] == '\'':  # cadena
                estado = 7
                columna = columna + 1
                valor = valor + contenido[x]   
            elif contenido[x] == '(':
                estado = -1
                columna = columna + 1
                valor = valor + contenido[x]  
            elif contenido[x] == ')':
                estado = -1
                columna = columna + 1
                valor = valor + contenido[x]    
            elif contenido[x] == '{':
                estado = -1
                columna = columna + 1
                valor = valor + contenido[x]  
            elif contenido[x] == '}':
                estado = -1
                columna = columna + 1
                valor = valor + contenido[x] 
            elif contenido[x] == ';':
                estado = -1
                columna = columna + 1
                valor = valor + contenido[x]  
            elif contenido[x] == '.':
                estado = -1
                columna = columna + 1
                valor = valor + contenido[x]  
            elif contenido[x] == ',':
                estado = -1
                columna = columna + 1
                valor = valor + contenido[x]  
            elif contenido[x] == ':':
                estado = -1
                columna = columna + 1
                valor = valor + contenido[x]      
            elif contenido[x] == '+':
                estado = -1
                tipovalor = 6
                columna = columna + 1
                valor = valor + contenido[x]
            elif contenido[x] == '-':
                estado = -1
                tipovalor = 6
                columna = columna + 1
                valor = valor + contenido[x]   
            elif contenido[x] == '*':
                estado = -1
                tipovalor = 6
                columna = columna + 1
                valor = valor + contenido[x]                  
            elif contenido[x] == '!':
                estado = -1
                tipovalor = 6
                columna = columna + 1
                valor = valor + contenido[x]  
            elif contenido[x] == '>':
                estado = -1
                tipovalor = 6
                columna = columna + 1
                valor = valor + contenido[x] 
            elif contenido[x] == '<':
                estado = -1
                tipovalor = 6
                columna = columna + 1
                valor = valor + contenido[x]                                
            elif contenido[x] == '&': 
                estado = 9
                columna = columna + 1
                valor = valor + contenido[x] 
            elif contenido[x] == '|':  
                estado = 10
                columna = columna + 1
                valor = valor + contenido[x]
            elif contenido[x] == '[':
                estado = -1
                columna = columna + 1
                valor = valor + contenido[x] 
            elif contenido[x] == ']':
                estado = -1
                columna = columna + 1
                valor = valor + contenido[x]    
            elif (contenido[x] >= 'A' and contenido[x] <= 'Z') or (contenido[x] >= 'a' and contenido[x] <= 'z') : # posible palabra o identificador
                estado = 11
                columna = columna + 1
                valor = valor + contenido[x]                 
                
            elif contenido[x] >= '1' and contenido[x] <= '9': # posible numero
                estado = 13
                columna = columna + 1
                valor = valor + contenido[x]   
            elif contenido[x] == '0': # posible valor 0
                estado = 15
                columna = columna + 1
                valor = valor + contenido[x]                  
                
                
            elif contenido[x] == ' ':
                columna = columna + 1       
                texto.insert(END, " ")
            elif contenido[x] ==  '\t':
                columna = columna + 1
                texto.insert(END, "\t")
            elif contenido[x] == '\n':
                columna = 0
                fila = fila + 1
                texto.insert(END, "\n")
            elif  contenido[x] ==  '\r':
                pass 
            else:
                estado = -2
                columna = columna + 1
                valor = valor + contenido[x]               
            
        elif estado == 1:   #   /
            if contenido[x] == '/':  # comentario de 1 linea
                estado = 2
                columna = columna + 1
                valor = valor + contenido[x]
            elif contenido[x] == '*': # comentario multilinea
                estado = 3
                columna = columna + 1
                valor = valor + contenido[x]
            else:
                estado = -1  # aceptacion para simbolo / que seria un operador
                tipovalor = 6
                x=x-1 # regresamos en 1 para volver a leer el simbolo                
        elif estado == 2: # comentario de 1 linea
            if contenido[x] == '\n':  # comentario de 1 linea
                estado = -1 
                tipovalor = 5
                x=x-1
            else:
                columna = columna + 1
                valor = valor + contenido[x]     
        elif estado == 3: # comentario multilinea
            if contenido[x] == '*':  # posible salida
                estado = 4 
                columna = columna + 1
                valor = valor + contenido[x]                
            else:
                if contenido[x] == '\n':
                    columna = 0
                    fila = fila + 1
                columna = columna + 1
                valor = valor + contenido[x]   
        elif estado == 4: # comentario multilinea posible salida
            if contenido[x] == '/':  # salida
                estado = -1   
                columna = columna + 1
                tipovalor = 5
                valor = valor + contenido[x] 
            elif contenido[x] == '*':  # posible salida
                columna = columna + 1
                valor = valor + contenido[x]                
            else:
                estado = 3
                if contenido[x] == '\n':
                    columna = 0
                    fila = fila + 1                
                columna = columna + 1
                valor = valor + contenido[x]      
        elif estado == 5:    #   posible cadena
            if contenido[x] == '\\':  # posible uso de \"
                estado = 6
                columna = columna + 1
                valor = valor + contenido[x] 
            elif contenido[x] == '"': # fin y aceptacion de cadena
                estado = -1
                columna = columna + 1
                tipovalor = 3
                listaEstados.extend([-1])
                listaValores.extend([contenido[x]])                
                valor = valor + contenido[x]
            elif contenido[x] == '\n':  #salto de linea es porque hay error
                estado = -2
                x=x-1
            else:
                columna = columna + 1
                valor = valor + contenido[x] 
        elif estado == 6:
            if contenido[x] == '\n':  #salto de linea es porque hay error
                estado = -2
                x=x-1       
            else:
                columna = columna + 1
                valor = valor + contenido[x]
                estado = 5
        elif estado == 7:    #   posible cadena
            if contenido[x] == '\\':  # posible uso de \'
                estado = 8
                columna = columna + 1
                valor = valor + contenido[x]
            elif contenido[x] == '\'': # fin y aceptacion de cadena
                estado = -1
                columna = columna + 1
                tipovalor = 3.5
                listaEstados.extend([-1])
                listaValores.extend([contenido[x]])                 
                valor = valor + contenido[x]
            elif contenido[x] == '\n':  #salto de linea es porque hay error
                estado = -2
                x=x-1
            else:
                columna = columna + 1
                valor = valor + contenido[x] 
        elif estado == 8:
            columna = columna + 1
            valor = valor + contenido[x]
            estado = 7      
        elif estado == 9:
            if contenido[x] == '&':  # aceptacion de &&
                estado = -1
                columna = columna + 1
                valor = valor + contenido[x]
                tipovalor = 6
            else:  # error 
                estado = -2
                x=x-1        
        elif estado == 10:
            if contenido[x] == '|':  # aceptacion de ||
                estado = -1
                columna = columna + 1
                valor = valor + contenido[x]
                tipovalor = 6
            else:  # error 
                estado = -2
                x=x-1         
          
        elif estado == 11:  # posible palabra o identificador
            if (contenido[x] >= 'A' and contenido[x] <= 'Z') or (contenido[x] >= 'a' and contenido[x] <= 'z') : # sigo en posible palabra o identificador
                columna = columna + 1
                valor = valor + contenido[x]  #48 - 57
            elif contenido[x] >= '0' and contenido[x] <= '9': # numero entonces es identificador
                estado = 12
                columna = columna + 1
                valor = valor + contenido[x]
            elif contenido[x] == '_': # _ entonces es identificador
                estado = 12
                columna = columna + 1
                valor = valor + contenido[x]                  
            else:  # acepta la palabra reservada o posible identificador
                estado = -1
                if esPalabraReservada(valor):
                    # poner tipovalor correcto palabra reservada
                    tipovalor = 1
                    pass
                else:
                    tipovalor = 2
                    pass
                x=x-1
        elif estado == 12: # es un identificador si o si
            if (contenido[x] >= 'A' and contenido[x] <= 'Z') or (contenido[x] >= 'a' and contenido[x] <= 'z') : # sigo en posible palabra o identificador
                columna = columna + 1
                valor = valor + contenido[x]  #48 - 57
            elif contenido[x] >= '0' and contenido[x] <= '9': # numero entonces es identificador
                columna = columna + 1
                valor = valor + contenido[x]
            elif contenido[x] == '_': # _ entonces es identificador
                columna = columna + 1
                valor = valor + contenido[x]                  
            else:  # acepta el identificador
                estado = -1
                # valortipo de identificador
                tipovalor = 2
                x=x-1    
        elif estado == 13: # posible numero
            if contenido[x] >= '0' and contenido[x] <= '9': # numero entonces es identificador
                columna = columna + 1
                valor = valor + contenido[x]
            elif contenido[x] == '.': # . entonces es numero con decimales
                estado = 14
                columna = columna + 1
                valor = valor + contenido[x]                  
            else:  # acepta el identificador
                estado = -1
                # valortipo de identificador
                tipovalor = 4
                x=x-1   
        elif estado == 14: # posible numero con decimales
            if contenido[x] >= '0' and contenido[x] <= '9': # numero entonces es numero con decimales
                columna = columna + 1
                estado = 19
                valor = valor + contenido[x]                  
            else:  # acepta el numero sin el .
                estado = -1
                # valortipo de identificador
                tipovalor = 4
                columna = columna - 1
                x=x-2
                tamanioValor = len(valor)
                listaEstados.pop()
                listaValores.pop()
                valor = valor[:-1]
        elif estado == 19: # posible numer
            if contenido[x] >= '0' and contenido[x] <= '9': # numero
                columna = columna + 1
                valor = valor + contenido[x]                  
            else:  # acepta el numero con decimales
                estado = -1
                # valortipo de identificador
                tipovalor = 4
                x=x-1                  
        elif estado == 15: # posible numero 0
            if contenido[x] == '.': # . posible 0. algo
                estado = 16
                columna = columna + 1
                valor = valor + contenido[x]                  
            elif contenido[x] >= '0' and contenido[x] <= '9': # es un 054687 o algo similar que seria un error
                estado = 18
                columna = columna + 1
                valor = valor + contenido[x]                
            else:  # acepta 0
                estado = -1
                tipovalor = 4
                # valortipo de identificador
                x=x-1      
        elif estado == 16: # posible numero
            if contenido[x] >= '0' and contenido[x] <= '9': # numero entonces es 0.5 o algo similar
                estado = 17
                columna = columna + 1
                valor = valor + contenido[x]                  
            else:  # acepta el 0 y el . por separado
                estado = -1
                # valortipo de identificador
                tipovalor = 4
                columna = columna - 1
                x=x-2
                valor = "0"
                listaEstados.pop()
                listaValores.pop()                
        elif estado == 17: # posible numero 0.654
            if contenido[x] >= '0' and contenido[x] <= '9': # numero entonces es identificador
                columna = columna + 1
                valor = valor + contenido[x]                  
            else:  # acepta el 0.6546
                estado = -1
                # valortipo de identificador
                tipovalor = 4
                x=x-1              
        elif estado == 18:
            if contenido[x] >= '0' and contenido[x] <= '9': # siguen siendo numeros y los acpetamos para el error
                columna = columna + 1
                valor = valor + contenido[x]                  
            else:  # aceptamos toda la cadena como error
                estado = -2
                # valortipo de identificador
                x=x-1            
        elif estado == -1:   #estado de aceptacion para todos
            listaValores.pop()
            inicioTag = texto.index(CURRENT)
            texto.insert(END, valor)
            finTag = texto.index(CURRENT)
            nombreTag = "nombre" + repr(contadorTag)
            contadorTag = contadorTag + 1
            if tipovalor == 2:
                if banderaPalabraR == False:
                    jsReporteIdentificador(listaEstados,listaValores,tipovalor)
                    banderaPalabraR = True
            elif tipovalor == 3:
                if banderaCadenaDoble == False:
                    jsReporteIdentificador(listaEstados,listaValores,tipovalor)
                    banderaCadenaDoble = True
            elif tipovalor == 3.5:
                if banderaCadenaSimple == False:
                    jsReporteIdentificador(listaEstados,listaValores,tipovalor)
                    banderaCadenaSimple = True
            elif tipovalor == 4:
                if banderaNumero == False:
                    jsReporteIdentificador(listaEstados,listaValores,tipovalor)
                    banderaNumero = True
          
            texto.tag_add(nombreTag, inicioTag, finTag)
            colorTag = obtenerColorTag(tipovalor)
            texto.tag_config(nombreTag, foreground=colorTag)            
            valor = ""  
            tipovalor = 0
            estado = 0
            x=x-1
        elif estado == -2:      # estado de errores
            # agregar a la lista de errores
            #
            # inicioValorColum = columna
            # inicioValorFila = fila    
            paraImprimirConsola = valor + " fila-col " + repr(inicioValorFila) + "-" +repr(inicioValorColum) + "\n"
            text2.insert(END, paraImprimirConsola)
            print(paraImprimirConsola)
            valor = ""  
            estado = 0
            x=x-1            
        x += 1   
        
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
    texto.insert(END, " ")
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

text2 = Text(root)
#text2.pack(expand=1, fill=BOTH)

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