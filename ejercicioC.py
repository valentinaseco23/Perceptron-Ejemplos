import math

class PerceptronDosEntradas:
    def __init__(self, pesos, umbral):
        self.pesos = pesos  # [w1, w2]
        self.umbral = umbral

    def decidir(self, x1, x2):
        z = (x1 * self.pesos[0]) + (x2 * self.pesos[1]) - self.umbral
        escalon = 1 if z >= 0 else 0
        z_lim = max(-500, min(500, z))
        sigmoide = 1 / (1 + math.exp(-z_lim))
        return escalon, sigmoide, z

print("=== APARTADO C: PUNTOS 4 Y 5 (CLIMA Y PAREJA) ===")
perfil = PerceptronDosEntradas(pesos=[1, 1], umbral=2)

try:
    c = int(input("Ingresa el clima x1 (0 = Malo, 1 = Bueno): "))
    p = int(input("Ingresa la pareja x2 (0 = No va, 1 = Sí va): "))
    
    if c in [0, 1] and p in [0, 1]:
        res_escalon, res_sigmoide, z_val = perfil.decidir(c, p)
        print(f"\nSuma Z: {z_val}")
        print(f"Decisión (Escalón 0/1): {res_escalon}")
        print(f"Probabilidad (Sigmoide): {res_sigmoide:.4f}")
        
        if res_escalon == 1:
            print("👉 El punto cae en el grupo de asistencia (VERDE).")
        else:
            print("🛑 El punto cae en el grupo de rechazo (ROJO).")
    else:
        print("⚠️ Ingresa únicamente 0 o 1.")
except ValueError:
    print("⚠️ Error de valor numérico.")