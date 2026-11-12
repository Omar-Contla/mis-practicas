def maxima_profundidad(comentarios):
    if len(comentarios) == 0:
        return 0

    primero = comentarios[0]

    if isinstance(primero, list):
        profundidad_actual = 1 + maxima_profundidad(primero)
    else:
        profundidad_actual = 1

    profundidad_resto = maxima_profundidad(comentarios[1:])

    return max(profundidad_actual, profundidad_resto)


hilo = ["Comentario 1", ["Respuesta 1.1", ["Respuesta 1.1.1"]], "Comentario 2"]

resultado = maxima_profundidad(hilo)

print(resultado)
