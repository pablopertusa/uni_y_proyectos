# -*- coding: utf-8 -*-
from alumno import Alumno
from asignatura import Asignatura
from grupo import Grupo

class Secretaria:
    def __init__(self):
        self.alumnos = {} # {dni:alumno}
        self.asignaturas = {} # {nombre_asignatura:asignatura}
        self.grupos = {} # {nombre_grupo:grupo}

    #############################################
    #           GESTIÓN ASIGNATURAS             #
    #############################################
    def alta_asignatura(self, nombre, creditos):
        self.asignaturas[nombre] = Asignatura(nombre,creditos)
        return True, 'todo perfecto' 

    def buscar_asignatura(self, nombre):
        nombre = str(nombre)
        l = []
        for asig in self.asignaturas:
            if nombre.lower() in asig.lower():
                l.append(asig)
        if len(l) == 0:
            return False, 'no existe ninguna asignatura con ese nombre'
        else:
            return True, l

    def listar_asignaturas(self):
        lista = list(self.asignaturas.keys())
        lista.sort()
        return lista

    #############################################
    #           GESTIÓN GRUPOS                  #
    #############################################
    def alta_grupo(self, nombre, nombre_asignatura, dia, inicio, duracion, aforo):
        dia = defineDia(dia)
        hm = inicio.split(':')
        hora_inicio = int(hm[0])
        minuto_inicio = int(hm[1])
        duracion = int(duracion)
        horario = [dia] + [hora_inicio] + [minuto_inicio] + [duracion]
        self.grupos[nombre] = Grupo(nombre,nombre_asignatura,horario,aforo)
        return True, 'todo perfecto'

    def listar_grupos(self, nombre_asignatura):
        lista = []
        for grupo in self.grupos:
            if self.grupos[grupo].asignatura.lower() == nombre_asignatura.lower():
                lista.append(grupo)
        if len(lista) == 0:
            return False, 'no existe una asignatura con ese nombre'
        else:
            return True, lista

    #############################################
    #           GESTIÓN ALUMNOS                 #
    #############################################
    def alta_alumno(self, dni, nombre):
        """
        Params:
          dni (str)
          nombre (str)
        """
        self.alumnos[dni] = Alumno(nombre, dni)
        return True, 'todo perfecto'

    def baja_alumno(self, dni):
        """
        Params:
          dni (str)
        """
        if dni not in self.alumnos:
            return False, 'ese alumno no existe'
        else:
            alumno = self.alumnos[dni]
        for asignatura in alumno.asig_matriculadas:
            grupo = alumno.asig_matriculadas[asignatura]
            grupo.quitar_alumno()
        del self.alumnos[dni]
        return True, 'todo perfecto'

    def buscar_alumno_dni(self, dni):
        """
        Params:
          dni (str)
        """
        if dni in self.alumnos:
            return True, f'{self.alumnos[dni]}'
        else:
            return False, 'no existe ese alumno'

    def buscar_alumno_nombre(self, nombre):
        """
        Params:
          nombre (str) fragmento del nombre
        """
        l = []
        for dni in self.alumnos:
            alumno = self.alumnos[dni]
            if nombre in alumno.nombre:
                l.append(alumno.nombre)
        if len(l)==0:
            return False, 'No hay alumnos con ese nombre'
        return True, l

    def matricular_alumno(self, dni, nombre_grupo):
        """
        Params:
          dni (str)
          nombre_grupo (str) nombre del grupo
        """
        if dni not in self.alumnos:
            return False, 'No exise ese alumno'
        if nombre_grupo not in self.grupos:
            return False, 'No existe ese grupo'
        alumno = self.alumnos[dni]
        grupo = self.grupos[nombre_grupo]
        alumno.matricular(grupo)
        return True, 'todo perfecto'

    def desmatricular_alumno(self, dni, nombre_grupo):
        """
        Params:
          dni (str)
          nombre_grupo (str) nombre del grupo
        """
        if dni not in self.alumnos:
            return False, 'No exise ese alumno'
        if nombre_grupo not in self.grupos:
            return False, 'No existe ese grupo'
        alumno = self.alumnos[dni]
        grupo = self.grupos[nombre_grupo]
        alumno.desmatricular(grupo.asignatura)
        return True, 'todo perfecto'

    def puntuar_alumno(self, dni, nombre_asignatura, nota):
        """
        Sirve para ponerle nota en una asignatura de la que está matriculado.
        Se le quita del grupo y pasa a ser una asignatura ya cursada.
        Params:
          dni (str)
          nombre_asignatura (str)
          nota (float)
        """
        if dni not in self.alumnos:
            return False, 'No exise ese alumno'
        if nombre_asignatura not in self.asignaturas:
            return False, 'No existe esa asignatura'
        alumno = self.alumnos[dni]
        alumno.puntuar(nombre_asignatura,nota)
        return True, 'Alumno puntuado'
    
def defineDia(dia):
    if dia.lower() == 'lunes':
        return 1
    elif dia.lower() == 'martes':
        return 2
    elif dia.lower() == 'miercoles' or dia.lower() == 'miércoles':
        return 3
    elif dia.lower() == 'jueves':
        return 4
    elif dia.lower() == 'viernes':
        return 5
