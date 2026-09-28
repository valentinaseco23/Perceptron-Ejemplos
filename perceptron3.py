class Perceptron:
    def __init__(self, pesos, umbral):
        self.pesos = pesos    # Nivel de importancia de cada factor
        self.umbral = umbral  # Límite mínimo para que la decisión sea "1"

    def decidir(self, entradas):
        # 1. Multiplica cada entrada por su peso y suma todo
        suma = sum(e * p for e, p in zip(entradas, self.pesos))
       
        # 2. Toma de decisión: ¿Supera el umbral?
        return 1 if suma >= self.umbral else 0


# --- CONFIGURACIÓN DEL PERCEPTRÓN: COMIDA PARA SALCHICHA ---
# - ¿Maulló pidiendo comida? (Vale 4 puntos)
# - ¿Ya pasó su horario habitual de comida? (Vale 5 puntos)
# - Umbral: Se necesitan al menos 6 puntos para ceder y llenarle el plato
neurona_gato = Perceptron(pesos=[4, 5], umbral=6)

print("=== ¿LE DOY DE COMER A SALCHICHA? ===")

try:
    # Solicitamos los datos al usuario por consola
    maullido = int(input("¿Maulló? (1 = Sí / 0 = No): "))
    horario = int(input("¿Ya pasó su horario habitual? (1 = Sí / 0 = No): "))

    # Ejecutamos la neurona con las entradas ingresadas
    resultado = neurona_gato.decidir([maullido, horario])

    print("\n--- RESULTADO ---")
    if resultado == 1:
        print("¡Decisión: SÍ, corre a llenarle el plato a Salchicha! (1) 🐱")
    else:
        print("Decisión: NO, todavía puede esperar un poco (0).")

except ValueError:
    print("Error: Por favor ingresa únicamente valores numéricos (1 o 0).")