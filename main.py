from RepositorioAlumno import RepositorioAlumno
from RepositorioAsignatura import RepositorioAsignatura, Nivel


def main() -> None:
    repo_alumno = RepositorioAlumno()
    repo_asignaturas = RepositorioAsignatura()

    print("--- Creamos alumnos ---", "\n")

    alumno1 = repo_alumno.crear_alumno("Pepe", 21, "21.212.212-2", "comun")
    alumno2 = repo_alumno.crear_alumno("Juan", 18, "11.111.111-1", "ayudante")
    alumno3 = repo_alumno.crear_alumno("Sofia", 40, "22.222.222-2", "magister")

    # No puede hacer ayudantías ni hacer clases
    alumno1.estudiar()

    # No puede hacer clases
    alumno2.estudiar()
    alumno2.hacer_ayudantia()

    alumno3.estudiar()
    alumno3.hacer_clases()

    print("Obteniendo alumno por rut 22.222.222-2")
    por_rut = repo_alumno.obtener_alumno("22.222.222-2")
    print(por_rut.nombre)

    print("Modifciando alumno por rut 11.111.111-1")
    modificar_rut = repo_alumno.modificar_alumno("11.111.111-1", "Elías")
    print(modificar_rut.nombre)

    print("Eliminando alumno por rut 21.212.212.2")
    repo_alumno.eliminar_alumno("21.212.212-2")

    print("\n", "--- Creamos asignaturas ---", "\n")

    asignatura1 = repo_asignaturas.crear_asignatura(
        "Matemáticas", "101", "5", Nivel.PREGRADO
    )
    asignatura2 = repo_asignaturas.crear_asignatura(
        "Física", "505", "101", Nivel.PREGRADO
    )
    asignatura3 = repo_asignaturas.crear_asignatura(
        "Metodología", "303", "7", Nivel.MAGISTER
    )

    print(asignatura1.creditos)
    print(asignatura2.nombre)
    print(asignatura3.codigo)

    asignatura_con_codigo = repo_asignaturas.obtener_asignatura("303")
    print(asignatura_con_codigo.nombre)

    print("Se asignan asignaturas")

    repo_alumno.cursar_asignatura("11.111.111-1", asignatura1)
    repo_alumno.cursar_asignatura("11.111.111-1", asignatura2)
    repo_alumno.cursar_asignatura("11.111.111-1", asignatura3)

    repo_alumno.desacargar_notas("11.111.111-1")


if __name__ == "__main__":
    main()
