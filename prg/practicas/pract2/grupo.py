class Grupo:
    def __init__(self,nombre, asignatura, horario, aforo):
        self.asignatura = asignatura
        self.nombre = nombre
        self.horario = horario
        self.aforo = int(aforo)
        self.matriculados = 0
    def get_nombre(self):
        return self.nombre
    def grupo_esta_completo(self):
        if self.matriculados >= self.aforo:
            return True
        else:
            return False
    def quitar_alumno(self):
        self.matriculados -= 1
    def anyadir_alumno(self):
        self.matriculados += 1
    def solapa(self,otro):
        dia_self = self.horario[0]
        dia_otro = otro.horario[0]
        if dia_self != dia_otro:
            return False
        hora_inicio_self = self.horario[1]
        hora_inicio_otro = otro.horario[1]
        minuto_inicio_self = self.horario[2]
        minuto_inicio_otro = otro.horario[2]
        duracion_self = self.horario[3]
        duracion_otro = otro.horario[3]
        ini1 = hora_inicio_self*60 + minuto_inicio_self
        ini2 = hora_inicio_otro*60 + minuto_inicio_otro
        fin1 = ini1 + duracion_self
        fin2 = ini2 + duracion_otro
        if not (fin1 <= ini2 or fin2 <= ini1):
            return True
        return False
    def __repr__(self):
        return f'GRUPO: {self.nombre} ({self.asignatura})'
