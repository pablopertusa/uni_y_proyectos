from socket import *
import re

serverName = '192.168.10.10'
serverPort = 12000
clientSocket = socket(AF_INET,SOCK_DGRAM)
clientSocket.bind(('', 12001))
mensaje = input('Mensaje para el servidor: ')

if re.findall(r'\Aescuchando', mensaje) == ['escuchando']:
    continuar = True #PARA FINALIZAR DE RECIBIR PRESIONAR ENTER
    while continuar:
        print('Esperando mensajes...')
        clientMessage, clientAdress = clientSocket.recvfrom(2048)
        print(clientMessage.decode())
        if clientMessage.decode() == '':
            continuar = False

else:
    clientSocket.sendto(mensaje.encode(), (serverName, serverPort))
    serverMessage, serverAdress = clientSocket.recvfrom(2048)
    recibido = serverMessage.decode()
    print(recibido)

    if re.findall(r'\A27', recibido) == ['27']:
        direccion = re.findall(r'\A27 (.+)', recibido)
        direccion = direccion[0].split(',')
        ip = ''
        for i in direccion[0]:
            if i.isdigit() or i == '.':
                ip += i
        puerto = ''
        for i in direccion[1]:
            if i.isdigit():
                puerto += i
        puerto = int(puerto)
        print(ip)
        print(puerto)

        continuar = True
        while continuar:
            enviar = input('Enviar: ')
            clientSocket.sendto(enviar.encode(), (ip, puerto))
            if enviar == '':
                continuar = False
    else:
        print(recibido)
    

clientSocket.close()