from Asignatura import Asignatura
from typing import Optional


class RepositorioAsignatura:
    def __init__(self):
        self.asignaturas = []

    def crear_asignatura(self, nombre, codigo, creditos) -> Asignatura:
        nueva_asignatura = Asignatura(nombre, codigo, creditos)
        self.asignaturas.append(nueva_asignatura)
        return nueva_asignatura

    def obtener_asignaturas(self):
        return self.asignaturas

    def obtener_asignatura(self, codigo) -> Optional[Asignatura]:
        for asignatura in self.asignaturas:
            if asignatura.codigo == codigo:
                return asignatura
        return None

    def modificar_asignatura(self, codigo, nombre=None, creditos=None) -> Asignatura:
        for asignatura in self.asignaturas:
            if asignatura.codigo == codigo:
                if nombre is not None:
                    asignatura.nombre = nombre
                if creditos is not None:
                    asignatura.creditos = creditos

        return asignatura

    def eliminar_asignatura(self, codigo) -> Optional[Asignatura]:
        for asignatura in self.asignaturas:
            if asignatura.codigo == codigo:
                self.asignaturas.remove(asignatura)
                return Asignatura
        return None
