from .estudiante import devolver_materias

def estudiante_registrado_en_materia(nombre_estudiante, materia):
    try:
        materias = devolver_materias(nombre_estudiante)
        return materia in materias
    except ValueError as e:
        print(e)
        return False
