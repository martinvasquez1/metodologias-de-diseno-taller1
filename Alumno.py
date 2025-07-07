from abc import ABC, abstractmethod
from Asignatura import Asignatura, Nivel
from typing import List


class Alumno(ABC):
    def __init__(self, nombre: str, edad: int, rut: str, nivel: Nivel) -> None:
        self.nombre: str = nombre
        self.edad: int = edad
        self.rut: str = rut
        self.nivel: Nivel = nivel


# No estudia ni puede hacer ayudantias
class Alumni(Alumno):
    def __init__(self, nombre: str, edad: int, rut: str) -> None:
        super().__init__(nombre, edad, rut, Nivel.ALUMNI)


class IEstudiar(ABC):
    @abstractmethod
    def estudiar(self) -> None:
        pass


# Solo estudia
class EstudianteComun(Alumno, IEstudiar):
    def __init__(self, nombre: str, edad: int, rut: str) -> None:
        super().__init__(nombre, edad, rut, Nivel.PREGRADO)
        self.asignaturas: List[Asignatura] = []

    def estudiar(self) -> None:
        print("Estudiante comun estudiando")


class IAyudante(ABC):
    @abstractmethod
    def hacer_ayudantia(self) -> None:
        pass


# Pueden estudiar y hacer ayudantías
class EstudianteAyudante(Alumno, IAyudante):
    def __init__(self, nombre: str, edad: int, rut: str) -> None:
        super().__init__(nombre, edad, rut, Nivel.PREGRADO)
        self.asignaturas: List[Asignatura] = []

    def estudiar(self) -> None:
        print("Estudiante ayudante estudiando")

    def hacer_ayudantia(self) -> None:
        print("Estudiante ayudante haciendo ayudantía")


class IClases(ABC):
    @abstractmethod
    def hacer_clases(self) -> None:
        pass


# Estudia y hace clases
class EstudianteMagister(Alumno, IEstudiar, IClases):
    def __init__(self, nombre: str, edad: int, rut: str) -> None:
        super().__init__(nombre, edad, rut, Nivel.MAGISTER)
        self.asignaturas: List[Asignatura] = []

    def estudiar(self) -> None:
        print("Estudiante magister estudiando")

    def hacer_clases(self) -> None:
        print("Estudiante magister haciendo clases")


class IInvestigar(ABC):
    @abstractmethod
    def hacer_investigacion(self) -> None:
        pass


# Estudia, hace clases e investiga
class EstudianteDoctorado(Alumno, IEstudiar, IClases, IInvestigar):
    def __init__(self, nombre: str, edad: int, rut: str) -> None:
        super().__init__(nombre, edad, rut, Nivel.DOCTORADO)
        self.asignaturas: List[Asignatura] = []

    def estudiar(self) -> None:
        print("Estudiante doctorado estudiando")

    def hacer_clases(self) -> None:
        print("Estudiante doctorado haciendo clases")

    def hacer_investigacion(self) -> None:
        print("Estudiante doctorado haciendo investigación")
