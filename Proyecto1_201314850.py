from tkinter import *
from tkinter import filedialog as FileDialog
from io import open
from graphviz import Digraph
import os.path

ruta = "" # La utilizaremos para almacenar la ruta del fichero


import webbrowser

import os

def crearDirectorio(directorio):
    os.makedirs(directorio, exist_ok=True)

#dot = Digraph(comment='The Round Table')
#dot.node('A', 'King Arthur')
#dot.node('B', 'Sir Bedevere the Wise')
#dot.node('L', 'Sir Lancelot the Brave')

#dot.edges(['AB', 'AL'])
#dot.edge('B', 'L', constraint='false')

#dot.render('test-output/round-table.gv', view=True)

def jsReporteIdentificador(listaEstados, listaValores, tipoValor, directorioRuta):
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
        ruta = directorioRuta +'/Identificador.gv'
        dot.render(ruta, view=True)
    elif tipoValor == 3:
        ruta = directorioRuta +'/CadenaDoble.gv'
        dot.render(ruta, view=True)
    elif tipoValor == 3.5:
        ruta = directorioRuta +'/CadenaSimple.gv'
        dot.render(ruta, view=True)
    elif tipoValor == 4:
        ruta = directorioRuta +'/Numero.gv'
        dot.render(ruta, view=True)



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
    

def analizarJS(contenido, ruta):
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
    directorioRuta = ""
    banderaDirectorio = False    
    #htmlErrores = open('ReporteErroresJS.html','w')
    mensajeError = "<html><head></head><style>table {  font-family: arial, sans-serif;  border-collapse: collapse;  width: 100%;}td, th {  border: 1px solid #dddddd;  text-align: left;  padding: 8px;}tr:nth-child(even) {  background-color: #dddddd;}</style><body><table style=\"width:100%\"><tr><th>No.</th><th>Linea</th><th>Columna</th><th>Descripcion</th></tr>"
    #htmlErrores.write(mensajeError)
    contadorError = 1
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
                valor.find
                x=x-1
                if banderaDirectorio == False:
                    if "PATHW: " in valor:
                        banderaDirectorio = True
                        crearDirectorio(valor[9:])
                        directorioRuta = valor[9:]                
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
                else:
                    tipovalor = 2
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
                    jsReporteIdentificador(listaEstados,listaValores,tipovalor,directorioRuta)
                    banderaPalabraR = True
            elif tipovalor == 3:
                if banderaCadenaDoble == False:
                    jsReporteIdentificador(listaEstados,listaValores,tipovalor,directorioRuta)
                    banderaCadenaDoble = True
            elif tipovalor == 3.5:
                if banderaCadenaSimple == False:
                    jsReporteIdentificador(listaEstados,listaValores,tipovalor,directorioRuta)
                    banderaCadenaSimple = True
            elif tipovalor == 4:
                if banderaNumero == False:
                    jsReporteIdentificador(listaEstados,listaValores,tipovalor,directorioRuta)
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
            mensajeError =mensajeError+ "<tr><th>" + repr(contadorError) + "</th><th>" +repr(inicioValorFila) + "</th><th>"+ repr(inicioValorColum) + "</th><th>El caracter " + valor + " no pertenece al lenguaje</th></tr>"
            #htmlErrores.write(mensajeError) 
            contadorError = contadorError + 1
            paraImprimirConsola = valor + " fila-col " + repr(inicioValorFila) + "-" +repr(inicioValorColum) + "\n"
            text2.insert(END, paraImprimirConsola)
            print(paraImprimirConsola)
            valor = ""  
            estado = 0
            x=x-1            
        x += 1  
    if estado != 0:
        mensajeError = mensajeError+ "<tr><th>" + repr(contadorError) + "</th><th>" +repr(inicioValorFila) + "</th><th>"+ repr(inicioValorColum) + "</th><th>Los caracteres " + valor + " no pertenece al lenguaje</th></tr>"
        #htmlErrores.write(mensajeError) 
        contadorError = contadorError + 1
        paraImprimirConsola = valor + " fila-col " + repr(inicioValorFila) + "-" +repr(inicioValorColum) + "\n"
        text2.insert(END, paraImprimirConsola)
        print(paraImprimirConsola)
        valor = ""  
        estado = 0
        x=x-1        
    mensajeError= mensajeError + "</table></body></html>"
       
    htmlNombre = directorioRuta + "\Reporte Errores JS.html"
    rutaO = ruta
    direc, nombre = os.path.split(rutaO)
    ruta = directorioRuta + "/" +nombre
    contenido2 = texto.get(1.0,'end-1c')
    fichero = open(ruta, 'w+')
    fichero.write(contenido2)
    fichero.close()
    htmlErrores = open(htmlNombre,'w')
    htmlErrores.write(mensajeError)
    htmlErrores.close()    
    
    webbrowser.open_new_tab(htmlNombre)        

    
    
    
def esPalabraReservadaCSS(palabra):
    if palabra == "color":
        return True
    elif palabra == "border":
        return True
    elif palabra == "text-align":
        return True
    elif palabra == "front-weight":
        return True
    elif palabra == "padding-left":
        return True  
    elif palabra == "padding-top":
        return True
    elif palabra == "line-height":
        return True    
    elif palabra == "margin-top":
        return True
    elif palabra == "margin-left":
        return True
    elif palabra == "display":
        return True
    elif palabra == "top":
        return True 
    elif palabra == "float":
        return True
    elif palabra == "min-width":
        return True    
    elif palabra == "background-color":
        return True
    elif palabra == "Opacity":
        return True  
    elif palabra == "font-family":
        return True
    elif palabra == "font-size":
        return True  
    elif palabra == "padding-right":
        return True
    elif palabra == "padding":
        return True 
    elif palabra == "width":
        return True 
    elif palabra == "margin-right":
        return True
    elif palabra == "margin":
        return True    
    elif palabra == "position":
        return True
    elif palabra == "right":
        return True  
    elif palabra == "clear":
        return True
    elif palabra == "max-height":
        return True  
    elif palabra == "background-image":
        return True
    elif palabra == "background":
        return True   
    elif palabra == "font-style":
        return True 
    elif palabra == "font":
        return True 
    elif palabra == "padding-bottom":
        return True 
    elif palabra == "display":
        return True 
    elif palabra == "height":
        return True 
    elif palabra == "margin-bottom":
        return True 
    elif palabra == "border-style":
        return True 
    elif palabra == "bottom":
        return True 
    elif palabra == "left":
        return True 
    elif palabra == "max-width":
        return True  
    elif palabra == "min-height":
        return True     
    elif palabra == "px":
        return True 
    elif palabra == "em":
        return True 
    elif palabra == "vh":
        return True 
    elif palabra == "vw":
        return True 
    elif palabra == "in":
        return True 
    elif palabra == "cm":
        return True 
    elif palabra == "mm":
        return True 
    elif palabra == "pt":
        return True 
    elif palabra == "pc":
        return True   
    elif palabra == "red":
        return True 
    elif palabra == "purple":
        return True 
    elif palabra == "rgba":
        return True  
    elif palabra == "url":
        return True    
    elif palabra == "relative":
        return True     
    else:
        return False
    
def analizarCSS(contenido, ruta):
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
    root2 = Tk()
    root2.title("Reporte CSS")
    texto3 = Text(root2)
    texto3.pack(fill="both", expand=1)
    texto3.config(bd=0, padx=6, pady=4, font=("Consolas",12))    
    x=0
    directorioRuta = ""
    listaValores = []
    listaEstados = []
    banderaDirectorio = False
    #htmlErrores = open('asdf/Reporte Errores CSS.html','w')
    mensajeError = "<html><head></head><style>table {  font-family: arial, sans-serif;  border-collapse: collapse;  width: 100%;}td, th {  border: 1px solid #dddddd;  text-align: left;  padding: 8px;}tr:nth-child(even) {  background-color: #dddddd;}</style><body><table style=\"width:100%\"><tr><th>No.</th><th>Linea</th><th>Columna</th><th>Descripcion</th></tr>"
    #htmlErrores.write(mensajeError)
    contadorError = 1
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
            elif contenido[x] == '"':  # cadena
                estado = 5
                columna = columna + 1
                valor = valor + contenido[x]               
            elif contenido[x] == '(':
                estado = -1
                listaEstados.extend([-1])               
                listaValores.extend([contenido[x]])                 
                columna = columna + 1
                valor = valor + contenido[x]  
            elif contenido[x] == ')':
                estado = -1
                listaEstados.extend([-1])               
                listaValores.extend([contenido[x]])                 
                columna = columna + 1
                valor = valor + contenido[x]    
            elif contenido[x] == '{':
                estado = -1
                listaEstados.extend([-1])               
                listaValores.extend([contenido[x]])                 
                columna = columna + 1
                valor = valor + contenido[x]  
            elif contenido[x] == '}':
                estado = -1
                listaEstados.extend([-1])               
                listaValores.extend([contenido[x]])                 
                columna = columna + 1
                valor = valor + contenido[x] 
            elif contenido[x] == ';':
                estado = -1
                listaEstados.extend([-1])               
                listaValores.extend([contenido[x]])                 
                columna = columna + 1
                valor = valor + contenido[x]  
            elif contenido[x] == '.':
                estado = -1
                listaEstados.extend([-1])               
                listaValores.extend([contenido[x]])                 
                columna = columna + 1
                valor = valor + contenido[x]  
            elif contenido[x] == ',':
                estado = -1
                listaEstados.extend([-1])               
                listaValores.extend([contenido[x]])                 
                columna = columna + 1
                valor = valor + contenido[x]  
            elif contenido[x] == ':':
                estado = -1
                listaEstados.extend([-1])               
                listaValores.extend([contenido[x]])                 
                columna = columna + 1
                valor = valor + contenido[x]
            elif contenido[x] == '*':
                estado = -1
                listaEstados.extend([-1])               
                listaValores.extend([contenido[x]])                 
                columna = columna + 1
                valor = valor + contenido[x]   
            elif contenido[x] == '#':
                estado = -1
                listaEstados.extend([-1])               
                listaValores.extend([contenido[x]])                 
                columna = columna + 1
                valor = valor + contenido[x] 
            elif contenido[x] == '%':
                estado = -1
                listaEstados.extend([-1])               
                listaValores.extend([contenido[x]])                 
                columna = columna + 1
                valor = valor + contenido[x]                 
            elif contenido[x] == '-': 
                estado = -1
                listaEstados.extend([-1])               
                listaValores.extend([contenido[x]])                 
                columna = columna + 1
                valor = valor + contenido[x]   
            elif (contenido[x] >= '0' and contenido[x] <= '9') or (contenido[x] >= 'A' and contenido[x] <= 'F') or (contenido[x] >= 'a' and contenido[x] <= 'f'): # posible numero
                if (contenido[x] >= 'A' and contenido[x] <= 'F') or (contenido[x] >= 'a' and contenido[x] <= 'f'):
                    estado = 15  #es numero o palabra
                else:
                    estado = 13  #es numero
                columna = columna + 1
                valor = valor + contenido[x]                 
            elif (contenido[x] >= 'A' and contenido[x] <= 'Z') or (contenido[x] >= 'a' and contenido[x] <= 'z'): # posible palabra o identificador
                estado = 11
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
            if contenido[x] == '*': # comentario multilinea
                estado = 3
                columna = columna + 1
                valor = valor + contenido[x]
            else:
                estado = -2
                x=x-1 
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
                listaEstados.extend([-1])
                listaValores.extend([contenido[x]])                
                valor = valor + contenido[x] 
                if banderaDirectorio == False:
                    if "PATHW: " in valor:
                        banderaDirectorio = True
                        crearDirectorio(valor[9:-2])
                        directorioRuta = valor[9:-2]
                        
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

        elif estado == 11:  # posible palabra o identificador
            if (contenido[x] >= 'A' and contenido[x] <= 'Z') or (contenido[x] >= 'a' and contenido[x] <= 'z') : # sigo en posible palabra o identificador
                columna = columna + 1
                valor = valor + contenido[x]  #48 - 57
            elif contenido[x] >= '0' and contenido[x] <= '9': # numero entonces es identificador
                estado = 12
                columna = columna + 1
                valor = valor + contenido[x]
            elif contenido[x] == '-': # - 
                columna = columna + 1
                valor = valor + contenido[x]                  
            else:  # acepta la palabra reservada o posible identificador
                estado = -1
                if esPalabraReservadaCSS(valor):
                    # poner tipovalor correcto palabra reservada
                    tipovalor = 1
                else:
                    tipovalor = 2
                x=x-1        
        elif estado == 12: # es un identificador si o si
            if (contenido[x] >= 'A' and contenido[x] <= 'Z') or (contenido[x] >= 'a' and contenido[x] <= 'z') : # sigo en posible palabra o identificador
                columna = columna + 1
                valor = valor + contenido[x]  #48 - 57
            elif contenido[x] >= '0' and contenido[x] <= '9': 
                columna = columna + 1
                valor = valor + contenido[x]
            elif contenido[x] == '-': # - -
                columna = columna + 1
                valor = valor + contenido[x]                  
            else:  # acepta el identificador
                estado = -1
                if esPalabraReservadaCSS(valor):
                    # poner tipovalor correcto palabra reservada
                    tipovalor = 1
                else:
                    tipovalor = 2                
                x=x-1    
        elif estado == 13: # posible numero
            if contenido[x] >= '0' and contenido[x] <= '9': 
                columna = columna + 1
                valor = valor + contenido[x]
            elif contenido[x] == '.': # . entonces es numero con decimales
                estado = 14
                columna = columna + 1
                valor = valor + contenido[x]
            elif  (contenido[x] >= 'A' and contenido[x] <= 'F') or (contenido[x] >= 'a' and contenido[x] <= 'f'):
                if len(valor) > 5:
                    estado = -1
                    tipovalor = 4
                    x=x-1                       
                estado = 20 
                columna = columna + 1
                valor = valor + contenido[x]
            else:  # acepta el identificador
                estado = -1
                # valortipo de identificador
                tipovalor = 4
                x=x-1  
        elif estado == 20:
            if contenido[x] >= '0' and contenido[x] <= '9': # numero
                if len(valor) > 5:
                    estado = -2
                    x=x-1
                else:                    
                    columna = columna + 1
                    valor = valor + contenido[x]  
            elif  (contenido[x] >= 'A' and contenido[x] <= 'F') or (contenido[x] >= 'a' and contenido[x] <= 'f'):
                if len(valor) > 5:
                    estado = -2
                    x=x-1
                else:
                    columna = columna + 1
                    valor = valor + contenido[x]      
         
            else:  # acepta el numero con decimales
                if len(valor) == 6:
                    estado = -1
                    # valortipo de identificador
                    tipovalor = 4
                    x=x-1
                else:
                    estado = -2
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
        elif estado == 15: # posible numero color
            if contenido[x] >= '0' and contenido[x] <= '9': # numero
                if len(valor) > 5:
                    estado = 12  
                columna = columna + 1
                valor = valor + contenido[x]  
            elif  (contenido[x] >= 'A' and contenido[x] <= 'F') or (contenido[x] >= 'a' and contenido[x] <= 'f'):
                if len(valor) > 5:
                    estado = 12
                columna = columna + 1
                valor = valor + contenido[x]      
            elif  (contenido[x] >= 'A' and contenido[x] <= 'Z') or (contenido[x] >= 'a' and contenido[x] <= 'z') or contenido[x] == '-':
                estado = 12
                columna = columna + 1
                valor = valor + contenido[x]                 
            else:  # acepta el numero con decimales
                if len(valor) == 6:
                    estado = -1
                    # valortipo de identificador
                    tipovalor = 4
                    x=x-1
                else:
                    estado = -1
                    # valortipo de identificador
                    tipovalor = 2
                    x=x-1    
        elif estado == -1:   #estado de aceptacion para todos
            listaValores.pop()
            inicioTag = texto.index(CURRENT)
            texto.insert(END, valor)
            texto3.insert(END, "Estados -> ")
            texto3.insert(END, listaEstados)
            texto3.insert(END, "\nCaracteres acceptados - > ")
            texto3.insert(END, listaValores)
            texto3.insert(END, "\nToken -> ")
            texto3.insert(END, valor)  
            texto3.insert(END, "\n\n")
            finTag = texto.index(CURRENT)
            nombreTag = "nombre" + repr(contadorTag)
            contadorTag = contadorTag + 1          
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
            inicioError = texto3.index(CURRENT)
            listaEstados.extend([-2])
            texto3.insert(END, "Error\n")
            finError = texto3.index(CURRENT)
            texto3.tag_add("error", inicioError, finError)
            texto3.tag_config("error", foreground="red")              
            texto3.insert(END, "Estados -> ")
            texto3.insert(END, listaEstados)
            texto3.insert(END, "\nCaracteres acceptados - > ")
            texto3.insert(END, listaValores)
            texto3.insert(END, "\nToken -> ")
            texto3.insert(END, valor)  
            texto3.insert(END, "\n\n")            
            mensajeError = mensajeError + "<tr><th>" + repr(contadorError) + "</th><th>" +repr(inicioValorFila) + "</th><th>"+ repr(inicioValorColum) + "</th><th>El caracter " + valor + " no pertenece al lenguaje</th></tr>"
            #htmlErrores.write(mensajeError) 
            contadorError = contadorError + 1
            paraImprimirConsola = valor + " fila-col " + repr(inicioValorFila) + "-" +repr(inicioValorColum) + "\n"
            text2.insert(END, paraImprimirConsola)
            print(paraImprimirConsola)
            valor = ""  
            estado = 0
            x=x-1            
        x += 1  
    if estado != 0:
        inicioError = texto3.index(CURRENT)
        listaEstados.extend([-2])
        texto3.insert(END, "Error\n")
        finError = texto3.index(CURRENT)
        texto3.tag_add("error", inicioError, finError)
        texto3.tag_config("error", foreground="red")              
        texto3.insert(END, "Estados -> ")
        texto3.insert(END, listaEstados)
        texto3.insert(END, "\nCaracteres acceptados - > ")
        texto3.insert(END, listaValores)
        texto3.insert(END, "\nToken -> ")
        texto3.insert(END, valor)  
        texto3.insert(END, "\n\n")          
        mensajeError = mensajeError + "<tr><th>" + repr(contadorError) + "</th><th>" +repr(inicioValorFila) + "</th><th>"+ repr(inicioValorColum) + "</th><th>Los caracteres " + valor + " no pertenece al lenguaje</th></tr>"
        #htmlErrores.write(mensajeError) 
        contadorError = contadorError + 1
        paraImprimirConsola = valor + " fila-col " + repr(inicioValorFila) + "-" +repr(inicioValorColum) + "\n"
        text2.insert(END, paraImprimirConsola)
        print(paraImprimirConsola)
        valor = ""  
        estado = 0
        x=x-1      
    mensajeError= mensajeError +"</table></body></html>"
    htmlNombre = directorioRuta + "\Reporte Errores CSS.html"
    rutaO = ruta
    direc, nombre = os.path.split(rutaO)
    ruta = directorioRuta + "/" +nombre
    contenido2 = texto.get(1.0,'end-1c')
    fichero = open(ruta, 'w+')
    fichero.write(contenido2)
    fichero.close()
    htmlErrores = open(htmlNombre,'w')
    htmlErrores.write(mensajeError)
    htmlErrores.close()    
    
    webbrowser.open_new_tab(htmlNombre)          
    root2.mainloop()
    
def analizarRMT(contenido):
    print("nada")    

def nuevo():
    global ruta
    mensaje.set("Nuevo fichero")
    ruta = ""
    nombreRuta = ""
    texto.delete(1.0, "end")
    root.title("Mi editor")

def abrir():
    global ruta
    mensaje.set("Abrir fichero")
    ruta = FileDialog.askopenfilename(
        initialdir='.', 
        filetypes=(("Ficheros de texto", "*.js *.css *.html *.rmt"),),
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
        analizarJS(contenido, ruta)
        
    elif extension == ".css":
        analizarCSS(contenido, ruta)
        
    elif extension == ".rmt":
        analizarRMT(contenido, ruta)
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