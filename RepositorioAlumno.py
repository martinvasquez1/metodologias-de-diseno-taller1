from typing import Optional
import random

from Asignatura import Asignatura, Nivel
from Alumno import (
    Alumno,
    Alumni,
    EstudianteComun,
    EstudianteAyudante,
    EstudianteDoctorado,
    EstudianteMagister,
)


class RepositorioAlumno:
    def __init__(self):
        self.alumnos = []

    def existe_alumno_con_rut(self, rut) -> bool:
        for alumno in self.alumnos:
            if alumno.rut == rut:
                return True
        return False

    def crear_alumno(self, nombre, edad, rut, tipo: str) -> Alumno:
        tipos = {
            "alumni": Alumni,
            "comun": EstudianteComun,
            "ayudante": EstudianteAyudante,
            "magister": EstudianteMagister,
            "doctorado": EstudianteDoctorado,
        }

        if not tipo.lower() in tipos:
            raise ValueError("Tipo de estudiante no reconocido.")
        if self.existe_alumno_con_rut(rut):
            raise ValueError("Ya existe estudiante con ese RUT.")

        nuevo_alumno = tipos[tipo](nombre, edad, rut)
        self.alumnos.append(nuevo_alumno)

        return nuevo_alumno

    def obtener_alumnos(self):
        return self.alumnos

    def obtener_alumno(self, rut) -> Optional[Alumno]:
        for alumno in self.alumnos:
            if alumno.rut == rut:
                return alumno
        return None

    def modificar_alumno(self, rut, nombre=None, edad=None) -> Optional[Alumno]:
        for alumno in self.alumnos:
            if alumno.rut == rut:
                if nombre is not None:
                    alumno.nombre = nombre
                if edad is not None:
                    alumno.edad = edad

                return alumno

        return None

    def eliminar_alumno(self, rut) -> None:
        for alumno in self.alumnos:
            if alumno.rut == rut:
                self.alumnos.remove(alumno)

    def cursar_asignatura(self, rut: str, asignatura: Asignatura) -> None:
        alumno = self.obtener_alumno(rut)

        if not alumno:
            return None

        if asignatura.nivel.value != alumno.nivel.value:
            print(
                "(!) Este alumno no puede cursar esta asignatura para",
                asignatura.nivel.value,
            )
            return None

        alumno.asignaturas.append(asignatura)

    def desacargar_notas(self, rut):
        alumno = self.obtener_alumno(rut)

        if not alumno:
            return None

        print("Descargando notas de asignatuas para:", rut, "\n")

        for asignatura in alumno.asignaturas:
            notas = [round(random.uniform(1, 7), 1) for _ in range(3)]
            print(asignatura.nombre)

            for nota in notas:
                print("- ", nota)
