def mostrar_encabezado_escuela():
    print("INSTITUTO X")
    print("REGISTRO Y EVALUACION DE CALIFICACIONES")

def obtener_nota_minima_aprobatoria():
    return 6.0

def evaluar_rendimiento(nota_final):
    if nota_final < 7.0:
        return "Reprobado"
    elif nota_final < 9.4:
        return "Aprobado"
    else:
        return "Excelente"
    
def calcular_promedio_ponderado(nota_examenes, nota_tareas):
    promedio = (nota_examenes * 0.70) + (nota_tareas * 0.30)
    return round(promedio,1)

def generar_boleta(nombre_alumno, nota_examenes, nota_tareas):
    nota_final = calcular_promedio_ponderado(nota_examenes, nota_tareas)
    nota_minima = obtener_nota_minima_aprobatoria()
    estado = evaluar_rendimiento(nota_final)

    print("Boleta del Alumno")
    print("Nombre", nombre_alumno)
    print("Nota de Examenes ", nota_examenes)
    print("Nota de Tareas ", nota_tareas)
    print("Nota Final ", nota_final)
    print("Estado: ", estado)
    if nota_final < nota_minima:
        print("Necesita Presentar Examen Extraordinario")
    else:
        print("No Necesita Presentar Examen Extraordinario")

mostrar_encabezado_escuela()
nombre = input("Ingrese el nombre del alumno: ")
examenes = float(input("Ingrese la nota de examenes: "))
tareas = float(input("Ingrese la nota de tareas: "))
generar_boleta(nombre, examenes, tareas)
