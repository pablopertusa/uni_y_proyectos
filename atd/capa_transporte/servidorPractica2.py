from socket import *
import re

serverPort = 12000
informacionClientes = []
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('servidor listo')
while True:
    mensajeBruto, adress = serverSocket.recvfrom(2048)
    mensaje = mensajeBruto.decode()
    if re.findall(r'R*r*egistro', mensaje) == ['Registro'] or re.findall(r'R*r*egistro', mensaje) == ['registro']:
        nombreCliente = re.findall(r'R*r*egistro,*\s*(\w+)', mensaje)
        ip, numeroPuerto = adress
        cliente = [nombreCliente, ip, numeroPuerto]
        if cliente not in informacionClientes:
            informacionClientes.append(cliente)
            serverSocket.sendto((str(len(informacionClientes))+' confirmado').encode(), adress)
            print(mensaje)
            print(informacionClientes)
            print(len(informacionClientes))
        else:
            serverSocket.sendto(('Cliente ya registrado').encode(), adress)
    elif re.findall(r'C*c*onsulta', mensaje) == ['Consulta'] or re.findall(r'C*c*onsulta', mensaje) == ['consulta']:
        nombreCliente = re.findall(r'C*c*onsulta,*\s*(\w+)', mensaje)
        esta = False
        for cliente in informacionClientes:
            if cliente[0] == nombreCliente:
                serverSocket.sendto(f'Ok, direccion de {nombreCliente[0]} es {cliente[1], cliente[2]}'.encode(), adress)
                esta = True
        if esta == False:
            serverSocket.sendto('El cliente que solicita no se encuentra'.encode(), adress)
    else:
        serverSocket.sendto('Introduzca una instruccion valida'.encode(), adress)
