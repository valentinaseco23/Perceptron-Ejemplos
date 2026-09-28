class PerceptronFestival:
    def __init__(self, pesos, umbral):
        self.pesos = pesos
        self.umbral = umbral

    def decidir(self, entradas):
        # Calcula la suma ponderada: (x1*w1) + (x2*w2) + (x3*w3)
        suma = sum(e * w for e, w in zip(entradas, self.pesos))
        # Función de activación escalón: 1 si supera o iguala el umbral, 0 si no
        return 1 if suma >= self.umbral else 0


# --- LISTA DE ESCENARIOS DE PRUEBA BASE ---
# Factores: [x1: Clima (1=bueno, 0=malo), 
#            x2: Pareja (1=quiere ir, 0=no quiere), 
#            x3: Transporte (1=cerca/fácil, 0=lejos/difícil)]
escenarios = [
    [1, 1, 1], # 1. Todos los factores favorables
    [1, 1, 0], # 2. Clima y pareja sí, transporte no
    [1, 0, 1], # 3. Clima y transporte sí, pareja no
    [0, 1, 1], # 4. Pareja y transporte sí, clima no
    [1, 0, 0], # 5. Solo clima favorable
    [0, 1, 0], # 6. Solo pareja quiere ir
    [0, 0, 1], # 7. Solo transporte cerca
    [0, 0, 0]  # 8. Ningún factor favorable
]


print("==================================================================")
print(" OBJETIVO 1: MODELAR PREFERENCIAS ESPECÍFICAS (PERSONALIDADES)")
print("==================================================================")

# --- Modelo A: Dependencia principal de la Pareja (x2) ---
# Asignamos un peso muy alto a la pareja (w2=8) y un umbral de 8. 
# Esto obliga a que la pareja deba querer ir sí o sí para superar el límite.
perceptron_pareja = PerceptronFestival(pesos=[1, 8, 1], umbral=8)

print("\n--- Modelo A: Asistencia dictada estrictamente por la Pareja ---")
for i, esc in enumerate(escenarios, 1):
    resultado = perceptron_pareja.decidir(esc)
    print(f"Escenario {i} {esc} -> ¿Asiste?: {resultado}")


# --- Modelo B: Transporte clave (x3) o al menos dos condiciones favorables ---
# Pesos: [Clima=3, Pareja=3, Transporte=5] con Umbral=5.
# - Si el transporte es cercano (x3=1), aporta 5 puntos y asegura la asistencia de inmediato.
# - Si el transporte es difícil (x3=0), necesita que el clima y la pareja sean 1 (3+3 = 6 >= 5), 
#   cumpliendo la regla de que al menos dos condiciones sean favorables.
perceptron_combinado = PerceptronFestival(pesos=[3, 3, 5], umbral=5)

print("\n--- Modelo B: Transporte cercano O al menos dos condiciones favorables ---")
for i, esc in enumerate(escenarios, 1):
    resultado = perceptron_combinado.decidir(esc)
    print(f"Escenario {i} {esc} -> ¿Asiste?: {resultado}")


print("\n==================================================================")
print(" OBJETIVO 2: ANALIZAR EL IMPACTO DEL UMBRAL (Pesos fijos: w1=6, w2=2, w3=2)")
print("==================================================================")

pesos_fijos = [6, 2, 2]
umbrales_a_probar = [1, 3, 5, 10]

for theta in umbrales_a_probar:
    print(f"\n---> Evaluando con Umbral (θ) = {theta}")
    perceptron_umbral = PerceptronFestival(pesos=pesos_fijos, umbral=theta)
    
    for i, esc in enumerate(escenarios, 1):
        suma_ponderada = sum(e * w for e, w in zip(esc, pesos_fijos))
        resultado = perceptron_umbral.decidir(esc)
        print(f"  Escenario {i} {esc} | Suma calculada: {suma_ponderada:2d} | ¿Decisión?: {resultado}")