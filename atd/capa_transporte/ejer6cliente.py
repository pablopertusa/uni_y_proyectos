from socket import *

clientSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 12000
serverAdress = '192.168.10.10' #cambiar esto segun donde estes conectado

print('Conectando...')

clientSocket.connect((serverAdress, serverPort))

print('Conectado')

url = input('Introduce a qué url te quieres conectar: ')
clientSocket.send(url.encode())

print('...')

respuesta = ''
seguir = True
while seguir:
    leer = clientSocket.recv(2048).decode()
    respuesta = respuesta + leer
    if len(leer) == 0:
        seguir = False

print(respuesta)
