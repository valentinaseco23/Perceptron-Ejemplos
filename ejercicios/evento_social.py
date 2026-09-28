class PerceptronSocial:
    def __init__(self, pesos, umbral):
        self.pesos = pesos
        self.umbral = umbral

    def decidir(self, entradas):
        # Suma ponderada de los factores
        suma = sum(e * w for e, w in zip(entradas, self.pesos))
        # Función de activación escalón (1 si asiste, 0 si no)
        return 1 if suma >= self.umbral else 0

# --- 1. DEFINICIÓN DE FACTORES (ENTRADAS) ---
# x1: ¿Mis amigos cercanos van? (1 = sí, 0 = no)
# x2: ¿El evento es de un tema que me interesa? (1 = sí, 0 = no)
# x3: ¿Tiene fácil acceso/transporte? (1 = fácil, 0 = difícil)
# x4: ¿No tengo pendientes de trabajo/estudio? (1 = sin pendientes, 0 = con pendientes)

# --- 2. MODELADO DE "PERSONALIDADES" (Pesos y Umbrales) ---
# Perfil 1: "El social" (Prioriza fuertemente a los amigos)
perfil_social = PerceptronSocial(pesos=[6, 1, 1, 1], umbral=5)

# Perfil 2: "El selectivo" (Prioriza el tema de interés)
perfil_selectivo = PerceptronSocial(pesos=[1, 6, 2, 2], umbral=6)

# Perfil 3: "El perezoso" (Prioriza que el transporte sea cómodo y fácil)
perfil_perezoso = PerceptronSocial(pesos=[1, 1, 6, 2], umbral=6)

# --- 3. ESCENARIOS DE PRUEBA ---
escenarios = [
    [1, 0, 1, 0],  # Escenario 1: Van amigos, sin interés, fácil acceso, con pendientes
    [0, 1, 1, 1],  # Escenario 2: Sin amigos, tema de interés, fácil acceso, sin pendientes
    [1, 1, 0, 1],  # Escenario 3: Van amigos, tema de interés, transporte difícil, sin pendientes
    [0, 0, 1, 1]   # Escenario 4: Solo transporte fácil y sin pendientes
]

# --- 4. EJECUCIÓN Y RESULTADOS ---
print("=== CASO 1: DECISIÓN DE ASISTIR A UN EVENTO SOCIAL ===")
print("Factores de entrada: [Amigos (x1), Tema (x2), Transporte (x3), Sin Pendientes (x4)]\n")

for i, esc in enumerate(escenarios, 1):
    res_social = perfil_social.decidir(esc)
    res_selectivo = perfil_selectivo.decidir(esc)
    res_perezoso = perfil_perezoso.decidir(esc)
    
    print(f"Escenario {i} {esc}:")
    print(f"  - 'El social' decide: {'Asistir (1)' if res_social == 1 else 'No asistir (0)'}")
    print(f"  - 'El selectivo' decide: {'Asistir (1)' if res_selectivo == 1 else 'No asistir (0)'}")
    print(f"  - 'El perezoso' decide: {'Asistir (1)' if res_perezoso == 1 else 'No asistir (0)'}\n")