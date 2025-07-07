from enum import Enum

class Nivel(Enum):
    PREGRADO = "Pregrado"
    MAGISTER = "Magister"
    DOCTORADO = "Doctorado"
    ALUMNI = "Alumni"


class Asignatura:
    def __init__(self, nombre: str, codigo: str, creditos: int, nivel: Nivel) -> None:
        self.nombre: str = nombre
        self.codigo: str = codigo
        self.creditos: int = creditos
        self.nivel: Nivel = nivel
