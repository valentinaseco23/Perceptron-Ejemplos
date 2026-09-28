class PerceptronEntrenable:
    def __init__(self, num_entradas, lr=0.1):
        self.pesos = [0.0] * num_entradas
        self.sesgo = 0.0
        self.lr = lr

    def predecir(self, x):
        z = sum(xi * wi for xi, wi in zip(x, self.pesos)) + self.sesgo
        return 1 if z >= 0 else 0

    def entrenar_con_detalle(self, X, y, nombre_compuerta, max_epocas=20):
        print(f"\n--- ENTRENANDO COMPUERTA: {nombre_compuerta} ---")
        print(f"Pesos iniciales: {self.pesos}, Sesgo inicial: {self.sesgo}")
        
        for epoca in range(1, max_epocas + 1):
            errores_en_epoca = 0
            for xi, objetivo in zip(X, y):
                prediccion = self.predecir(xi)
                error = objetivo - prediccion
                if error != 0:
                    for i in range(len(self.pesos)):
                        self.pesos[i] += self.lr * error * xi[i]
                    self.sesgo += self.lr * error
                    errores_en_epoca += abs(error)
            
            if errores_en_epoca == 0:
                print(f"¡Entrenamiento exitoso en la época {epoca}!")
                print(f"Pesos finales: {self.pesos}, Sesgo final: {self.sesgo:.2f}")
                return True
                
        print(f"Aviso: No convergió tras {max_epocas} épocas (No linealmente separable).")
        print(f"Pesos al detenerse: {self.pesos}, Sesgo: {self.sesgo:.2f}")
        return False

# Datos de entrada comunes (Tabla de verdad base)
X_datos = [[0, 0], [0, 1], [1, 0], [1, 1]]

# 6. Compuerta AND
p_and = PerceptronEntrenable(2, lr=0.1)
p_and.entrenar_con_detalle(X_datos, [0, 0, 0, 1], "AND")

# 7. Compuerta OR
p_or = PerceptronEntrenable(2, lr=0.1)
p_or.entrenar_con_detalle(X_datos, [0, 1, 1, 1], "OR")

# 8. Compuerta XOR
p_xor = PerceptronEntrenable(2, lr=0.1)
p_xor.entrenar_con_detalle(X_datos, [0, 1, 1, 0], "XOR")