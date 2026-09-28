class Perceptron:
    def __init__(self, pesos, umbral):
        self.pesos = pesos    # Nivel de importancia: [Tareas, Examen]
        self.umbral = umbral  # Límite de puntos para aprobar

    def decidir(self, entradas):
        # 1. Multiplica cada entrada por su peso y suma todo
        suma = sum(e * p for e, p in zip(entradas, self.pesos))
       
        # 2. Toma de decisión: ¿Supera el umbral?
        return 1 if suma >= self.umbral else 0


# --- CONFIGURACIÓN DEL PERCEPTRÓN ---
# - Tareas valen: 3 pts
# - Examen vale: 7 pts
# - Se aprueba con: 6 pts
neurona = Perceptron(pesos=[3, 7], umbral=6)

print("SISTEMA DE EVALUACIÓN DE MATERIA")

# Solicitamos los datos de forma interactiva por consola
try:
    tarea = int(input("¿Entrego las tareas? (1 = Sí / 0 = No): "))
    examen = int(input("¿Aprobó el examen final? (1 = Sí / 0 = No): "))

    # Ejecutamos la neurona con las entradas ingresadas
    resultado = neurona.decidir([tarea, examen])

    print("\n--- RESULTADO ---")
    if resultado == 1:
        print("¡Estado: APROBADO (1)!")
    else:
        print("Estado: NO APROBADO (0).")

except ValueError:
    print("Error: Por favor ingresa únicamente valores numéricos (1 o 0).")