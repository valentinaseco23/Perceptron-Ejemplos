class PerceptronTrabajo:
    def __init__(self, pesos, umbral):
        self.pesos = pesos
        self.umbral = umbral

    def decidir(self, entradas):
        # Suma ponderada de los 5 factores de la oferta de trabajo
        suma = sum(e * w for e, w in zip(entradas, self.pesos))
        # Función de activación escalón (1 si acepta la oferta, 0 si la rechaza)
        return 1 if suma >= self.umbral else 0

# --- 1. DEFINICIÓN DE FACTORES (ENTRADAS) ---
# x1: ¿El salario es bueno? (1 = sí, 0 = no)
# x2: ¿El horario es flexible? (1 = sí, 0 = no)
# x3: ¿El puesto ofrece oportunidades de crecimiento? (1 = sí, 0 = no)
# x4: ¿El trayecto al trabajo es corto/fácil? (1 = sí, 0 = no)
# x5: ¿El equipo de trabajo tiene buenas referencias? (1 = sí, 0 = no)

# --- 2 y 3. MODELADO DE "CANDIDATOS" (Pesos y Umbrales) ---
# Perfil 1: "El pragmático" (Prioriza fuertemente el salario y el crecimiento profesional)
pragmatico = PerceptronTrabajo(pesos=[5, 1, 5, 2, 1], umbral=9)

# Perfil 2: "El que busca flexibilidad" (Prioriza el horario flexible y las buenas referencias del equipo)
busca_flexibilidad = PerceptronTrabajo(pesos=[1, 5, 1, 3, 5], umbral=9)

# --- 4. ESCENARIOS DE PRUEBA COMPLEJOS ---
escenarios = [
    [1, 0, 0, 0, 1],  # Escenario 1: Buen salario, sin flexibilidad, sin crecimiento, mal trayecto, equipo excelente
    [0, 1, 0, 1, 1],  # Escenario 2: Salario bajo, horario flexible, sin crecimiento, trayecto corto, equipo excelente
    [1, 1, 1, 1, 1]   # Escenario 3: Oferta perfecta (todo en 1)
]

# --- EJECUCIÓN Y RESULTADOS ---
print("=== CASO 3: DECISIÓN DE ACEPTAR UNA OFERTA DE TRABAJO ===")
print("Factores de entrada: [Salario (x1), Horario (x2), Crecimiento (x3), Trayecto (x4), Equipo (x5)]\n")

for i, esc in enumerate(escenarios, 1):
    res_pragmatico = pragmatico.decidir(esc)
    res_flexible = busca_flexibilidad.decidir(esc)
    
    print(f"Escenario complejo {i} {esc}:")
    print(f"  - 'El pragmático' decide: {'Aceptar oferta (1)' if res_pragmatico == 1 else 'Rechazar oferta (0)'}")
    print(f"  - 'El que busca flexibilidad' decide: {'Aceptar oferta (1)' if res_flexible == 1 else 'Rechazar oferta (0)'}\n")