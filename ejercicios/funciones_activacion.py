import math

class PerceptronConActivacion:
    def __init__(self, pesos, umbral, tipo_activacion="escalon"):
        self.pesos = pesos
        self.umbral = umbral
        self.tipo_activacion = tipo_activacion

    def evaluar(self, entradas):
        # 1. Suma ponderada menos el umbral
        z = sum(e * w for e, w in zip(entradas, self.pesos)) - self.umbral
        
        # 2. Aplicar función de activación
        if self.tipo_activacion == "escalon":
            return 1 if z >= 0 else 0
        elif self.tipo_activacion == "lineal":
            return z
        elif self.tipo_activacion == "sigmoide":
            z_lim = max(-500, min(500, z))
            return 1 / (1 + math.exp(-z_lim))
        elif self.tipo_activacion == "tanh":
            return math.tanh(z)
        elif self.tipo_activacion == "relu":
            return max(0.0, z)
        return z

# Escenario de prueba (ej. Oferta de trabajo con ciertos factores cumplidos)
escenario_ejemplo = [1, 1, 0, 1, 1] 
pesos_trabajo = [4, 1, 4, 1, 1]
umbral_trabajo = 7

print("=== ANÁLISIS DE FUNCIONES DE ACTIVACIÓN EN OFERTA DE TRABAJO ===")
print(f"Escenario evaluado: {escenario_ejemplo}\n")

activaciones = ["escalon", "lineal", "sigmoide", "tanh", "relu"]

for act in activaciones:
    modelo = PerceptronConActivacion(pesos_trabajo, umbral_trabajo, tipo_activacion=act)
    resultado = modelo.evaluar(escenario_ejemplo)
    
    if act == "sigmoide" or act == "tanh":
        print(f"Función '{act.upper()}' -> Salida continua: {resultado:.4f}")
    else:
        print(f"Función '{act.upper()}' -> Salida: {resultado}")