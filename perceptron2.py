class Perceptron:
    def __init__(self, pesos, umbral):
        self.pesos = pesos    # Nivel de importancia de cada factor
        self.umbral = umbral  # Límite mínimo para que la decisión sea "1"

    def decidir(self, entradas):
        # 1. Multiplica cada entrada por su peso y suma todo
        suma = sum(e * p for e, p in zip(entradas, self.pesos))
       
        # 2. Toma de decisión: ¿Supera el umbral?
        return 1 if suma >= self.umbral else 0


# --- CONFIGURACIÓN DEL PERCEPTRÓN: FÓRMULA 1 ---
# - ¿Logró la Pole Position el sábado? (Vale 5 puntos)
# - ¿El auto tiene buen ritmo de carrera? (Vale 4 puntos)
# - Umbral: Se necesitan al menos 7 puntos para apostar por el primer puesto
neurona_f1 = Perceptron(pesos=[5, 4, 3, 5],umbral=7)

print("=== PREDICCIÓN DE VICTORIA: F1 (LANDO NORRIS) ===")

try:
    pole = int(input("¿Logró la Pole Position? (1 = Sí / 0 = No): "))
    ritmo = int(input("¿Tiene buen ritmo de carrera? (1 = Sí / 0 = No): "))
    parada_box = int(input("¿Tuvo una buena parada de boxes? (1 = Sí / 0 = No):"))
    degradacion = int(input("¿Tuvo mucha degradación durante las primeras vueltas? (1 = Sí / 0 = No):"))

    # Ejecutamos la neurona con las entradas ingresadas
    resultado = neurona_f1.decidir([pole, ritmo, parada_box, degradacion])

    print("\n--- RESULTADO ---")
    if resultado == 1:
        print("¡Predicción: Altas chances de VICTORIA (1)! 🏆")
    else:
        print("Predicción: Difícil que gane hoy (0).")

except ValueError:
    print("Error: Por favor ingresa únicamente valores numéricos (1 o 0).")