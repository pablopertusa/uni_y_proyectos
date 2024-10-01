# -*- coding: utf-8 -*-

######################################################################
# Poned/pon aquí vuestros/tu nombre/s y apellidos:
# Pablo Pertusa Canales
#
######################################################################

import pathlib

# actividad 1
def explorar(fs_node):
    if fs_node.is_file ():
        print(fs_node)
    else:
        print(fs_node)
        for entry in fs_node.iterdir():
            explorar(entry)

# actividad 2
def contar_lineas(fs_node, word):
    """
    'fs_node' es un objeto creado con pathlib de tipo fichero.
    Esta función asume que 'word' es una palabra EN MINÚSCULA.
    Debe contar y devolver el número de líneas del fichero
    'fs_node' que contiene la palabra 'word'
    """
    
    a = 0
    with fs_node.open () as f:
        for linea in f:
            palabras = linea[:-1].lower().split()
            if word in palabras:
                a += 1
    return a
                
# actividad 3
def explorar_contar(fs_node, word):
    """
    'fs_node' es un objeto creado con pathlib de tipo directorio.
    Asume que 'word' es una palabra EN MINÚSCULA
    """
    
    if fs_node.is_file():
        n = 0
        n = contar_lineas(fs_node, word)
        print (f'{n:4d}', fs_node)
        return n
    
    else:
        a = 0
        for entry in fs_node.iterdir():
            a += explorar_contar(entry, word)
        print (f'{a:4d}', fs_node)
        return a
            
            
# programa principal (no cambiéis nada en esta parte)
def main():
    opcion = ""
    while opcion not in ('1','2','3'):
        opcion = input('Elige actividad:\n 1) Recorrido recursivo\n'+
                       ' 2) Contar lineas\n 3) Recorrido recursivo '+
                       'contando lineas\nOpcion: ')
        if opcion not in ('1','2','3'):
            print('Opcion incorrecta')

    ruta = input("Nombre del fichero o carpeta (enter para 'GCD'): ")
    if ruta == '':
        ruta = 'GCD'
    fs_node = pathlib.Path(ruta)
    
    if not fs_node.exists():
        print(f"Error: no se encuentra el fichero o carpeta '{fs_node}'")
        return
    
    elif opcion == '1':
        if not fs_node.is_dir():
            print(f"Error: {fs_node} no es un directorio")
            return
        explorar(fs_node)
    else:
        word = input('Palabra a buscar: ').lower()
        if opcion == '2':
            if not fs_node.is_file():
                print(f"Error: {fs_node} no es un fichero")
                return
            cuenta = contar_lineas(fs_node, word)
            print(f'Hay {cuenta} lineas con la palabra {word}')
        else:
            explorar_contar(fs_node, word)

if __name__ == '__main__':
    main()