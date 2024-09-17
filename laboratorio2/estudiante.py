estudiantes = {
    "Daniel": ["Matematica", "Computacion"],
    "Maria": ["Matematica", "Fisica"],
    "Juan": ["Quimica", "Biologia"],
    "Ana": ["Fisica", "Historia"],
    "Luis": ["Computacion", "Matematica"]
}

def devolver_materias(nombre_estudiante):
    try:
        return estudiantes[nombre_estudiante]
    except KeyError:
        raise ValueError(f"El estudiante {nombre_estudiante} no está registrado.")
