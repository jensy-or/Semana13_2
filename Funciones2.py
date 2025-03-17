# Definir la función para calcular el promedio de temperaturas
def calcular_promedio_temperaturas(temperaturas, ciudades, ciudad_buscada):
    # Verificar si la ciudad buscada está en la lista de ciudades
    if ciudad_buscada not in ciudades:
        # Si la ciudad no está en la lista, devolver un mensaje de error
        return f"La ciudad '{ciudad_buscada}' no se encuentra en la lista de ciudades."

    # Obtener el índice de la ciudad buscada en la lista de ciudades
    ciudad_idx = ciudades.index(ciudad_buscada)
    # Acceder a las temperaturas de la ciudad seleccionada usando el índice
    ciudad_temperaturas = temperaturas[ciudad_idx]

    # Inicializar variables para la suma de temperaturas y el conteo de días
    suma_temperaturas = 0
    total_dias = 0

    # Iterar sobre cada semana de la ciudad seleccionada
    for semana in ciudad_temperaturas:
        # Iterar sobre cada día de la semana
        for dia in semana:
            # Sumar la temperatura del día a la suma total
            suma_temperaturas += dia["temp"]
            # Incrementar el conteo de días
            total_dias += 1

    # Calcular el promedio de temperaturas
    promedio = suma_temperaturas / total_dias if total_dias > 0 else 0
    # Devolver el promedio formateado como un string
    return f"El promedio de temperaturas en {ciudad_buscada} es: {promedio:.2f}°C"

# Definir la matriz 3D de temperaturas
temperaturas = [
    [   # Cuenca
        [   # Semana 1
            {"day": "Lunes", "temp": 56},  # Temperatura del lunes
            {"day": "Martes", "temp": 45},  # Temperatura del martes
            {"day": "Miércoles", "temp": 56},  # Temperatura del miércoles
            {"day": "Jueves", "temp": 80},  # Temperatura del jueves
            {"day": "Viernes", "temp": 93},  # Temperatura del viernes
            {"day": "Sábado", "temp": 42},  # Temperatura del sábado
            {"day": "Domingo", "temp": 35}  # Temperatura del domingo
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 23},  # Temperatura del lunes
            {"day": "Martes", "temp": 88},  # Temperatura del martes
            {"day": "Miércoles", "temp": 81},  # Temperatura del miércoles
            {"day": "Jueves", "temp": 83},  # Temperatura del jueves
            {"day": "Viernes", "temp": 77},  # Temperatura del viernes
            {"day": "Sábado", "temp": 89},  # Temperatura del sábado
            {"day": "Domingo", "temp": 41}  # Temperatura del domingo
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 77},  # Temperatura del lunes
            {"day": "Martes", "temp": 81},  # Temperatura del martes
            {"day": "Miércoles", "temp": 85},  # Temperatura del miércoles
            {"day": "Jueves", "temp": 82},  # Temperatura del jueves
            {"day": "Viernes", "temp": 88},  # Temperatura del viernes
            {"day": "Sábado", "temp": 91},  # Temperatura del sábado
            {"day": "Domingo", "temp": 95}  # Temperatura del domingo
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 75},  # Temperatura del lunes
            {"day": "Martes", "temp": 78},  # Temperatura del martes
            {"day": "Miércoles", "temp": 80},  # Temperatura del miércoles
            {"day": "Jueves", "temp": 79},  # Temperatura del jueves
            {"day": "Viernes", "temp": 84},  # Temperatura del viernes
            {"day": "Sábado", "temp": 87},  # Temperatura del sábado
            {"day": "Domingo", "temp": 91}  # Temperatura del domingo
        ]
    ],
    [   # Quito
        [   # Semana 1
            {"day": "Lunes", "temp": 62},  # Temperatura del lunes
            {"day": "Martes", "temp": 64},  # Temperatura del martes
            {"day": "Miércoles", "temp": 68},  # Temperatura del miércoles
            {"day": "Jueves", "temp": 70},  # Temperatura del jueves
            {"day": "Viernes", "temp": 73},  # Temperatura del viernes
            {"day": "Sábado", "temp": 75},  # Temperatura del sábado
            {"day": "Domingo", "temp": 79}  # Temperatura del domingo
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 63},  # Temperatura del lunes
            {"day": "Martes", "temp": 66},  # Temperatura del martes
            {"day": "Miércoles", "temp": 70},  # Temperatura del miércoles
            {"day": "Jueves", "temp": 72},  # Temperatura del jueves
            {"day": "Viernes", "temp": 75},  # Temperatura del viernes
            {"day": "Sábado", "temp": 77},  # Temperatura del sábado
            {"day": "Domingo", "temp": 81}  # Temperatura del domingo
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 61},  # Temperatura del lunes
            {"day": "Martes", "temp": 65},  # Temperatura del martes
            {"day": "Miércoles", "temp": 68},  # Temperatura del miércoles
            {"day": "Jueves", "temp": 70},  # Temperatura del jueves
            {"day": "Viernes", "temp": 72},  # Temperatura del viernes
            {"day": "Sábado", "temp": 76},  # Temperatura del sábado
            {"day": "Domingo", "temp": 80}  # Temperatura del domingo
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 64},  # Temperatura del lunes
            {"day": "Martes", "temp": 67},  # Temperatura del martes
            {"day": "Miércoles", "temp": 69},  # Temperatura del miércoles
            {"day": "Jueves", "temp": 71},  # Temperatura del jueves
            {"day": "Viernes", "temp": 74},  # Temperatura del viernes
            {"day": "Sábado", "temp": 77},  # Temperatura del sábado
        ]
    ],
    [   # Guayaquil
        [   # Semana 1
            {"day": "Lunes", "temp": 56},  # Temperatura del lunes
            {"day": "Martes", "temp": 45},  # Temperatura del martes
            {"day": "Miércoles", "temp": 56},  # Temperatura del miércoles
            {"day": "Jueves", "temp": 80},  # Temperatura del jueves
            {"day": "Viernes", "temp": 93},  # Temperatura del viernes
            {"day": "Sábado", "temp": 42},  # Temperatura del sábado
            {"day": "Domingo", "temp": 35}  # Temperatura del domingo
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 23},  # Temperatura del lunes
            {"day": "Martes", "temp": 88},  # Temperatura del martes
            {"day": "Miércoles", "temp": 81},  # Temperatura del miércoles
            {"day": "Jueves", "temp": 83},  # Temperatura del jueves
            {"day": "Viernes", "temp": 77},  # Temperatura del viernes
            {"day": "Sábado", "temp": 89},  # Temperatura del sábado
            {"day": "Domingo", "temp": 41}  # Temperatura del domingo
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 77},  # Temperatura del lunes
            {"day": "Martes", "temp": 81},  # Temperatura del martes
            {"day": "Miércoles", "temp": 85},  # Temperatura del miércoles
            {"day": "Jueves", "temp": 82},  # Temperatura del jueves
            {"day": "Viernes", "temp": 88},  # Temperatura del viernes
            {"day": "Sábado", "temp": 91},  # Temperatura del sábado
            {"day": "Domingo", "temp": 95}  # Temperatura del domingo
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 75},  # Temperatura del lunes
            {"day": "Martes", "temp": 78},  # Temperatura del martes
            {"day": "Miércoles", "temp": 80},  # Temperatura del miércoles
            {"day": "Jueves", "temp": 79},  # Temperatura del jueves
            {"day": "Viernes", "temp": 84},  # Temperatura del viernes
            {"day": "Sábado", "temp": 87},  # Temperatura del sábado
            {"day": "Domingo", "temp": 91}  # Temperatura del domingo
        ]
    ]
]
# Lista de ciudades
ciudades = ["Cuenca", "Quito", "Guayaquil"]  # Definimos una lista que contiene los nombres de las ciudades

# Calcular el promedio de temperaturas para cada ciudad y semana
for ciudad_idx, ciudad in enumerate(temperaturas):  # Iteramos sobre la lista de temperaturas, obteniendo el índice y los datos de cada ciudad
    # Imprimir el nombre de la ciudad y un mensaje indicando que se calculará el promedio de temperaturas
    print(f"\nPromedio de temperaturas en {ciudades[ciudad_idx]}:")  # Usamos el índice para acceder al nombre de la ciudad correspondiente

    # Iterar sobre cada semana de la ciudad actual
    for semana_idx, semana in enumerate(ciudad):  # Enumeramos las semanas de la ciudad, obteniendo el índice y los datos de cada semana
        # Calcular la suma de las temperaturas de todos los días de la semana
        suma_temperaturas = sum([dia["temp"] for dia in semana])  # Usamos una lista por comprensión para extraer las temperaturas de cada día y sumarlas

        # Calcular el promedio de temperaturas dividiendo la suma total por el número de días en la semana
        promedio = suma_temperaturas / len(semana)  # La longitud de la semana nos da el número de días

        # Imprimir el promedio de temperaturas para la semana actual, formateado a dos decimales
        print(f"Semana {semana_idx + 1}: {promedio:.2f}°C")  # Usamos el índice de la semana para mostrar el número de semana y el promedio calculado