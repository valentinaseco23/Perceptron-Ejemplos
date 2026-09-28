def perceptron(entradas, pesos=[1, 1, 2], umbral=3):
    """
    Calcula la salida de un perceptrón utilizando valores por defecto 
    o parámetros explícitamente pasados.
    """
    suma_ponderada = sum(e * w for e, w in zip(entradas, pesos))
    # Función de activación escalón binaria
    return 1 if suma_ponderada >= umbral else 0

# --- LISTA DE ESCENARIOS DE PRUEBA ---
# Factores: [Clima (x1), Dinero (x2), Pareja (x3)]
escenarios_prueba = [
    [0, 0, 0],
    [0, 0, 1],
    [0, 1, 0],
    [0, 1, 1],
    [1, 0, 0],
    [1, 0, 1],
    [1, 1, 0],
    [1, 1, 1]
]

print("=== PRUEBA 1: Usando los valores por defecto (Pesos=[1, 1, 2], Umbral=3) ===")
for i, esc in enumerate(escenarios_prueba, 1):
    resultado = perceptron(esc)
    print(f"Escenario {i} {esc} -> Decisión: {resultado}")

print("\n=== PRUEBA 2: Pasando pesos y umbral explícitamente (Pesos=[2, 2, 4], Umbral=5) ===")
pesos_personalizados = [2, 2, 4]
umbral_personalizado = 5

for i, esc in enumerate(escenarios_prueba, 1):
    resultado = perceptron(esc, pesos=pesos_personalizados, umbral=umbral_personalizado)
    print(f"Escenario {i} {esc} -> Decisión personalizada: {resultado}")