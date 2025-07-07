from typing import List, Optional

from Asignatura import Asignatura, Nivel


class RepositorioAsignatura:
    def __init__(self) -> None:
        self.asignaturas: List[Asignatura] = []

    def crear_asignatura(
        self, nombre: str, codigo: str, creditos: int, nivel: Nivel
    ) -> Asignatura:
        nueva_asignatura = Asignatura(nombre, codigo, creditos, nivel)
        self.asignaturas.append(nueva_asignatura)
        return nueva_asignatura

    def obtener_asignaturas(self) -> List[Asignatura]:
        return self.asignaturas

    def obtener_asignatura(self, codigo: str) -> Optional[Asignatura]:
        for asignatura in self.asignaturas:
            if asignatura.codigo == codigo:
                return asignatura
        return None

    def modificar_asignatura(
        self, codigo: str, nombre: Optional[str] = None, creditos: Optional[int] = None
    ) -> Optional[Asignatura]:
        for asignatura in self.asignaturas:
            if asignatura.codigo == codigo:
                if nombre is not None:
                    asignatura.nombre = nombre
                if creditos is not None:
                    asignatura.creditos = creditos

        return asignatura

    def eliminar_asignatura(self, codigo: str) -> Optional[Asignatura]:
        for asignatura in self.asignaturas:
            if asignatura.codigo == codigo:
                self.asignaturas.remove(asignatura)
                return Asignatura
        return None
