"""
Este modulo exporta las siguientes funciones:

pedir_campos(campos,titulo="",permite_vacios=False):
notificar(msg,titulo="",ok=False,esperar=True):
listar(lista,titulo="",esperar=True):
menu(options,clear_screen=True):
seleccionar_fichero(msg, save_mode=False):

"""

import os

def pedir_campos(campos,titulo="", permite_vacios=False):
    if titulo!='':
        print("\n--- "+titulo+" ---")
    resul = []
    for campo in campos:
        respuesta =input(campo+": ")
        while respuesta=="" and permite_vacios==False:
            respuesta =input(campo+": ")
        resul.append(respuesta)
    return tuple(resul)

def pedir_campo(campo,titulo='',permite_vacio=False):
    return pedir_campos([campo],titulo=titulo,
                        permite_vacios=permite_vacio)[0]

def notificar(msg,titulo="",ok=False,esperar=True):
    if titulo!='':
        print("\n--- "+titulo+" ---")
    print(msg)
    if esperar:
        input("Pulse enter para continuar")

def listar(lista,titulo="",esperar=True):
    if titulo!='':
        print("\n--- "+titulo+" ---")
    for item in lista:
        print(item)
    if esperar:
        input("Pulse enter para continuar")

def menu(options, clear_screen=True):
    while True:
        if clear_screen:
            os.system("cls" if os.name=="nt" else "clear")
        d = [] # asocia índice a lo que devuelve
        i = 0
        for item in options:
            if isinstance(item,str): # es un título
                print(item)
            else: # es una tupla
                i += 1
                descr,returned = item
                print(f" {i:>2}) {descr}")
                d.append(returned)
        op = 0
        try:
            op = int(input("Opcion: "))
        except ValueError as err:
            op = 0
        if 0<op<=len(d):
            return d[op-1]
        print("Debes introducir una opcion correcta")
        if clear_screen:
            input("Pulsa enter para continuar")
    
def seleccionar_fichero(msg, es_directorio=False, save_mode=False):
    return pedir_campo(msg)

