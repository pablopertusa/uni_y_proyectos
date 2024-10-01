# -*- coding: utf-8 -*-
from grupo import Grupo

class Asignatura:
    def __init__(self, nombre, creditos):
        self.nombre = nombre
        self.creditos = creditos
        self.grupos = []
    def get_nombre(self):
        return self.nomnre
    def listar_grupos(self):
        l = []
        for grupo in self .grupos:
            l += [grupo.nombre]
        return l
    def anyadir_grupo(self,otro):
        if isinstance(otro,Grupo):
            self.grupos += [otro]
        else:
            return 'No es un objeto tipo grupo'
    def __repr__(self):
        return self.nombre + ' ' + str(self.creditos) + ' créditos'
    