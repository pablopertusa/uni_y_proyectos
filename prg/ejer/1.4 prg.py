# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 20:13:28 2023

@author: pablo
"""

def leerDivisas(nFichero):
    d={'EUR':'1'}
    try:
        f=open(nFichero,'r')
        for l in f:
            linea=l[:-1].split()
            d[linea[0]]=linea[1]
        f.close()
        return d
    except FileNotFoundError:
        print('No existe el fichero')
        
def leerPrecios(dic,fPrecios):
    d={}
    try:
        f=open(fPrecios,'r')
        for l in f:
            linea=l[:-1].split()
            if linea[len(linea)-1] not in dic:
                precio=float(linea[len(linea)-1])
                l=[]
                for i in linea[:-1]:
                    l+=[i]
                producto=' '.join(l)
                d[producto]=precio
            else:
                moneda=linea[len(linea)-1]
                precio=linea[len(linea)-2]
                l=[]
                for i in linea[:-2]:
                    l+=[i]
                producto=' '.join(l)
                precio=float(dic[moneda])*float(precio)
                d[producto]=precio
        f.close()
        suma=0
        for i in d:
            suma+=d[i]
        for i in d:
            print(f'{d[i]} euros ({i})')
        return suma
    except FileNotFoundError:
        print('No existe el fichero')
        return None

d = leerDivisas('monedas.txt')
suma = leerPrecios(d ,'precios.txt')
print ( " -" *40)
print (f'{suma:8.2f} euros en total')