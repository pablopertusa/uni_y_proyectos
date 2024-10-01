from socket import *
import time
# Leer el numero del teclado
number = input('Introduce mensaje de inicio :')
# Enviar el numero al servidor
serverName = 'LAPTOP-2U1CL578'
serverPort = 12000
clientSocket = socket( AF_INET , SOCK_DGRAM )
clientSocket.settimeout(1)
for i in range(10):
    clientSocket.sendto( number.encode() , ( serverName , serverPort ))
    tiempoInicial = time.time()
    try:
        # Recibir respuesta del servidor y cerrar socket
        modifiedNumber , serverAddress = clientSocket.recvfrom(2048)
        tiempoFinal = time.time()
        # Imprimir el numero recibido
        print( f'mensaje numero {i+1}: ',tiempoFinal - tiempoInicial)
    except timeout:
        print(f'ha ocurrido un problema de timeout en el mensaje {i+1}')


clientSocket.close()