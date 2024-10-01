from socket import *

serverName = 'LAPTOP-2U1CL578'
serverPort = 12000
clientSocket = socket(AF_INET,SOCK_DGRAM)
clientSocket.settimeout(3)
mensaje = input('Escribe algo: ')
clientSocket.sendto(mensaje.encode(), (serverName, serverPort))
try:
    serverMessage, serverAdress = clientSocket.recvfrom(2048)
    print(serverAdress, 'dice',serverMessage.decode())
except timeout:
    print('Ha ocurrido un problema, el servidor no responde')
clientSocket.close()
