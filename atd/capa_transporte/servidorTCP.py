from socket import *
import re

serverPort = 12000
informacionClientes = []
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('servidor listo')
while True:
    connectionSocket, adress = serverSocket.accept()
    mensaje = connectionSocket.recv(2048).decode()
    if re.findall(r'R*r*egistro', mensaje) == ['Registro'] or re.findall(r'R*r*egistro', mensaje) == ['registro']:
        nombreCliente = re.findall(r'R*r*egistro,*\s*(\w+)', mensaje)
        ip, numeroPuerto = adress
        cliente = [nombreCliente, ip, numeroPuerto]
        if cliente not in informacionClientes:
            informacionClientes.append(cliente)
            connectionSocket.send((str(len(informacionClientes))+' confirmado').encode())
            print(mensaje)
            print(informacionClientes)
            print(len(informacionClientes))
        else:
            connectionSocket.send(('Cliente ya registrado').encode())
    elif re.findall(r'C*c*onsulta', mensaje) == ['Consulta'] or re.findall(r'C*c*onsulta', mensaje) == ['consulta']:
        nombreCliente = re.findall(r'C*c*onsulta,*\s*(\w+)', mensaje)
        esta = False
        for cliente in informacionClientes:
            if cliente[0] == nombreCliente:
                connectionSocket.send(f'Ok, direccion de {nombreCliente[0]} es {cliente[1], cliente[2]}'.encode())
                esta = True
        if esta == False:
            connectionSocket.send('El cliente que solicita no se encuentra'.encode())
    else:
        connectionSocket.send('Introduzca una instruccion valida'.encode())
    connectionSocket.close()