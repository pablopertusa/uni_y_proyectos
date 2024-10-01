
# -*- coding: utf-8 -*-
from secretaria import Secretaria
from interfaz import *
import os
import pickle

secretaria = Secretaria()

################################
# LEER Y GUARDAR BASE DE DATOS #
################################

def leer_datos():
    global secretaria
    filename = seleccionar_fichero('Nombre del fichero a leer',
                                   es_directorio=False,
                                   save_mode=False)
    try:
        with open(filename,'rb') as f:
            secretaria = pickle.load(f)
    except Exception as ex:
        return (False, 'Error al leer fichero. Excepcion de tipo '+
                f'{type(ex).__name__}\nArgumentos:{ex.args}. \n'+
                f'Directorio actual:{os.getcwd()}')
    notificar("Datos cargados", ok=True, titulo='Leer datos')

def guardar_datos():
    filename = seleccionar_fichero('Nombre del fichero a guardar',
                                     es_directorio=False,
                                     save_mode=True)
    try:
        with open(filename, 'wb') as f:
            pickle.dump(secretaria,f)
    except Exception as ex:
        return (False, 'Error al guardar fichero. Excepcion de tipo '+
                f'{type(ex).__name__}\nArgumentos:{ex.args}. \n'+
                f'Directorio actual:{os.getcwd()}')
    notificar("Datos guardados", ok=True, titulo='Guardar datos')

######################
# GESTIÓN ASIGNATURA #
######################

def alta_asignatura():
    nombre, creditos = pedir_campos(('Nombre', 'Creditos'),
                                    titulo='Alta asignatura')
    ok, msg = secretaria.alta_asignatura(nombre, float(creditos))
    notificar(msg, ok=ok, titulo='Alta asignatura')

def buscar_asignatura():
    nombre = pedir_campo('Nombre', titulo='Buscar asignatura')
    ok, msg = secretaria.buscar_asignatura(nombre)
    if not ok:
        notificar(msg, ok=ok, titulo='Puntuar alumno')
    else:
        listar(msg, titulo='Buscar asignatura')

def listar_asignaturas():
    listar(secretaria.listar_asignaturas(),
           titulo='Listado de asignaturas')

##################
# GESTIÓN GRUPOS #
##################

def alta_grupo():
    nom, asig, dia, ini, dur, aforo = pedir_campos(('Nombre grupo',
                                                    'Nombre asignatura',
                                                    'Día',
                                                    'Hora inicio (hh:mm)',
                                                    'Duración (en minutos)',
                                                    'Aforo máximo'),
                                                   titulo='Alta grupo')
    ok, msg = secretaria.alta_grupo(nom, asig, dia, ini, dur, aforo)
    notificar(msg, ok=ok, titulo='Alta grupo')

def listar_grupos():
    asignatura = pedir_campo('Asignatura', titulo='Listar grupos')
    ok, msg = secretaria.listar_grupos(asignatura)
    if not ok:
        notificar(msg, ok=ok, titulo='Listar grupos')
    else:
        listar(msg, titulo='Listar grupos')

###################
# GESTIÓN ALUMNOS #
###################

def alta_alumno():
    dni, nombre = pedir_campos(('DNI','Nombre'), titulo='Alta de alumno')
    ok, msg = secretaria.alta_alumno(dni,nombre)
    notificar(msg, ok=ok, titulo='Alta de alumno')

def baja_alumno():
    dni = pedir_campo('DNI', titulo='Baja de alumno')
    ok, msg = secretaria.baja_alumno(dni)
    notificar(msg, ok=ok, titulo='Baja de alumno')

def buscar_alumno_dni():
    dni = pedir_campo('DNI', titulo='Búsqueda de alumno por DNI')
    ok, msg = secretaria.buscar_alumno_dni(dni)
    if not ok:
        notificar(msg ,ok=False,
                  titulo='Buscar alumno por DNI')
    else:
        listar([msg], titulo='Alumno:')

def buscar_alumno_nombre():
    nombre = pedir_campo('Nombre',
                         titulo='Búsqueda de alumno por nombre',
                         permite_vacio=True)
    ok, msg = secretaria.buscar_alumno_nombre(nombre)
    if not ok:
        notificar(msg ,ok=False,
                  titulo='Buscar alumno por nombre')
    else:
        listar(msg, titulo='Alumno(s):')

def matricular_alumno():
    dni, grupo = pedir_campos(('DNI', 'Grupo'),
                              titulo='Matricular alumno')
    ok, msg = secretaria.matricular_alumno(dni, grupo)
    notificar(msg, ok=ok, titulo='Matricular alumno')

def puntuar_alumno():
    dni, asignatura, nota = pedir_campos(('DNI', 'Asignatura', 'Nota'),
                                         titulo='Puntuar alumno')
    ok, msg = secretaria.puntuar_alumno(dni, asignatura, float(nota))
    notificar(msg, ok=ok, titulo='Puntuar alumno')

######################
# PROGRAMA PRINCIPAL #
######################

def inicializa():
    # Alta asignaturas
    secretaria.alta_asignatura('FCO',5)
    secretaria.alta_asignatura('FPR',4.5)
    secretaria.alta_asignatura('PRG',6)
    secretaria.alta_asignatura('PROY1',4.5)
    secretaria.alta_asignatura('EST',4.5)

    # Alta grupos
    secretaria.alta_grupo('PRG-1A', 'PRG', 'Miércoles', '11:00', 60, 30)
    secretaria.alta_grupo('PRG-1B', 'PRG', 'Martes', '17:30', 60, 30)
    secretaria.alta_grupo('PROY1-1A', 'PROY1', 'Miércoles', '11:30', 60, 30)
    secretaria.alta_grupo('PROY1-1B', 'PROY1', 'Martes', '18:00', 60, 30)

    # Alta alumnos
    secretaria.alta_alumno('1069978R', 'Teodor Relinque Somoano')
    secretaria.alta_alumno('9179931A', 'Estiven Brana Juzgado')
    secretaria.alta_alumno('7139263O', 'Alia Ybarra Soñora')
    secretaria.alta_alumno('9857808D', 'Axel Villamarin Galavis')
    secretaria.alta_alumno('9237087Z', 'Alvaro Valdericeda Larraga')
    secretaria.alta_alumno('1585918L', 'Custodio Torollo Terry')
    secretaria.alta_alumno('9152667N', 'Judith Asensio Menarguez')
    secretaria.alta_alumno('6610540J', 'Maximiliana Castineira Urretavizcaya')
    secretaria.alta_alumno('4946853D', 'Bernhard Aviles Manivesa')
    secretaria.alta_alumno('9156161S', 'Saloua Raton Mazas')

    # Matricular alumnos
    secretaria.matricular_alumno('1069978R', 'PRG-1A')
    secretaria.matricular_alumno('9179931A', 'PRG-1A')
    secretaria.matricular_alumno('7139263O', 'PRG-1B')
    secretaria.matricular_alumno('9857808D', 'PRG-1B')
    secretaria.matricular_alumno('9237087Z', 'PROY1-1A')
    secretaria.matricular_alumno('1585918L', 'PROY1-1A')
    secretaria.matricular_alumno('9152667N', 'PROY1-1B')
    secretaria.matricular_alumno('6610540J', 'PROY1-1B')


def main_menu():
    while True:
        op = menu(('--- ARCHIVO ---',
                   ('Abrir', leer_datos),
                   ('Guardar', guardar_datos),
                   '--- ASIGNATURAS ---',
                   ('Alta', alta_asignatura),
                   ('Buscar', buscar_asignatura),
                   ('Listar', listar_asignaturas),
                   '--- GRUPOS ---',
                   ('Alta', alta_grupo),
                   ('Listar', listar_grupos),
                   '--- ALUMNOS ---',
                   ('Alta', alta_alumno),
                   ('Baja', baja_alumno),
                   ('Buscar por DNI', buscar_alumno_dni),
                   ('Buscar por nombre', buscar_alumno_nombre),
                   ('Matricular', matricular_alumno),
                   ('Poner nota', puntuar_alumno),
                   '-----------------------',
                   ('Salir del programa', None)))

        if op is None:
            return
        op()

if __name__ == '__main__':
    inicializa()
    main_menu()
