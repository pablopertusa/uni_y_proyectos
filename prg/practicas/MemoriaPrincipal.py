import math
#
#      MEMORIA Principal
#.............................................................................................
#   Módulo con funciones y clases prácticas para simular
#                memoria principal y cache
#
#
#   Está organizado:
#     a) Constantes
#     b) Funciones
#     c) Clases
#
#.............................................................................................
#   CONSTANTES para la CACHE
POSTERIOR = 0
DIRECTA = 1
ALLOCATE = 0
NOALLOCATE = 1
FIFO = 0
LRU = 1
RANDOM = 2
#........................FUNCIONES VARIADAS:
#    Función :  BytesAPal
#       ENTRADA:  bytes_entran es un entero con cantidad de bytes
#                 bitspalabra: la cantidad de bits/palabra (entero)
#       SALIDA:   palabras que equivalen a bytes_entran
#
#     POSIBLES ERRORES:  Si bytes_entran no es divisible entre la
#                        cantidad de bytes/palabra, Ej. 2.5 retorna 2
def BytesAPal(bytes_entran, bitspalabra):

        bytespalabra = int(bitspalabra/8)
        return int(bytes_entran/ bytespalabra)
#........................ 
#    Función :  PalABytes
#       ENTRADA:  palabras es un entero
#                 bitspalabra: la cantidad de bits/palabra (entero)
#       SALIDA:   bytes que equivalen a palabras
#
def PalABytes(palabras,bitspalabra):
        bytespalabra = int(bitspalabra/8)
        return int(palabras* bytespalabra)
#.............................................................................................
#    Función :  TraduceD
#       ENTRADA:  caracter 
#                  
#       SALIDA:   retorna el decimal equivalente
#
#     POSIBLES ERRORES:   que el caracter sea minúsculas, no admitido
#
def TraduceD(caracter):
        if caracter == "A": return 10
        elif caracter == "B": return 11
        elif caracter == "C": return 12
        elif caracter == "D": return 13
        elif caracter == "E": return 14
        elif caracter == "F": return 15
        else:
                valor = int(caracter)
                return valor
#
#.............................................................................................
#    Función :  Traduce
#
#       ENTRADA:  valor in range[0,15] 
#                  
#       SALIDA:   retorna el caracter hexadecimal equivalente
#
#     POSIBLES ERRORES:   valor fuera de ese rango no controlado.
#
def Traduce(valor):
        if valor >= 10:
                if valor == 10: return "A"
                elif valor == 11: return "B"
                elif valor == 12: return "C"
                elif valor == 13: return "D"
                elif valor == 14: return "E"
                else: return "F"
        else: return str(valor)
#.....................................................................................................
#   Función: CambioBase_E
#
#       ENTRADA:  entero (valor entero) 
#                 base: la base a la que se desea traducir el entero
#       SALIDA:   retorna el valor equivalente convertirdo en la base 
#
#     POSIBLES ERRORES:   
#
def CambioBase_E(entero,base):
        if entero in range(0,base):
                return Traduce(entero)
        else:
                resto = entero %base
                cociente = entero // base
                return CambioBase_E(cociente,base)+Traduce(resto)
#.....................................................................................................
#   Función: Normaliza
#
#       ENTRADA:  cadena llega como un string de dígitos en hexadecimal,
#                   y puede tener mas o menos
#                   dígitos de los que se expresa en variable cantidad
#                 cantidad es un entero que representa cantidad de dígitos
#                   en hexadecimal que se desea tenga cadena
#       SALIDA:   retorna una cadena con tantos dígitos en hexadecimal
#                 como se indica en cantidad.
#                 Si cadena fuera mayor, se espera que sea 0XXXX, por tanto
#                       solo se elimina el primer dígito de la cadena.
#                       y si fuera menor, se le añaden ceros por arriba
#
#     POSIBLES ERRORES:  que la cadena enviada sea mayor que cantidad
#               y no tuviera el formato 0xxxx, 
#               Ejemplo    Normaliza("12345", 3) retornaria "2345"
#               Está pensada para normalizar:  Normaliza("0123",3) = "123"
#                                              Normaliza("23",4) = "0023"
def Normaliza(cadena, cantidad):
        l = len(cadena)
        if (l < cantidad):
                nuevacadena = "0"
                for i in range (1,cantidad-l):
                        nuevacadena = nuevacadena + "0"
                nuevacadena=nuevacadena+cadena
                return nuevacadena
        elif (l> cantidad):
                nuevacadena = ""
                for i in range (1,l):  # hago esto porque solo es uno demás
                        nuevacadena = nuevacadena + cadena[i]
                return nuevacadena
        else: return cadena
#.....................................................................................................
#
#   Función: TraduceAHexa
#
#       ENTRADA:  valor (entero) 
#                 digitos: cantidad de digitos hexa de salida
#       SALIDA:   retorna el valor equivalente en hexadecimal
#               como una secuencia de "digitos" caracteres
#
#     Ejemplo:   "000A" = TraduceAHexa(10,4)
#
#     POSIBLES ERRORES:   
#
def TraduceAHexa(valor, digitos):
        cadena = CambioBase_E(valor, 16)
        ncadena = Normaliza(cadena, digitos)
        return ncadena
#.....................................................................................................
#
#   Función: AHexa
#
#       ENTRADA:  dire (valor que llega de decimal), que normalmente será una dirección 
#                 nbits: cantidad de bits que tiene una dirección
#       SALIDA:   retorna el valor equivalente en hexadecimal
#               como una secuencia de caracteres según los "nbits" que 
#                tenga la direccion
#     Ejemplo:   "00000" = AHexa(0,20) Si la dirección es de 20 bits
#                "0000" = AHexa(0,16) Si la dirección es de 16 bits
#     POSIBLES ERRORES:   
#
def AHexa(dire, nbits): # Que llega en decimal, como un valor entero
        cantidad = math.ceil(nbits/4) # cantidad de bits hexa de una direccion
        return TraduceAHexa(dire, cantidad) 
#..................................................................................................
#      
#   Función: TraduceADecimal
#
#       ENTRADA:  hexa es una cadena de valores hexadecimales
#                  
#       SALIDA:   retorna el valor equivalente en decimal
#                
#
#     Ejemplo:   100 = TraduceADecimal("64")
#
#     POSIBLES ERRORES:   No admite valores fraccionarios ("64,2A")
#
def TraduceADecimal(hexa):
        valor_entero = 0;
        long_entero = len(hexa)-1 
 
        for indice in range(long_entero,-1,-1):
                q = TraduceD(hexa[long_entero-indice])
                peso = 16 ** indice
                valor_entero = valor_entero + peso * q
        return valor_entero
#.............................................................................................
#
#   Función: Convertir
#
#       ENTRADA:  dir es una cadena de caracteres.
#                    Puede expresarse en decimal   Convertir("100") = 100
#                                       en  hexa   Convertir("0x64) = 100 
#       SALIDA:   retorna el valor equivalente en decimal
#                
#
#     POSIBLES ERRORES:   No admite valores fraccionarios ("0x64,2A")
#
def Convertir(dir):
        l = len(dir)
        if l>2:
                if (dir[0]=="0" and dir[1]=="x"):  # Se trata de dirección en Hexadecimal
                        cadena =""
                        for i in range(2,l):
                                cadena = cadena + dir[i]
                        return TraduceADecimal(cadena)
        # Asumo que entonces llega en decimal
        return int(dir)
#..................................................................................................
#
#   Función: es_potencia_de_dos
#
#       ENTRADA:  numero es un valor decimal.
#
#       SALIDA:   True o False
#                
#
#     POSIBLES ERRORES:    
#
def es_potencia_de_dos(numero):
    if numero < 1:
        return False
    i = math.log(numero, 2)
    return 0 == (i - math.floor(i))

#..................................................................................................     
#
#   Función: ConvertirAPrefijos
#
#       ENTRADA:  b es un valor decimal.
#
#       SALIDA:   cadena de caracteres equivalente, con prefijos
#                
#       Ejemplo:   ConvertirAPrefijos(2048) = "2.0 K"
#
#     POSIBLES ERRORES:  
#
def ConvertirAPrefijos(b):
         
        kas = 1024.0
        megas = 1048576.0
        gigas = 1073741824.0
        teras = 1099511627776.0
        petas = teras * 1024.0
        if b >= petas:
                return str(round(b/petas,1))+" P"
        elif b >= teras:
                return str(round(b/teras,1))+" T"
        elif (b >= gigas):
                return str(round(b/gigas,1))+" G"
        elif (b >= megas):
                return str(round(b/megas,1))+" M"
        elif (b >= kas):
                return str(round(b/kas,1))+" K"
        return str(round(b,1))+" "
#..................................................................................................     
#
#   Función: ConvertirAPrefijosI
#
#       ENTRADA:  b es un valor entero (llega en base 10)
#
#       SALIDA:   cadena de caracteres equivalente, con prefijos
#                
#       Ejemplo:   ConvertirAPrefijos(2048) = "2 K"
#
#     POSIBLES ERRORES:  
#
def ConvertirAPrefijosI(b):
        kas = 1024
        megas = 1048576
        gigas = 1073741824
        teras = 1099511627776
        petas = teras * 1024
        if (b >= petas):
                return str(int(b/petas))+" P"
        elif (b >= teras):
                return str(int(b/teras))+" T"
        elif (b >= gigas):
                return str(int(b/gigas))+" G"
        elif (b >= megas):
                return str(int(b/megas))+" M"
        elif (b >= kas):
                return str(int(b/kas))+" K"
        return str(int(b))+" "
#.............................................................................................
#    Funcion :  ABytes
#
#       ENTRADA:  cadena es un valor con/sin prefijo y unidades (b o B):
#           Ej.   12   = ABytes("12") 
#                 1024 = ABytes("1 KB")
#                 128  = ABytes("1 Kb")
#                     .... entiende hasta P
#
#       SALIDA:   valor equivalente en Bytes (en decimal)
#                  
#
def ABytes(cadena):

        l = len(cadena)
        if l <= 1:
                # Se trata de un dato que viene en Bytes
                return int(cadena)
        else: 
                if cadena[l-1] == 'b': # Entra en bits la info
                        EnBits = True
                        ultimo = 2
                elif cadena[l-1] == 'B': # Entra en Bytes la info
                        EnBits = False
                        ultimo = 2
                else:  # Es un dato sin unidades, en Bytes ya
                #        return int(cadena)
                        EnBits = False
                        ultimo = 1
                #  el dato viene con unidades
                #  ahora veamos si lleva prefijos
                if cadena[l-ultimo] == 'K':
                        uni = 1024
                elif cadena[l-ultimo] == 'M':
                        uni = 1024* 1024
                elif cadena[l-ultimo] == 'G':
                        uni = 1024 *1024 *1024
                elif cadena[l-ultimo] == 'T':
                        uni = 1024 *1024 *1024 *1024
                elif cadena[l-ultimo] == 'P':
                        uni = 1024 *1024 *1024 *1024 *1024
                elif cadena[l-ultimo] == ' ':
                        uni = 1
                else:   # Asumo que no lleva prefijos
                        uni = 1
                if uni==1: # El dato solo lleva unidades
                        if ultimo == 2:  # hay b o B
                                c = cadena[0:l-1]
                        else: return int(cadena) # el dato llega solo con valores 
                else :  
                        if ultimo == 2: #El dato lleva unidades y prefijo
                                c = cadena[0:l-2]
                        else: c = cadena[0:l-1] # el dato solo lleva prefijos
                valor = int(c)*uni
                if EnBits:
                        valor = valor/8
                return valor
#.............................................................................................
#    Funcion :  ValorConPrefijo
#
#       ENTRADA:  cadena es un valor con/sin prefijo:
#           Ej.   12 = ValorConPrefijo("12") 
#                 1024 = ValorConPrefijo("1K")
#                 .... = ValorConPrefijo("1M")
#                     .... entiende hasta P
#
#       SALIDA:   valor equivalente (en decimal)
#                
#       POSIBLES ERRORES:  ponerle un prefijo no conocido
#
# 
def ValorConPrefijo(cadena):
         
        l = len(cadena)
        if l <= 1:
                # Se trata de un dato que viene sin prefijos
                return float(cadena)
        else: 
                #  ahora veamos si lleva prefijos
                if cadena[l-1] == 'K':
                        uni = 1024
                elif cadena[l-1] == 'M':
                        uni = 1024* 1024
                elif cadena[l-1] == 'G':
                        uni = 1024 *1024 *1024
                elif cadena[l-1] == 'T':
                        uni = 1024 *1024 *1024 *1024
                elif cadena[l-1] == 'P':
                        uni = 1024 *1024 *1024 *1024 *1024
                elif cadena[l-1] == ' ':
                        uni = 1.0
                else:   # Asumo que no lleva prefijos
                        uni = 1.0
                if uni==1.0:
                        c=cadena
                else:
                        c=cadena[0:l-1]
                 
                valor = float(c)*uni
                return valor      
#.............................................................................................
#    Funcion :  LeerBitsPalabra
#
#       ENTRADA:  bitsdepalabra es un valor decimal
#
#       SALIDA:   
#            va a pedir por teclado que se introduzca una cantidad de bits
#            si la variable bitsdepalabra no es cero pregunta si se desea
#            cambiar por otra
#
#             Se pide un valor que sea potencia de 2.  Lo solicita hasta que
#             se cumpla o retorna sin leer
#
#             Si el valor introducido es correcto:
#               Retorna  True, bitspalabra, bytespalabra
#             Si el valor introducido no es correcto y el usuario no quiere
#                 seguir intentándolo:
#               Retorna  False, 0,0
#
#       POSIBLES ERRORES:   
#
# 
def LeerBitsPalabra(bitsdepalabra):
        resp = "s"
        if bitsdepalabra != 0: # Ya viene con un valor definido
                resp =input("Hay " +str(bitsdepalabra)+" bits/palabra. ¿Cambiar? (S/N)> ")
                if resp in ["N","n"]:
                        return True,bitsdepalabra,int(bitsdepalabra/8)
        while resp in ["S","s"]:
                        bitsmemoria = input("Indica bits/palabra (sin poner unidades): ")
                        bitsdatos = int(bitsmemoria)
                        bytespalabra = int(bitsdatos/8)
                        es = es_potencia_de_dos(bytespalabra)
                        if (es):
                                return True, bitsdatos, bytespalabra
                        else:
                                palabrasbloque = 0
                                print("Hay "+str(bytespalabra)+" B/pal, y tiene que ser potencia de 2")
                                resp = input("¿Quieres probar con otro valor? S/N ")
        return False, 0,0
 
#
#.............................................................................................
#    Funcion :  LeerTamanoBloque
#
#       ENTRADA:  palabrasbloque es un valor decimal
#                 bytespalabra es un valor decimal
#       SALIDA:   
#            va a pedir por teclado que se introduzca la cantidad de palabras/bloque
#            si la variable palabrasbloque no es cero pregunta si se desea
#            cambiar por otra
#
#            El valor se puede introducir en palabras o en bytes:
#            Ejemplo:   Si deseo 4 palabras/bloque, y sé que hay 2B/pal
#                   Puedo introducir   > 4  (sin unidades), significa 4 palabras
#                                      > 8B  (indicando que son bytes mediante la B)
#                    En ambos casos la función retorna 4 
#            Con las palabras bloque que se introducen calcula la cantidad de bytes/bloque
#            y si no es potencia de 2 vuelve a solicitar de nuevo el valor
#
#             Si el valor introducido cumple:
#               Retorna  True, palabrasbloque
#             Si el valor introducido no es correcto y el usuario no quiere
#                 seguir intentándolo:
#               Retorna  False, 0
#
#       POSIBLES ERRORES:   
#
# 
def LeerTamanoBloque(palabrasbloque, bytespalabra):
        respuestas = ["s", "si" ,"S" ,"Si" ,"SI"]
        resp = 's'
        es = False
        if palabrasbloque != 0 :
                resp =input("Hay " +str(palabrasbloque)+" palabras/bloque. ¿Cambiar? (S/N)> ")
                if resp in ["N","n"]:
                        return True,palabrasbloque              
        while (resp in respuestas):   
                print("Indica la cantidad de palabras que tiene un bloque (en Bytes poner B):")
                print(" (Ejemplo si hay 4 palabras/bloque, y cada palabra 2 bytes, poner > 4  o poner > 8B) ")
                pal= input(" > ")
                if pal[len(pal)-1] == "B":
                        bytesbloque= pal[0:len(pal)-1]
                        palabrasbloque = int(int(bytesbloque)/bytespalabra)
                else:
                        palabrasbloque = int(pal)
                es = es_potencia_de_dos(palabrasbloque)
                if (es):
                        resp = "N"
                else:
                        palabrasbloque = 0
                        resp = input("Tiene que ser potencia de 2 ¿Quieres probar con otro valor? S/N ")
        return es, palabrasbloque

#.............................................................................................
#    Función:  TipoPolitica
#       
#
#       ENTRADA:  cadena con tipo politica
#              Ej.   TipoPolitica("Allocate")
#       SALIDA:   constante interna equivalente
#                
#       POSIBLES ERRORES: No poner un tipo de politica conocido  
#
def TipoPolitica(tipo):
        if tipo in ["Allocate", "allocate","ALLOCATE"]:
                return ALLOCATE
        if tipo in ["NotAllocate", "notallocate","NOTALLOCATE","Not Allocate","not allocate", "NOT ALLOCATE"]:
                return NOALLOCATE
        return -1
#
#.............................................................................................
#    Función:  TipoAlgoritmo   
#
#       ENTRADA:  cadena con tipos de algoritmos de reemplazo
#              Ej.   TipoAlgoritmo("Fifo")
#       SALIDA:   constante interna equivalente 
#                
#       POSIBLES ERRORES: No poner un tipo de algoritmo conocido  
#
def TipoAlgoritmo(tipo):

        if tipo in ["FIFO", "Fifo","fifo"]:
                return FIFO
        if tipo in ["LRU", "lru","Lru"]:
                return LRU
        if tipo in ["Aleatoria", "aleatoria","ALEATORIA"]:
                return RANDOM
        return -1
#.............................................................................................
#    Función:  TipoEscritura
#
#       ENTRADA:  cadena con tipos de politicas de escritura
#              Ej.   TipoEscritura("Directa")
#       SALIDA:   constante interna equivalente 
#                
#       POSIBLES ERRORES: No poner un tipo de politica escritura conocido  
#
def TipoEscritura(tipo):

        if tipo in ["Directa", "directa","DIRECTA","Through","through","THROUGH"]:
                return DIRECTA
        if tipo in ["Posterior", "posterior","POSTERIOR","Back","back","BACK"]:
                return POSTERIOR
        return -1
#.............................................................................................
#       CLASES   CLASES    CLASES   CLASES    CLASES    CLASES   CLASES
#.............................................................................................
# 
#
#    Objeto :  Direccion
#.............................................................................................

class Direccion():

        def __init__(self, dir, bits):
                self.dir = dir    # valor en decimal de la direccion
                self.nbits = bits # numero de bits de la direccion

        def Nueva(self, dir):
                self.dir = dir
        def NuevaEnHexa(self,ValorDir):  #  Se le pasa una dirección en Hexa
                dir = TraduceADecimal(ValorDir)
        def Ver(self):
                return self.dir
        def VerHexa(self):   # Queremos que retorne en Hexa el atributo dir
                cadena= CambioBase_E(self.dir,16)
                cantidad = math.ceil(self.nbits/4) # cantidad de bits hexa de una direccion
                return Normaliza(cadena, cantidad)
        def Bloque(self,tamanobloque): # indica el campo bloque al que pertenece
                return self.dir // tamanobloque
        def Desplazamiento(self,tamanobloque): # indica el campo desplazamiento dentro del bloque
                return self.dir % tamanobloque
        def EsMenor(self, valor): # Añadido 29/11/2019 para añadir vectores a la memoria
                return valor <= self.dir
        
#.............................................................................................
#
#    Objeto :  Elemento
#.............................................................................................

class Elemento():
        Bytes = 1
        
        def __init__(self, tipo):
                self.Cambia(tipo)
                
        def Cambia(self, tipo):
                self.tipo = tipo
                if (tipo == "byte"):
                        self.Bytes = 1
                elif (tipo == "short"):
                         self.Bytes = 2
                elif (tipo == "half"):
                         self.Bytes = 2
                elif (tipo == "word"):
                         self.Bytes = 4
                elif (tipo == "int"):
                         self.Bytes = 4
                elif (tipo == "char"):
                         self.Bytes = 1
                elif (tipo == "float"):
                         self.Bytes = 4
                elif (tipo == "double"):
                         self.Bytes = 8
                else:  self.Bytes = 1

        def NBytes(self):
                return self.Bytes
        
        def Alineamiento(self, direccion): # 30/11/2019 Para añadir Vectores en memoria
                # Dada una direccion indica la cantidad de bytes correctores que
                # hacen falta para ubicar un dato de dicho tipo
                if (self.tipo == "byte") or (self.tipo == "char"):
                        return 0
                elif (self.tipo == "short") or (self.tipo == "half"):
                        # Tiene que ser dirección par
                        resto = direccion % 2
                        
                elif (self.tipo == "word") or (self.tipo == "int") or (self.tipo == "float"):
                        # Tiene que ser mútiplo de cuatro
                        resto = direccion % 4
                        
                        if resto != 0:
                                resto = 4- resto
                elif (self.tipo == "double"):
                        # Tiene que ser mútiplo de ocho
                        resto = direccion % 8
                        if resto != 0:
                                resto = 8-resto
                else:  resto = 0

                
                return resto
                
#.............................................................................................
#
#    Objeto :  Vector
#
#.............................................................................................

class Vector():
        
        elementos = 0

        def __init__(self, tipo, cantidad):
                self.tipo = Elemento(tipo)
                self.nombreTipo = tipo
                self.elementos = cantidad
                
       # Modificado dia 29/NOV/2019 para añadir vectores a la memoria
        def Inicializa(self, tipo, cantidad, direcc = 0, bits = 16):
                self.tipo.Cambia(tipo)
                self.nombreTipo = tipo
                self.elementos = cantidad
                a = self.tipo.Alineamiento(direcc)
                self.direccion = Direccion(direcc+a, bits)

                return a
                
        def DirInicial(self,direc, bits):
                self.direccion = Direccion(direc,bits)
                
        def NumBloques(self,tamanoBloque):

                ultimoBloque = self.BloqueElemento(self.elementos-1,tamanoBloque)
                primerBloque = self.direccion.Bloque(tamanoBloque)
                bloquesocupa = ultimoBloque - primerBloque +1

                return int(bloquesocupa),int(primerBloque)

        def BytesOcupa(self):
                bytesT = self.tipo.NBytes()
                return self.elementos * bytesT

        def BytesElemento(self,i):
                lsb = self.DireccionElemento(i)
                return  lsb+self.tipo.bytes-1, lsb

        def DireccionElemento(self,i):  # Numerando desde 0 .. elementos-1
                if i>=0 and i <= self.elementos:
                        return self.direccion.Ver()+(self.tipo.NBytes()*i)  # Retorna la dirección del elemento
                else: return -1
        def BloqueElemento(self,i,tamanoBloque):
                if i>=0 and i <= self.elementos:
                        dir = self.DireccionElemento(i)
                        blq = dir // tamanoBloque  # bloque final 
                        return int(blq)
                else: return -1
        def Presentacion(self,tamanoBloque):
                print("     Vector desde dirección : "+ str(self.direccion.Ver()))
                print("        Tiene "+str(self.elementos)+" elementos tipo "+self.nombreTipo)
                print("        Ocupa " + str(self.BytesOcupa()) + " Bytes ")
                bloq, primerBloque = self.NumBloques(tamanoBloque)
                print("        Ocupa "+str(bloq)+" bloques desde el bloque "+str(primerBloque))
#.............................................................................................
#
#    Objeto :  Memoria Principal
#
#.............................................................................................
class Memoria():
        palabras_bloque = 1
        f = 0 # Frecuencia del sistema
        frecuencia = 0.0
        bitsBloque = 0
        
        
        def __init__(self, bD, bP, bytesbloq=4,nvectores = 5): # Modificado dia 29/11/2019
                # He añadido la definición de vectores dentro de la memoria
                self.bits_direccion = bD  # bits de una dirección
                self.bits_palabra = bP    # bits que tiene una palabra de datos
                self.bytes_pal = int(bP/8)
                self.dirMin = Direccion(0, bD)
                self.dirMax = Direccion((2**bD)-1, bD)
                self.dirVec = 0 # dia 29/11/2019 para añadir vectores a la memoria
                self.sigVec = 0 # Esto sería el indice para ir añadiendo vectores
                self.maxVec = nvectores

                self.InitBloqueB(bytesbloq)

                # Aqui se crea un array de vectores
                self.datos = list()
                for i in range(nvectores):
                        #b = Vector("byte",1) # Por defecto, pero luego se puede cambiar
                        self.datos.insert(i,Vector("byte",1))
                        
        def EstablecerDireccion(self, direccion): # 29/11/2019 para vectores en memoria
                # simula la directiva .data del mips

                #  El valor en dirección puede llegar como un decimal: ej: 64
                #  o puede llegar como un hexadecimal: ej. 0x100
                direc = Convertir(direccion)
                if self.dirMax.EsMenor(direc):
                        self.dirVec= direc
                        
        def CreaVector(self, tipo, numeroelementos): # 29/11/2019 para vectores en memoria
                if self.sigVec < self.maxVec:

                        a = self.datos[self.sigVec].Inicializa(tipo, numeroelementos,self.dirVec,self.bits_direccion)
                        self.dirVec = self.dirVec + a  # a es el posible alineamiento
                        guarda = self.dirVec + self.datos[self.sigVec].BytesOcupa()
                        #print("  ")
                        #print("     CreaVector " + str(self.sigVec))
                        #print("           Añadiendo vector de tipo " + tipo + " en memoria " )
                        #print("           valores de " + str(self.datos[self.sigVec].tipo.NBytes())+" bytes(elemento)")
                        #print("           dirección es " + str(self.dirVec) + " Se alineó " + str(a)+" bytes ")
                        #print("           Direccion de inicio del siguiente elemento será: " + str (guarda))
                        #print(" ")
                        if self.dirMax.EsMenor(guarda):
                                self.dirVec = guarda 
                                self.sigVec = self.sigVec +1
                                return self.sigVec-1
                        else: # Caso en que el vector definido no cabe en la memoria
                                return -1  
                else: return -1  # Caso en que no queda espacio para otro vector
                
        def Vector(self, queVector, indice): # 29/11/2019 para vectores en memoria
                if queVector >= 0 and queVector < self.maxVec:
                      dirElemento = self.datos[queVector].DireccionElemento(indice)
                else: dirElemento = -1
                return dirElemento
        def PresentacionVectores(self): # 29/11/2019 para vectores en memoria
                print(" ")
                print("   Presentación de vectores definidos en memoria")
                print(" .................................................. ")
                for i in range(self.sigVec):
                        print(" VECTOR " + str(i))
                        self.datos[i].Presentacion(self.BytesPorBloque())
        def BloquesVector(self,indice): # 29/11/2019 para vectores en memoria
                if indice >=0 and indice < self.sigVec :
                        b, p = self.datos[indice].NumBloques(self.BytesPorBloque())
                        return b
                else: return -1
                
        def InitBloqueB(self, pB):
                self.bytes_pal = int(self.bits_palabra/8)
                self.palabras_bloque = pB // self.bytes_pal  # B/bloque // 
                self.bitsBloque = self.bits_direccion - int(math.log(pB,2))  
                
        def InitBloque(self, pB):
                self.palabras_bloque = pB # palabras/bloque
                self.bytes_pal = int(self.bits_palabra/8)
                bytes_bloque = self.bytes_pal * pB
                self.bitsBloque = self.bits_direccion - int(math.log(bytes_bloque,2))

        def BytesPal(self):
                return int(self.bits_palabra/8)

        def EsDirPalabra(self,direc):
                return (direc%self.bytes_pal==0)
        
        def InitFrecuencia(self,f):
                self.frecuencia = f
                
        def AnchoBanda(self):
                AB = self.frecuencia * self.bytes_pal
                return AB, ConvertirAPrefijos(AB)+"B/s"
        
        def CambioBitsPalabra(self,bitspalabra):
                self.bits_palabra = bitspalabra    # bits que tiene una palabra de datos
                bytes_pal = int(bitspalabra/8)
                bytes_bloque = bytes_pal * self.palabras_bloque
                self.bitsBloque = self.bits_direccion - int(math.log(bytes_bloque,2))
                
        def Direcciones(self):
                return self.dirMin.VerHexa(), self.dirMax.VerHexa()
        
        def BitsBloque(self):
                return self.bitsBloque
        def BitsDesplazamiento(self):
                return self.bits_direccion - self.bitsBloque
        def BytesComprendidos(self,d1,valor = False):

                bytes_pal = int(self.bits_palabra/8)

                #  4/3/2019  Compruebo que sea correcta
                
                d = Convertir(d1) # Porque puede llegar en hexa o decimal

                valor = d % bytes_pal
                if valor != 0:
                        return False, 0,0
                # Si se continua la dirección de palabra es correcta
                
                primerbyte = d    # el primer byte es el mismo

                if (valor == True):  # Cambiado 19.2.2019                          
                        if primerbyte < self.dirMax.Ver():
                                primerbyte_h = AHexa(primerbyte, self.bits_direccion)
                                ultimobyte = d+bytes_pal-1
                                ultimobyte_h = AHexa(ultimobyte,self.bits_direccion)
                                return True, primerbyte, ultimobyte, primerbyte_h, ultimobyte_h
                        else:  # Esta direccion no pertenece a esta memoria
                                return False, 0,0,0,0
                else:  # desde 19.2.2019 retorna solo estos valores.
                        if primerbyte < self.dirMax.Ver():
                                ultimobyte = d+bytes_pal-1
                                return True, primerbyte, ultimobyte
                        else:  # Esta direccion no pertenece a esta memoria
                                return False, 0,0  

        def Bytes_Comprendidos(self,direccion ):  
                ok, primer, ultimo = self.BytesComprendidos(direccion)
                if ok:
                        l = len(direccion)
                        if l>2:
                                if (direccion[0]=="0" and direccion[1]=="x"):  
                                        # Se trata de dirección en Hexadecimal
                                        primerH = AHexa(primer, self.bits_direccion)
                                        ultimoH = AHexa(ultimo, self.bits_direccion)
                                        return ok, "0x"+primerH, "0x"+ultimoH
                                else: # Asumo que llegaba en decimal
                                        return ok, primer, ultimo
                        else:   return ok, str(primer), str(ultimo)
                else:
                         return ok, str(primer), str(ultimo)

        def EstaDireccion(self,d1, valor = False): # Modificda 22/2/2019
                d = Convertir(d1) # Porque puede llegar en hexa o decimal
                if d < self.dirMax.Ver():
                        bytes_pal = self.bits_palabra/8
                        bytes_bloque = bytes_pal * self.palabras_bloque
                        blq = int(d // bytes_bloque)
                        desp = int(d % bytes_bloque)
                        if (valor == True):
                                blq_h = TraduceAHexa(blq, math.ceil(self.bitsBloque/4))
                                return True, blq,desp,blq_h
                        else:   return True, blq,desp
                else:  # Esta direccion no pertenece a esta memoria
                        if (valor == True):  return False, 0,0,"0"
                        else: return False, 0,0
                        
        def Rango(self, bloque):
                bytes_pal = int(self.bits_palabra/8)
                bytes_bloque = bytes_pal * self.palabras_bloque
                dI = bloque * bytes_bloque
                dF = dI + bytes_bloque -1
                return dI, dF, TraduceAHexa(dI,math.ceil(self.bits_direccion/4)), TraduceAHexa(dF,math.ceil(self.bits_direccion/4))

        def RangoBloque(self, bloque):  # Creada por compatibilidad dia 22/2/2019
                # bloque es una cadena de caracteres con un decimal o un hexa "0x..."
                valor = Convertir(bloque)
                di, df, diH,dfH = self.Rango(valor)
                return di, df

        def PrimerByte(self, bloque):
                bytes_pal = int(self.bits_palabra/8)
                bytes_bloque = bytes_pal * self.palabras_bloque
                dI = bloque * bytes_bloque
                return dI
        def BytesPorBloque(self):
                bytes_pal = int(self.bits_palabra/8)
                return bytes_pal * self.palabras_bloque
        def Campos(self):
                return self.bitsBloque,self.bits_direccion - self.bitsBloque 
        def NumeroBytes(self, valor= False):
                b = 2**self.bits_direccion # Bytes totales
                
                # Cambiado dia 19/2/2019
                if (valor == True):
                        return b, ConvertirAPrefijosI(b)+" B" 
                else:
                        return b
        def Numero_Bytes(self):
                b= self.NumeroBytes()
                bh = ConvertirAPrefijosI(b)
                return bh

        def NumeroPalabras(self, valor = False):
                b = 2**(self.bits_direccion+3)  # bits totales
                b = int(b / self.bits_palabra)  # palabras totales

                # Cambiado dia 19/2/2019
                #    para que solo retorne palabras
                if (valor == True):
                        bp = ConvertirAPrefijosI(b)
                        return b, bp+" x " + str(self.bits_palabra)
                        
                return b
        def Numero_Palabras(self):
                b= self.NumeroPalabras()
                bh = ConvertirAPrefijosI(b)
                return bh

        def CuantosBloques(self, valor = False):
                b = int(2**(self.bits_direccion+3))  # bits totales
                b = int(b / self.bits_palabra)       # palabras totales
                b = int(b / (self.palabras_bloque))  # bloques totales

                # Cambiada el 22/2/2019, para que solo retorne en decimal un valor
                if (valor == False): return b
                else: # Entonces además convierte a prefijos
                        bp = ConvertirAPrefijosI(b)
                        return b, bp+" bloques"

        def Presentacion(self):
                print("MEMORIA DEFINIDA:")
                tupla = self.NumeroPalabras(True)
                print("Tamaño " + tupla[1]) # Indica palabras x bits/palabra
                print("Direcciones: " + self.dirMin.VerHexa() + " a " + self.dirMax.VerHexa())
                bB= self.BytesPorBloque()
                print("Bloque: " + str(bB)+ " Bytes/bloque "+str(BytesAPal(bB,self.bits_palabra)) + " palabras/bloque")
                #print("Tiene " + str(self.bitsBloque) + " bits campo bloque y " +str(self.bits_direccion - self.bitsBloque)+" bits desplazamiento")
                print("   ")
                print("   ")
#.............................................................................................
#    Clase :  Bloque
#        
#.............................................................................................

class Bloque():
        valido = False
        etiqueta = 0
        contador = 0  # solo válido para LRU
        marcado = False  # Para politica de escritura: Back
        def Existe(self,eti):
                if (self.valido) and (self.etiqueta == eti):
                        c= self.contador
                        self.contador = 0
                        return True,c
                else:
                        return False,0
        def QueEtiqueta(self):
                if (self.valido):
                        return True,self.etiqueta
                else:
                        return False,0                
        def Inserta(self,eti,marcado = False,contador = 0):
                # Solo con politica de escritura BACK
                # es útil el marcar un bloque
                self.valido = True
                self.etiqueta = int(eti)
                self.contador = contador
                self.marcado = marcado
        def Marcar(self):
                self.marcado = True
        def VerMarca(self):
                if self.valido:
                        return self.marcado
                else:
                        return False
        def Envejece(self,c):
                if (self.contador < c) and self.valido:
                        self.contador += 1
        def Incrementa(self):
                if self.valido:
                        self.contador +=1
#.............................................................................................
#    Clase :  Conjunto
#.............................................................................................
        
class Conjunto():
        elementos = 0
        Siguiente = 0
        
        def __init__(self, vias):
                self.vias = vias
                self.datos = list()
                for i in range(vias):
                        b = Bloque()
                        self.datos.insert(i,b)
                        
        def Existe(self, eti,algoritmo):
                encontrado = False
                linea = 0
                for i in range(0,self.vias):
                        ok, c = self.datos[i].Existe(eti)
                        if ok:
                                encontrado = True
                                linea = i
                                break
                if ok and algoritmo== LRU: # LRU
                        for i in range (0,self.vias):
                                if i != linea:
                                        self.datos[i].Envejece(c)
                         # Tengo que buscar el que tiene contador mayor
                        for i in range(0,self.vias):
                                if self.datos[i].contador == (self.vias-1):
                                        self.Siguiente = i
                                        break       
                return encontrado,linea
        def QueEtiqueta(self,i):
                return self.datos[i].QueEtiqueta()
        
        def ExisteEtiqueta(self,i,eti):
                ok, valor = self.datos[i].Existe(eti)
                return ok
        def BloquesMarcados(self):
                cont = 0
                for i in range(self.vias):
                        if self.datos[i].VerMarca():
                                cont += 1
                return cont
        def Marcar(self,i):
                # Este solo sirve para politica
                # de escritura BACK. Marca el bloque i
                self.datos[i].Marcar()
        def Inserta(self,i,eti,marcado = False,contador = 0):
                self.elementos +=1
                self.Siguiente = i+ 1
                self.Siguiente = self.Siguiente % self.vias
                if self.datos[i].valido:
                        marca = self.datos[i].VerMarca()
                        self.datos[i].Inserta(eti,marcado,contador)
                        return True,marca
                else:   # Inserto por primera vez
                        self.datos[i].Inserta(eti,marcado,contador)
                        return False, False
        
        def InsertaFifo(self, eti,marcado = False):
                # Si se inserta un bloque desde lectura,
                #  No se proporciona el parámetro marcado
                lugar = self.Siguiente
                ok = False
                marca = self.datos[self.Siguiente].VerMarca()
                self.datos[self.Siguiente].Inserta(eti,marcado)
                self.Siguiente += 1
                self.Siguiente = self.Siguiente % self.vias
                self.elementos +=1
                if self.elementos > self.vias:
                        ok = True # Ya hay reemplazo
                return ok,lugar,marca       
        def InsertaLRU(self, eti,marcado = False):
                # Si se inserta un bloque desde lectura,
                #  No se proporciona el parámetro marcado
                self.elementos += 1
                lugar = self.Siguiente
                marca = self.datos[self.Siguiente].VerMarca()
                self.datos[self.Siguiente].Inserta(eti,marcado) # Su contador es cero
                # Incremento contadores de todos, menos actual
                for i in range(0, self.vias):
                        if i != self.Siguiente:
                                self.datos[i].Incrementa()
                if self.elementos >= self.vias:  # Cuando ya esta lleno el conjunto
                        # Tengo que buscar el que tiene contador mayor
                        for i in range(0,self.vias):
                                if self.datos[i].contador == (self.vias-1):
                                        self.Siguiente = i
                                        break
                else:  # Mientras no está lleno, es como un FIFO
                        self.Siguiente+= 1
                        self.Siguiente = self.Siguiente % self.vias
                ok = (self.elementos > self.vias)
                return ok,lugar,marca
        def Reemplazos(self):
                return self.reemplazos
        def Imprime(self):
                cad = ""
                if (self.vias <= 4):
                        for i in range(0,self.vias):
                                cad = cad + str(self.datos[i].etiqueta) + "("+str( self.datos[i].contador)+"):"
                        print(cad)
                else:
                        for i in range(0,self.vias):
                                cad = "l" +str(i)+": "+str(self.datos[i].etiqueta) + "("+str( self.datos[i].contador)+")"
                                print(cad)                       
        def ImprimeH(self,bits):
                cad = ""
                if (self.vias <=4):
                        for i in range(0,self.vias):
                                dir_h = AHexa(self.datos[i].etiqueta,bits)
                                cad = cad + "0x"+dir_h + "("+str( self.datos[i].contador)+"):"
                        print(cad)
                else:
                        for i in range(0,self.vias):
                                cad = "l"+str(i)+": "
                                dir_h = AHexa(self.datos[i].etiqueta,bits)
                                cad = cad + "0x"+dir_h + "("+str( self.datos[i].contador)+"):"
                                print(cad)
        def ImprimeV(self,lista):
                cad = ""
                for i in range(0,self.vias):
                        cad = "l"+str(i)+": "
                        cad = cad + lista[i]
                        print(cad)
              
#.............................................................................................
#    Clase :  Cache Totalmente Asociativa
#.............................................................................................

class CacheTotal():
        # Algoritmo de reemplazo FIFO por defecto
        Aciertos = 0
        Referencias = 0
        bytesporbloque = 0
        lineas = 0
        bytestotales = 0
        bitspalabra = 0
        escriturasenMP=0
        palabrasbloque = 0
        reemplazos = 0
        politica_escritura = 0 # Write Allocate (1 es Write Not Allocate)
        
        def __init__(self, bytes_totales, bytesporbloque,bitspalabra = 16,algoritmo = "FIFO",politica="Allocate", escritura="directa"):
                # Modificado 30/11/2019 para simplificar
                bytestotales = ABytes(bytes_totales)
                self.bytestotales = bytestotales
                self.lineas = int(bytestotales / bytesporbloque)
                self.datos = Conjunto(self.lineas)
                self.bytesporbloque = bytesporbloque
                self.bitspalabra = bitspalabra
                self.palabrasbloque = bytesporbloque/(bitspalabra/8)                
                pol = TipoPolitica(politica)
                esc = TipoEscritura(escritura)
                self.politica_escritura = [pol, esc]
                self.algoritmo = TipoAlgoritmo(algoritmo)
                self.reemplazos = 0
                
        def CambioBitsPalabra(self,bitspalabra):
                bytespalabra = (bitspalabra/8)
                self.bytesporbloque = self.palabrasbloque * bytespalabra
                self.lineas = int(self.bytestotales / self.bytesporbloque)
                self.datos = Conjunto(self.lineas)
                self.bitspalabra = bitspalabra
                # Borrado del resto de variables
                self.Aciertos = 0
                self.Referencias = 0
                self.escriturasenMP = 0
                self.reemplazos = 0
                
        def CambioBloque(self,palabrasbloque):
                self.palabrasbloque = palabrasbloque
                self.bytesporbloque = int(palabrasbloque * self.bitspalabra/8)
                lineas = int(self.bytestotales / self.bytesporbloque)
                if lineas != self.lineas:
                        self.lineas = lineas
                        self.datos = Conjunto(self.lineas)
                
        def BloquesMarcados(self):
                return self.datos.BloquesMarcados()
                
        def Redefine(self,bytestotales, bytesporbloque,bitspalabra=16,algoritmo ="FIFO",politica="Allocate",escritura="directa"):
                self.bytestotales = bytestotales
                self.lineas = int(bytestotales / bytesporbloque)
                self.datos = Conjunto(self.lineas)
                self.bitspalabra = bitspalabra
                self.bytesporbloque = bytesporbloque
                self.palabrasbloque = bytesporbloque/(bitspalabra/8)
                pol = TipoPolitica(politica)
                esc = TipoEscritura(escritura)
                self.politica_escritura = [pol, esc]
                self.algoritmo = TipoAlgoritmo(algoritmo)
                # Borrado del resto de variables
                self.Aciertos = 0
                self.Referencias = 0
                self.escriturasenMP = 0
                self.reemplazos = 0

        def QueBloque(self,linea):
                ok, etiqueta = self.datos.QueEtiqueta(linea)
                if ok:  # Es un bloque válido
                        bloque = (etiqueta * self.lineas)+linea
                        return ok, bloque
                else:
                        return False, 0
        def EsteBloque(self,bloque):
                eti = bloque // self.lineas
                lin = bloque % self.lineas
                return eti,lin
        
        def Escritura(self,direc): #Escritura de una direccion
                self.Referencias+= 1
                eti = direc // self.bytesporbloque
                ok, linea =self.datos.Existe(eti, self.algoritmo)
                
                if ok:  # Si es un acierto
                        self.Aciertos += 1
                        if self.politica_escritura[1] == POSTERIOR: #Back
                                #Hay que marcar el bloque
                                self.datos.Marcar(linea)
                        else:  # Escritura Directa
                                self.escriturasenMP +=1
                        return True,linea
                else:   # Si es un fallo
                        if self.politica_escritura[0] == ALLOCATE: # Write Allocate
                                
                                if self.politica_escritura[1] == POSTERIOR: # Back
                                        if self.algoritmo == FIFO:  # FIFO
                                                ok, linea,marca =self.datos.InsertaFifo(eti,True)
                                        else:  # LRU
                                                ok, linea,marca =self.datos.InsertaLRU(eti,True)
                                        if ok:  # Si se ha reemplazado por otro
                                                self.reemplazos +=1
                                                if marca:  # Si se ha reemplazado por un bloque escrito
                                                        self.escriturasenMP += self.palabrasbloque
                                else:  #  DIRECTA
                                        if self.algoritmo == FIFO:  # FIFO
                                                ok, linea, marca = self.datos.InsertaFifo(eti)
                                        else:  # LRU
                                                ok, linea, marca = self.datos.InsertaLRU(eti)
                                        self.escriturasenMP +=1
                                        if ok:  # Se ha reemplazado por otro
                                                self.reemplazos +=1
                        else:  # NOt- Allocate                      
                                self.escriturasenMP +=1
                        return False, linea
                                        
                        
        def Lectura(self, direc): # Lectura de una direccion
                self.Referencias+= 1
                eti = direc // self.bytesporbloque
                ok, linea =self.datos.Existe(eti, self.algoritmo)
                if ok:
                        self.Aciertos += 1
                        return True,linea
                else:
                        if self.algoritmo == FIFO:  # FIFO
                                ok, linea, marca = self.datos.InsertaFifo(eti)
                        else:  # LRU
                                ok, linea,marca = self.datos.InsertaLRU(eti)
                        if ok:
                                self.reemplazos += 1
                                if marca:
                                        # Si se ha reemplazado un bloque escrito
                                        self.escriturasenMP += self.palabrasbloque
                        return False, linea

        def Inserta(self, linea,eti,marcado,contador = 0): # Inserta un valor forzado
                # No actualiza la variable reemplazos, ni escrituras en MP
                #  pero si las referencias
                #self.Referencias+= 1  # No las cuento porque asumo que es un estado de llegada
                etiqueta = Convertir(eti) # Porque puede llegar en hexa o decimal
                self.datos.Inserta(linea,etiqueta, marcado,contador)
                
        def TasaH(self):
                return round(self.Aciertos/self.Referencias,4)
        def Imprime(self):
                self.datos.Imprime()
        def ImprimeH(self,bitsdireccion):
                r = int(math.log(self.bytesporbloque,2))
                self.datos.ImprimeH(bitsdireccion-r)
        def ImprimeV(self, v,bitsdireccion,tipo="decimal"):
                if tipo =="decimal":
                        decimal =True
                else:
                        decimal =False
                numbloques, primerbloque = v.NumBloques(self.bytesporbloque)
                r = int(math.log(self.bytesporbloque,2))
                r = bitsdireccion -r                                 
                lista = list()
                for i in range(self.lineas):
                        l=""
                        lista.insert(i,l)
                print("MC       Bloques MP")
                bloque = primerbloque
                linea = 0
                for i in range(numbloques):
                        lin = linea % self.lineas
                        if decimal:
                                lista[lin]+= "   bl. "+str(bloque)
                        else:
                                lista[lin]+= "   bl. 0x"+AHexa(bloque,bitsdireccion)
                        bloque += 1
                        linea +=1
                self.datos.ImprimeV(lista)                
        def Campos(self, bitsdireccion):
                r = int(math.log(self.bytesporbloque,2))
                return bitsdireccion-r, r
        def BloquesTotales(self):
                return self.lineas
        def Politica(self,tipo):
                pol = ""
                if tipo == 0:
                        if self.politica_escritura[0] == ALLOCATE:
                                pol += "Allocate"
                        else:
                                pol += "Not Allocate"
                else:
                        if self.politica_escritura[1] == DIRECTA:
                                return pol + " y Directa(Write Through)"
                        else:
                                return pol+ " y Posterior (Write back)"
        def PoliticaEscritura(self):
                pol = ""
                if self.politica_escritura[0] == ALLOCATE:
                        pol += "Allocate"
                else:
                        pol += "Not Allocate"
                if self.politica_escritura[1] == DIRECTA:
                        return pol + " y Directa(Write Through)"
                else:
                        return pol+ " y Posterior (Write back)"
        def AlgoritmoReemplazo(self):
                if self.algoritmo == 0:
                        return "FIFO"
                elif self.algoritmo == 1:
                        return "LRU"
                else:  # Aleatorio
                        return "Aleatorio"          
        def Presentacion(self):
                print("MEMORIA CACHE Totalmente Asociativa")
                megas = 1048576
                gigas = 1073741824
                kas = 1024
                if (self.bytestotales >= gigas):
                        cadena = str(int(self.bytestotales/gigas))+" GB"
                elif (self.bytestotales >= megas):
                        cadena = str(int(self.bytestotales/megas))+" MB"
                elif (self.bytestotales >= kas):
                        cadena = str(int(self.bytestotales/kas))+" KB"
                else:
                        cadena =  str(self.bytestotales)+" B"
                print("Cache de " + cadena+ " y " + str(self.bytesporbloque)+" B/bloque ")
                print("Tiene " + str(self.lineas) +" lineas")
                print("Algoritmo reemplazo: "+self.AlgoritmoReemplazo())
                print("Politicas escritura: "+self.PoliticaEscritura())

#.............................................................................................
#    Clase :  Cache  
#.............................................................................................
class Cache():
        def __init__(self,bytes_totales,bitspalabra, bytesporbloque):
                self.c = CacheTotal(bytes_totales, bytesporbloque,bitspalabra)
        def Presentacion(self):
                self.c.Presentacion()
        def Lectura(self,direc):
                return self.c.Lectura(direc)
        def Escritura(self,direc):
                return self.c.Escritura(direc)
        def TasaH(self):
                return self.c.TasaH()
        def Referencias(self):
                return self.c.Referencias
        def Aciertos(self):
                return self.c.Aciertos
#.............................................................................................
#    Clase :  Cache Asociativa
#.............................................................................................

class CacheAsociativa():
        # Algoritmo de reemplazo FIFO por defecto
        Aciertos = 0
        Referencias = 0
        bytesporbloque = 0
        lineas = 0
        conjuntos = 0
        vias = 0
        bytestotales = 0
        bitspalabra = 0
        escriturasenMP=0
        palabrasbloque = 0
        reemplazos = 0
        politica_escritura = 0 # Write Allocate (1 es Write Not Allocate)
        
        def __init__(self, bytestotales, bytesporbloque,vias, bitspalabra = 16,algoritmo = "FIFO",politica="Allocate", escritura="directa"):
                self.bytestotales = bytestotales
                self.lineas = int(bytestotales / bytesporbloque)
                self.vias = vias
                self.conjuntos = int(self.lineas/vias)
                
                # Ahora tenemos una lista de conjuntos
                self.datos = list()
                for i in range(self.conjuntos):
                        c = Conjunto(self.vias)
                        self.datos.insert(i,c)
                        
                self.bytesporbloque = bytesporbloque
                self.bitspalabra = bitspalabra
                self.palabrasbloque = int(bytesporbloque/(bitspalabra/8) )               
                pol = TipoPolitica(politica)
                esc = TipoEscritura(escritura)
                self.politica_escritura = [pol, esc]
                self.algoritmo = TipoAlgoritmo(algoritmo)
                self.reemplazos = 0

        def Redefine(self, bytestotales, bytesporbloque,vias, bitspalabra = 16,algoritmo = "FIFO",politica="Allocate", escritura="directa"):                       
                self.bytestotales = bytestotales
                self.lineas = int(bytestotales / bytesporbloque)
                self.vias = vias
                self.conjuntos = int(self.lineas/vias)
                # Ahora tenemos una lista de conjuntos
                self.datos = list()
                for i in range(self.conjuntos):
                        c = Conjunto(self.vias)
                        self.datos.insert(i,c)
                        
                self.bytesporbloque = bytesporbloque
                self.palabrasbloque = int(8* bytesporbloque/bitspalabra)                
                pol = TipoPolitica(politica)
                esc = TipoEscritura(escritura)
                self.politica_escritura = [pol, esc]
                self.algoritmo = TipoAlgoritmo(algoritmo)               
                self.bitspalabra = bitspalabra
                # Borrado del resto de variables
                self.Aciertos = 0
                self.Referencias = 0
                self.escriturasenMP = 0
                self.reemplazos = 0

        def CambioBitsPalabra(self,bitspalabra):
                bytespalabra = (bitspalabra/8)
                self.bytesporbloque = self.palabrasbloque * bytespalabra
                self.lineas = int(self.bytestotales / self.bytesporbloque)
                self.datos = Conjunto(self.lineas)
                self.bitspalabra = bitspalabra
                # Borrado del resto de variables
                self.Aciertos = 0
                self.Referencias = 0
                self.escriturasenMP = 0
                self.reemplazos = 0
                
        def CambioBloque(self,palabrasbloque):
                self.palabrasbloque = palabrasbloque
                self.bytesporbloque = int(palabrasbloque * self.bitspalabra/8)
                lineas = int(self.bytestotales / self.bytesporbloque)
                if lineas != self.lineas:
                        self.lineas = lineas
                        self.datos = Conjunto(self.lineas)
                        
        def QueBloque(self,conjunto, via):
                ok, etiqueta = self.datos[conjunto].QueEtiqueta(via)
                if ok:  # Es un bloque válido
                        bloque = (etiqueta * self.conjuntos)+conjunto
                        return ok, bloque
                else:
                        return False, 0
        def EsteBloque(self,bloque):
                eti = bloque // self.conjuntos
                conjunto = bloque % self.conjuntos
                return eti,conjunto                
        def BloquesMarcados(self):
                c = 0
                for i in range(self.conjuntos):
                        c += self.datos[i].BloquesMarcados()
                return c        

        def Politica(self,tipo):
                pol = ""
                if tipo == 0:
                        if self.politica_escritura[0] == ALLOCATE:
                                pol += "Allocate"
                        else:
                                pol += "Not Allocate"
                else:
                        if self.politica_escritura[1] == DIRECTA:
                                return pol + " y Directa(Write Through)"
                        else:
                                return pol+ " y Posterior (Write back)"
        def PoliticaEscritura(self):
                pol = ""
                if self.politica_escritura[0] == ALLOCATE:
                        pol += "Allocate"
                else:
                        pol += "Not Allocate"
                if self.politica_escritura[1] == DIRECTA:
                        return pol + " y Directa(Write Through)"
                else:
                        return pol+ " y Posterior (Write back)"
        def AlgoritmoReemplazo(self):
                if self.algoritmo == 0:
                        return "FIFO"
                elif self.algoritmo == 1:
                        return "LRU"
                else:  # Aleatorio
                        return "Aleatorio"
                
        def Inserta(self, conjunto,via,eti,marcado,contador = 0): # Inserta un valor forzado
                # No actualiza la variable reemplazos, ni escrituras en MP
                #  pero si las referencias
               # self.Referencias+= 1
                etiqueta = Convertir(eti) # Porque puede llegar en hexa o decimal
                self.datos[conjunto].Inserta(via,etiqueta, marcado,contador)

                
        def Lectura(self, direc): # Lectura de una direccion
                self.Referencias+= 1
                bloque = direc // self.bytesporbloque
                eti = bloque // self.conjuntos
                conjunto = bloque % self.conjuntos
                ok, via =self.datos[conjunto].Existe(eti,self.algoritmo)
                if ok:
                        self.Aciertos += 1
                        return True,conjunto,via
                else:
                        if self.algoritmo == 0:  # FIFO
                                ok,via,marca = self.datos[conjunto].InsertaFifo(eti)
                        else:  # LRU
                                ok,via,marca = self.datos[conjunto].InsertaLRU(eti)

                        if ok:
                                self.reemplazos +=1
                                if marca:  # Si el bloque reemplazado estaba marcado
                                        self.escriturasenMP += self.palabrasbloque
                        return False, conjunto, via

                
        def Escritura(self,direc): #Escritura de una direccion
                self.Referencias+= 1
                bloque = direc // self.bytesporbloque
                eti = bloque // self.conjuntos
                conjunto = bloque % self.conjuntos
                ok, via =self.datos[conjunto].Existe(eti,self.algoritmo)
                
                if ok:  # Si es un acierto
                        self.Aciertos += 1
                        if self.politica_escritura[1] == POSTERIOR: #Back
                                #Hay que marcar el bloque
                                self.datos[conjunto].Marcar(via)
                        else:  # Escritura Directa
                                self.escriturasenMP +=1
                        return True,conjunto, via
                else:   # Si es un fallo
                        if self.politica_escritura[0] == ALLOCATE: # Write Allocate
                                
                                if self.politica_escritura[1] == POSTERIOR: # Back
                                        if self.algoritmo == FIFO:  # FIFO
                                                ok, via,marca =self.datos[conjunto].InsertaFifo(eti,True)
                                        else:  # LRU
                                                ok, via,marca =self.datos[conjunto].InsertaLRU(eti,True)
                                        if ok:  # Si se ha reemplazado por otro
                                                self.reemplazos +=1
                                                if marca:  # Si se ha reemplazado por un bloque escrito
                                                        self.escriturasenMP += self.palabrasbloque
                                else:  #  DIRECTA
                                        if self.algoritmo == FIFO:  # FIFO
                                                ok, via, marca = self.datos[conjunto].InsertaFifo(eti)
                                        else:  # LRU
                                                ok, via, marca = self.datos[conjunto].InsertaLRU(eti)
                                        self.escriturasenMP +=1
                                        if ok:  # Se ha reemplazado por otro
                                                self.reemplazos +=1
                        else:  # NOt- Allocate                      
                                self.escriturasenMP +=1
                        return False, conjunto, via             

        def TasaH(self):
                return round(self.Aciertos/self.Referencias,4)
        
        def Imprime(self):
                for i in range (self.conjuntos):
                        print("C"+str(i)+":")
                        self.datos[i].Imprime()

        def ImprimeH(self,bitsdireccion):
                r = int(math.log(self.bytesporbloque,2))
                r = bitsdireccion -r
                for i in range (self.conjuntos):
                        print("Conjunto"+str(i)+": ")
                        self.datos[i].ImprimeH(r)
                        
        def ImprimeV(self, v,bitsdireccion,tipo ="decimal"):
                if tipo =="decimal":
                        decimal = True
                else:
                        decimal = False
                numbloques, primerbloque = v.NumBloques(self.bytesporbloque)
                r = int(math.log(self.bytesporbloque,2))
                r = bitsdireccion -r               
                lista = list()
                for i in range(self.conjuntos):
                        l=""
                        lista.insert(i,l)
                print("MC       Bloques MP")
                bloque = primerbloque
                for i in range(numbloques):
                        lin = bloque % self.conjuntos
                        if decimal:
                                lista[lin]+= "   bl. "+str(bloque)
                        else:
                                lista[lin]+= "   bl. 0x"+AHexa(bloque,r)
                        bloque += 1
                #  Una línea por conjunto
                for i in range(self.conjuntos):
                        print("C"+str(i)+lista[i])
                 
                
        def Campos(self, bitsdireccion):
                r1 = int(math.log(self.bytesporbloque,2))
                r2 = int(math.log(self.conjuntos,2))                
                return bitsdireccion-r2-r1,r2, r1
        def BloquesTotales(self):
                return int(self.bytestotales/self.bytesporbloque)
        def Presentacion(self):
                print("MEMORIA CACHE Asociativa por conjuntos")
                megas = 1048576
                gigas = 1073741824
                kas = 1024
                if (self.bytestotales >= gigas):
                        cadena = str(int(self.bytestotales/gigas))+" GB"
                elif (self.bytestotales >= megas):
                        cadena = str(int(self.bytestotales/megas))+" MB"
                elif (self.bytestotales >= kas):
                        cadena = str(int(self.bytestotales/kas))+" KB"
                else:
                        cadena =  str(self.bytestotales)+" B"
                print("Cache de " + cadena+ " y " + str(self.bytesporbloque)+" B/bloque ")
                print("Tiene " + str(self.lineas) +" lineas y "+str(self.conjuntos)+" conjuntos de " + str(self.vias)+" vias/cjto")
                print("Algoritmo reemplazo: "+self.AlgoritmoReemplazo())
                print("Politicas escritura: "+self.PoliticaEscritura())

#.............................................................................................
#    Clase :  Cache Directa
#
class CacheDirecta():
        Aciertos = 0
        Referencias = 0
        bytesporbloque = 0
        lineas = 0
        bytestotales = 0
        bitspalabra = 0
        escriturasenMP=0
        palabrasbloque = 0
        reemplazos = 0
        politica_escritura = 0 # Write Allocate (1 es Write Not Allocate)
        
        def __init__(self, bytestotales, bytesporbloque,bitspalabra = 16,algoritmo = "FIFO",politica="Allocate", escritura="directa"):
                self.bytestotales = bytestotales
                self.lineas = int(bytestotales / bytesporbloque)
                self.datos = Conjunto(self.lineas)
                self.bytesporbloque = bytesporbloque
                self.bitspalabra = bitspalabra
                self.palabrasbloque = bytesporbloque/(bitspalabra/8)                
                pol = TipoPolitica(politica)
                esc = TipoEscritura(escritura)
                self.politica_escritura = [pol, esc]
                self.algoritmo = TipoAlgoritmo(algoritmo)
                self.reemplazos = 0

        def Redefine(self, bytestotales, bytesporbloque,bitspalabra = 16,algoritmo = "FIFO",politica="Allocate", escritura="directa"):
                self.bytestotales = bytestotales
                self.lineas = int(bytestotales / bytesporbloque)
                self.datos = Conjunto(self.lineas)
                self.bitspalabra = bitspalabra
                self.bytesporbloque = bytesporbloque
                self.palabrasbloque = bytesporbloque/(bitspalabra/8)
                pol = TipoPolitica(politica)
                esc = TipoEscritura(escritura)
                self.politica_escritura = [pol, esc]
                self.algoritmo = TipoAlgoritmo(algoritmo)
                # Borrado del resto de variables
                self.Aciertos = 0
                self.Referencias = 0
                self.escriturasenMP = 0
                self.reemplazos = 0
        def CambioBitsPalabra(self,bitspalabra):
                bytespalabra = (bitspalabra/8)
                self.bytesporbloque = self.palabrasbloque * bytespalabra
                self.lineas = int(self.bytestotales / self.bytesporbloque)
                self.datos = Conjunto(self.lineas)
                self.bitspalabra = bitspalabra
                # Borrado del resto de variables
                self.Aciertos = 0
                self.Referencias = 0
                self.escriturasenMP = 0
                self.reemplazos = 0
        def CambioBloque(self,palabrasbloque):
                self.palabrasbloque = palabrasbloque
                self.bytesporbloque = int(palabrasbloque * self.bitspalabra/8)
                lineas = int(self.bytestotales / self.bytesporbloque)
                if lineas != self.lineas:
                        self.lineas = lineas
                        self.datos = Conjunto(self.lineas)

        def BloquesMarcados(self):
                return self.datos.BloquesMarcados()
        
        def QueBloque(self,linea):
                ok, etiqueta = self.datos.QueEtiqueta(linea)
                if ok:  # Es un bloque válido
                        bloque = (etiqueta * self.lineas) + linea
                        return ok, bloque
                else:
                        return False, 0
        def EsteBloque(self,bloque):
                eti = bloque // self.lineas
                lin = bloque % self.lineas
                return eti,lin
        def Direccion(self, direc):
                bloque = int(direc // self.bytesporbloque)
                eti = int(bloque // self.lineas)
                linea = int(bloque % self.lineas)
                return linea, eti
        
        def Inserta(self, linea,eti,marcado): # Inserta un valor forzado
                # No actualiza la variable reemplazos, ni escrituras en MP
                #  pero si las referencias
                #self.Referencias+= 1
                etiqueta = Convertir(eti) # Porque puede llegar en hexa o decimal
                self.datos.Inserta(linea,etiqueta, marcado)
                
        def Lectura(self, direc): # Lectura de una direccion
                self.Referencias+= 1
                bloque = int(direc // self.bytesporbloque)
                eti = int(bloque // self.lineas)
                linea = int(bloque % self.lineas)
                
                ok  = self.datos.ExisteEtiqueta(linea, eti)
                if ok:
                        self.Aciertos += 1
                        return True,linea
                else:
                        ok, marca = self.datos.Inserta(linea,eti)
                        if ok:
                                self.reemplazos += 1
                        if marca:
                                # Si se ha reemplazado un bloque escrito
                                self.escriturasenMP += self.palabrasbloque
                        return False, linea
        def Escritura(self,direc): #Escritura de una direccion
                self.Referencias+= 1
                bloque = int(direc // self.bytesporbloque)
                eti = int(bloque // self.lineas)
                linea = int(bloque % self.lineas)
                
                
                ok =self.datos.ExisteEtiqueta(linea,eti)
                
                if ok:  # Si es un acierto
                        self.Aciertos += 1
                        if self.politica_escritura[1] == POSTERIOR: #Back
                                #Hay que marcar el bloque
                                self.datos.Marcar(linea)
                        else:  # Escritura Directa
                                self.escriturasenMP +=1
                        return True,linea
                else:   # Si es un fallo
                        if self.politica_escritura[0] == ALLOCATE: # Write Allocate
                                if self.politica_escritura[1] == POSTERIOR: # Back
                                        ok, marca =self.datos.Inserta(linea,eti,True)
                                        if ok:  # Si se ha reemplazado por otro
                                                self.reemplazos +=1
                                                if marca:  # Si se ha reemplazado por un bloque escrito
                                                        self.escriturasenMP += self.palabrasbloque
                                else:  #  DIRECTA
                                        ok, marca = self.datos.Inserta(linea,eti)
                                        self.escriturasenMP +=1
                                        if ok:  # Se ha reemplazado por otro
                                                self.reemplazos +=1
                        else:  # NOt- Allocate                      
                                self.escriturasenMP +=1
                        return False, linea                
        def Politica(self,tipo):
                pol = ""
                if tipo == 0:
                        if self.politica_escritura[0] == ALLOCATE:
                                pol += "Allocate"
                        else:
                                pol += "Not Allocate"
                else:
                        if self.politica_escritura[1] == DIRECTA:
                                return pol + " y Directa(Write Through)"
                        else:
                                return pol+ " y Posterior (Write back)"                              
        def PoliticaEscritura(self):
                pol = ""
                if self.politica_escritura[0] == ALLOCATE:
                        pol += "Allocate"
                else:
                        pol += "Not Allocate"
                if self.politica_escritura[1] == DIRECTA:
                        return pol + " y Directa(Write Through)"
                else:
                        return pol+ " y Posterior (Write back)"
        def AlgoritmoReemplazo(self):
                if self.algoritmo == 0:
                        return "FIFO"
                elif self.algoritmo == 1:
                        return "LRU"
                else:  # Aleatorio
                        return "Aleatorio"                                
        def TasaH(self):
                return (self.Aciertos/self.Referencias,4)
                #return self.Aciertos/self.Referencias
        def Imprime(self):
                self.datos.Imprime()
        def ImprimeH(self,bitsdireccion):
                r = int(math.log(self.bytesporbloque,2))
                self.datos.ImprimeH(bitsdireccion-r)
        def ImprimeV(self, v,bitsdireccion,tipo="decimal"):
                if tipo == "decimal":
                        decimal = True
                else:
                        decimal = False
                numbloques, primerbloque = v.NumBloques(self.bytesporbloque)
                r = int(math.log(self.bytesporbloque,2))
                r = bitsdireccion -r                                
                lista = list()
                for i in range(self.lineas):
                        l=""
                        lista.insert(i,l)
                print("MC       Bloques MP")
                bloque = primerbloque
                for i in range(numbloques):
                        lin = bloque % self.lineas
                        if decimal:
                                lista[lin]+= "   bl."+str(bloque)
                        else:
                                lista[lin]+= "   bl. 0x"+AHexa(bloque,r)
                        bloque += 1
                self.datos.ImprimeV(lista)
                        
        def Campos(self, bitsdireccion):
                r1 = int(math.log(self.bytesporbloque,2))
                r2 = int(math.log(self.lineas,2))                
                return bitsdireccion-r2-r1,r2, r1
        def BloquesTotales(self):
                return self.lineas        
        def Presentacion(self):
                print("MEMORIA CACHE Directa")
                megas = 1048576
                gigas = 1073741824
                kas = 1024
                if (self.bytestotales >= gigas):
                        cadena = str(int(self.bytestotales/gigas))+" GB"
                elif (self.bytestotales >= megas):
                        cadena = str(int(self.bytestotales/megas))+" MB"
                elif (self.bytestotales >= kas):
                        cadena = str(int(self.bytestotales/kas))+" KB"
                else:
                        cadena =  str(self.bytestotales)+" B"
                print("Cache de " + cadena+ " y " + str(self.bytesporbloque)+" B/bloque ")
                print("Tiene " + str(self.lineas) +" lineas")
                print("Politicas escritura: "+self.PoliticaEscritura())               
