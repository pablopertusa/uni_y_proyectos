from socket import *
import math

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('El servidor está listo para recibir')
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    try:
        modificado = str(math.factorial(int(message)))

    except:
        modificado = 'jefe tiene que ser un numero cabron'
    serverSocket.sendto(modificado.encode(), clientAddress)


