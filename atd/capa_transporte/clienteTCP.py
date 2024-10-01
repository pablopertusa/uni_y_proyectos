from socket import *

serverName = '192.168.10.10'
serverPort = 12000
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.settimeout(3)
clientSocket.connect((serverName, serverPort))
mensaje = input('Mensaje para el servidor: ')
clientSocket.send(mensaje.encode())
try:
    serverMessage = clientSocket.recv(2048)
    print(serverMessage.decode())
    clientSocket.close()
except timeout:
    print('Ha ocurrido un problema, el servidor no responde')
