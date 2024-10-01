from socket import *
import re

serverName = 'LAPTOP-2U1CL578'
serverPort = 12000
clientSocket = socket(AF_INET,SOCK_DGRAM)
clientSocket.bind(('', 12001))
clientSocket.settimeout(3)
mensaje = input('Mensaje para el servidor: ')
clientSocket.sendto(mensaje.encode(), (serverName, serverPort))
try:
    serverMessage, serverAdress = clientSocket.recvfrom(2048)
    recibido = serverMessage.decode()
    print(recibido)
    if 'Adelante, ' in recibido:
        ip, puerto = re.findall(r'Adelante, (.+)', recibido)[0]
        

except timeout:
    print('Ha ocurrido un problema, el servidor no responde')
clientSocket.close()