class PerceptronComprador:
    def __init__(self, pesos, umbral):
        self.pesos = pesos
        self.umbral = umbral

    def decidir(self, entradas):
        # Suma ponderada de los factores de compra
        suma = sum(e * w for e, w in zip(entradas, self.pesos))
        # Función de activación escalón (1 si compra, 0 si no)
        return 1 if suma >= self.umbral else 0

# --- 1. DEFINICIÓN DE FACTORES (ENTRADAS) ---
# x1: ¿El precio es una buena oferta? (1 = sí, 0 = no)
# x2: ¿Las reseñas son mayoritariamente positivas? (1 = sí, 0 = no)
# x3: ¿Necesito el producto con urgencia? (1 = sí, 0 = no)
# x4: ¿Los gastos de envío son gratuitos? (1 = sí, 0 = no)

# --- 2 y 3. MODELADO DE "COMPRADORES" (Pesos y Umbrales) ---
# Perfil 1: "El cazador de ofertas" (Prioriza fuertemente el precio y envío gratis)
cazador_ofertas = PerceptronComprador(pesos=[5, 1, 1, 4], umbral=8)

# Perfil 2: "El precavido" (Prioriza fuertemente las reseñas positivas)
precavido = PerceptronComprador(pesos=[1, 7, 1, 1], umbral=6)

# Perfil 3: "El impaciente" (Prioriza la urgencia por encima del precio)
impaciente = PerceptronComprador(pesos=[1, 1, 6, 1], umbral=6)

# --- 4. ESCENARIOS DE PRUEBA ---
escenarios = [
    [1, 1, 0, 1],  # Escenario 1: Buena oferta, buenas reseñas, sin urgencia, envío gratis
    [0, 1, 1, 0],  # Escenario 2: Sin oferta, buenas reseñas, con urgencia, sin envío gratis
    [1, 0, 0, 1],  # Escenario 3: Buena oferta, malas reseñas, sin urgencia, envío gratis
    [1, 1, 1, 1]   # Escenario 4: Todo favorable
]

# --- EJECUCIÓN Y RESULTADOS ---
print("=== CASO 2: DECISIÓN DE COMPRAR UN PRODUCTO EN LÍNEA ===")
print("Factores de entrada: [Oferta (x1), Reseñas (x2), Urgencia (x3), Envío Gratis (x4)]\n")

for i, esc in enumerate(escenarios, 1):
    res_cazador = cazador_ofertas.decidir(esc)
    res_precavido = precavido.decidir(esc)
    res_impaciente = impaciente.decidir(esc)
    
    print(f"Escenario {i} {esc}:")
    print(f"  - 'El cazador de ofertas' decide: {'Comprar (1)' if res_cazador == 1 else 'No comprar (0)'}")
    print(f"  - 'El precavido' decide: {'Comprar (1)' if res_precavido == 1 else 'No comprar (0)'}")
    print(f"  - 'El impaciente' decide: {'Comprar (1)' if res_impaciente == 1 else 'No comprar (0)'}\n")