from socket import *
# Leer el n´umero del teclado
number = input('Introduce el n´umero :')
# Enviar el n´umero al servidor
serverName = 'LAPTOP-2U1CL578'
serverPort = 12000
clientSocket = socket( AF_INET , SOCK_DGRAM )
clientSocket.sendto( number.encode() , ( serverName , serverPort ))

# Recibir respuesta del servidor y cerrar socket
modifiedNumber , serverAddress = clientSocket.recvfrom (2048)
clientSocket.close()
# Imprimir el n´umero recibido
print( modifiedNumber.decode())