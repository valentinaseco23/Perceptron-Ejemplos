class PerceptronMachineLearning:
    def __init__(self, num_entradas, lr=0.1):
        self.pesos = [0.0] * num_entradas
        self.sesgo = 0.0
        self.lr = lr

    def predecir(self, x):
        z = sum(xi * wi for xi, wi in zip(x, self.pesos)) + self.sesgo
        return 1 if z >= 0 else 0

    def entrenar(self, X, y, max_epocas=50):
        for epoca in range(max_epocas):
            errores = 0
            for xi, objetivo in zip(X, y):
                prediccion = self.predecir(xi)
                error = objetivo - prediccion
                if error != 0:
                    for i in range(len(self.pesos)):
                        self.pesos[i] += self.lr * error * xi[i]
                    self.sesgo += self.lr * error
                    errores += abs(error)
            if errores == 0:
                print(f"¡Modelo convergido exitosamente en la época {epoca + 1}!")
                return
        print("Aviso: Se alcanzó el máximo de épocas.")

# 1. Dataset de 6 elementos [Altura (cm), Peso (kg)]
X_basket = [
    [150, 45], [180, 75], [160, 50], 
    [190, 85], [155, 48], [185, 80]
]
y_basket = [0, 1, 0, 1, 0, 1]

# 2. Normalizamos los datos dividiendo manualmente para facilitar el cálculo del perceptrón
X_norm = [[alt / 200.0, peso / 100.0] for alt, peso in X_basket]

# 3. Instanciar y entrenar el perceptrón
modelo_ml = PerceptronMachineLearning(num_entradas=2, lr=0.1)
print("=== ENTRENANDO CLASIFICADOR DE BÁSQUET (MACHINE LEARNING) ===")
modelo_ml.entrenar(X_norm, y_basket)

# 4. Calcular la precisión sobre el propio dataset de entrenamiento
aciertos = 0
for xi, objetivo in zip(X_norm, y_basket):
    pred = modelo_ml.predecir(xi)
    if pred == objetivo:
        aciertos += 1

precision = (aciertos / len(y_basket)) * 100
print(f"\nPesos finales aprendidos: w1 (altura) = {modelo_ml.pesos[0]:.2f}, w2 (peso) = {modelo_ml.pesos[1]:.2f}")
print(f"Sesgo final: {modelo_ml.sesgo:.2f}")
print(f"Precisión obtenida en el dataset: {precision:.1f}% ({aciertos}/{len(y_basket)} aciertos)")

# 5. Prueba interactiva con una nueva persona
print("\n--- PRUEBA DE PREDICCIÓN ---")
try:
    alt_ingresada = float(input("Ingresa la altura en cm (ej. 175): "))
    peso_ingresado = float(input("Ingresa el peso en kg (ej. 70): "))
    
    entrada_usuario = [alt_ingresada / 200.0, peso_ingresado / 100.0]
    resultado_prediccion = modelo_ml.predecir(entrada_usuario)
    
    if resultado_prediccion == 1:
        print("🏀 Predicción: ¡Sí juega al básquet (1)!")
    else:
        print("🚫 Predicción: No juega al básquet (0).")
except ValueError:
    print("Error: Ingresa valores numéricos válidos.")