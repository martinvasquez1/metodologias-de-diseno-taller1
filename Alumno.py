from abc import ABC, abstractmethod


class Alumno(ABC):
    def __init__(self, nombre, edad, rut):
        self.nombre = nombre
        self.edad = edad
        self.rut = rut


# No estudia ni puede hacer ayudantias
class Alumni(Alumno):
    pass


class IEstudiar(ABC):
    @abstractmethod
    def estudiar(self):
        pass


# Solo estudia
class EstudianteComun(Alumno, IEstudiar):
    def __init__(self, nombre, edad, rut):
        super().__init__(nombre, edad, rut)
        self.asignaturas = []

    def estudiar(self):
        print("Estudiante comun estudiando")


class IAyudante(ABC):
    @abstractmethod
    def hacer_ayudantia(self):
        pass


# Pueden estudiar y hacer ayudantías
class EstudianteAyudante(Alumno, IAyudante):
    def __init__(self, nombre, edad, rut):
        super().__init__(nombre, edad, rut)
        self.asignaturas = []

    def estudiar(self):
        print("Estudiante ayudante estudiando")

    def hacer_ayudantia(self):
        print("Estudiante ayudante haciendo ayudantía")


class IClases(ABC):
    @abstractmethod
    def hacer_clases(self):
        pass


# Estudia y hace clases
class EstudianteMagister(Alumno, IEstudiar, IClases):
    def __init__(self, nombre, edad, rut):
        super().__init__(nombre, edad, rut)
        self.asignaturas = []

    def estudiar(self):
        print("Estudiante magister estudiando")

    def hacer_clases(self):
        print("Estudiante magister haciendo clases")


class IInvestigar(ABC):
    @abstractmethod
    def hacer_investigacion(self):
        pass


# Estudia, hace clases e investiga
class EstudianteDoctorado(Alumno, IEstudiar, IClases, IInvestigar):
    def __init__(self, nombre, edad, rut):
        super().__init__(nombre, edad, rut)
        self.asignaturas = []

    def estudiar(self):
        print("Estudiante doctorado estudiando")

    def hacer_clases(self):
        print("Estudiante doctorado haciendo clases")

    def hacer_investigacion(self):
        print("Estudiante doctorado haciendo investigación")
