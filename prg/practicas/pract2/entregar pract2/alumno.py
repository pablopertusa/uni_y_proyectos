# -*- coding: utf-8 -*-
from grupo import Grupo

class Alumno(Grupo):
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = str(dni)
        self.asig_cursadas = {}
        self.asig_matriculadas = {}
    def matricular(self, grupo):
        ok = True
        if grupo.asignatura in self.asig_cursadas and self.asig_cursadas[grupo.asignatura] >= 5:
            ok = False
        ok2 = False
        if (grupo.asignatura not in self.asig_matriculadas) and isinstance(grupo, Grupo):
            ok2 = True
        ok3 = not(grupo.grupo_esta_completo())
        ok4 = True
        for asig in self.asig_matriculadas:
            grupo2 = self.asig_matriculadas[asig]
            if grupo.solapa(grupo2):
                ok4 = False
        if ok and ok2 and ok3 and ok4:
            self.asig_matriculadas[grupo.asignatura] = grupo
            print('Alumno añadido al grupo')
            Grupo.anyadir_alumno(grupo)
            return True
        return False
    def desmatricular(self, asignatura):
        if asignatura in self.asig_matriculadas:
            a = self.asig_matriculadas.pop(asignatura)
            print('Alumno eliminado de',a)
            return True
        else:
            print('no estaba')
            return False
    def puntuar(self,asignatura,nota):
        if asignatura in self.asig_matriculadas and (nota >= 0) and (nota <= 10):
            self.asig_cursadas[asignatura] = nota
            Grupo.quitar_alumno(self.asig_matriculadas[asignatura])
            self.desmatricular(asignatura)
            return True
        else:
            print('mira a ver lo que pones')
            return False
    def __repr__(self):
        return f'Alumno/a: {self.nombre}, DNI: {self.dni}, Asig. cursadas: {self.asig_cursadas}, Asig. matriculadas: {self.asig_matriculadas}'
        