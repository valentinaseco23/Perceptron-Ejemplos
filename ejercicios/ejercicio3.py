def perceptron_ampliado(entradas, pesos, umbral):
    """
    Función de perceptrón ampliado que recibe 6 entradas y sus respectivos pesos.
    """
    suma_ponderada = sum(e * w for e, w in zip(entradas, pesos))
    return 1 if suma_ponderada >= umbral else 0

# --- 1. DEFINICIÓN DE ENTRADAS Y PESOS ---
# Entradas (6 variables):
# x1: ¿Buen clima? (1 = sí, 0 = no)
# x2: ¿Va la pareja? (1 = sí, 0 = no)
# x3: ¿Transporte cercano? (1 = sí, 0 = no)
# x4: ¿Tiene música en vivo? (1 = sí, 0 = no)
# x5: ¿La entrada es gratuita? (1 = sí, 0 = no)
# x6: ¿Van los amigos? (1 = sí, 0 = no)

# Asignamos pesos según la importancia personal (ej. pareja y amigos pesan más)
pesos_personales = [1, 4, 1, 2, 3, 3]  # [w1, w2, w3, w4, w5, w6]
umbral_personal = 8

# --- 2. NUEVOS ESCENARIOS DE PRUEBA (Combinaciones de las 6 variables) ---
escenarios_ampliados = [
    [1, 1, 1, 1, 1, 1],  # Escenario 1: ¡Todo perfecto! (Clima, pareja, transporte, música, gratis, amigos)
    [0, 1, 0, 1, 0, 1],  # Escenario 2: Mal clima y transporte, pero va la pareja, hay música y amigos
    [1, 0, 1, 0, 1, 0],  # Escenario 3: Buen clima, transporte cerca, entrada gratis, pero sin pareja ni amigos
    [0, 0, 0, 1, 1, 1],  # Escenario 4: Solo hay música, entrada gratis y amigos (sin clima, ni pareja, ni transporte)
    [0, 0, 0, 0, 0, 0]   # Escenario 5: Nada favorable
]

# --- 3. EJECUCIÓN DEL CÓDIGO ---
print("=== PUNTO 3: PERCEPTRÓN AMPLIADO DEL FESTIVAL (6 ENTRADAS) ===")
print(f"Pesos asignados: {pesos_personales}")
print(f"Umbral elegido: {umbral_personal}\nlee:")

for i, esc in enumerate(escenarios_ampliados, 1):
    suma = sum(e * w for e, w in zip(esc, pesos_personales))
    resultado = perceptron_ampliado(esc, pesos_personales, umbral_personal)
    print(f"Escenario {i} {esc}")
    print(f"   -> Suma ponderada: {suma} | ¿Decide ir?: {'SÍ (1)' if resultado == 1 else 'NO (0)'}\n")