from socket import *

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', 12000))
print('servidor listo')
while True:
    message, clientAdress = serverSocket.recvfrom(2048)
    print(f'Mensaje de {clientAdress}: {message.decode()}')
    try:
        modifiedMessage = message.decode().upper()
        serverSocket.sendto(modifiedMessage.encode(), clientAdress)
    except Exception as ex:
        print('Ha ocurrido un problema', ex)
    
