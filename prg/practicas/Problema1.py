
import MemoriaPrincipal as mem


#.....................................Problema 1
#
#      Trabajando conceptos relativos a memoria: Capacidad y direcciones
#....................................................................

# Apartado (P4.2): definir una memoria y calcular Bytes y direcciones Min/Max
bitsPalabra = 16
bitsDireccion = 16
print(".......................")
print("   Apartado  P4.2\n")
print(" Memoria con "+str(bitsPalabra)+" bits/palabra y "+str(bitsDireccion)+" bits/direcciones")
m = mem.Memoria(bitsDireccion,bitsPalabra)

print("     (1) Capacidad en Bytes:" )
Bytes  = m.Numero_Bytes()


print("         Tiene " + Bytes + "Bytes\n")
print("     (2) Longitud de Palabra en bits: "+ str(bitsPalabra) +" bits\n") 

print("     (3) Dirección menor y mayor de un Byte:")
dirMin, dirMax =  m.Direcciones()
 
print("         Dirección menor: 0x" + dirMin)
print("         Dirección mayor: 0x" + dirMax)

# Apartado (P4.4): calcular capacidad expresada en palabras
print("     (4) Capacidad en Palabras:")
palabras = m.Numero_Palabras()
print("         Tiene " + palabras + "Palabras\n")

#Apartado (P4.7): calcular direccion de Bytes de una palabra
##??? RELLENAR POR EL ALUMNO

resp = input(" \nPulse retorno de carro (return) para FIN  ")


