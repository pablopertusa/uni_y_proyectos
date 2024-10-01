from socket import *
import requests as r

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',12000))
serverSocket.listen(1)
print('Servidor proxy listo')
while True:
    connectionSocket, adress = serverSocket.accept()
    url = connectionSocket.recv(2048).decode()
    print(f'Mandando peticion a {url}')
    peticionHTTP = r.get(url)
    peticionHTTP = peticionHTTP.text
    print(f'Mandando respuesta a {adress}')
    connectionSocket.send(peticionHTTP.encode())
    connectionSocket.close()
    