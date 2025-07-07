from enum import Enum


class Nivel(Enum):
    PREGRADO = "Pregrado"
    MAGISTER = "Magister"
    DOCTORADO = "Doctorado"
    ALUMNI = "Alumni"


class Asignatura:
    def __init__(self, nombre, codigo, creditos, nivel: Nivel):
        self.nombre = nombre
        self.codigo = codigo
        self.creditos = creditos
        self.nivel = nivel
