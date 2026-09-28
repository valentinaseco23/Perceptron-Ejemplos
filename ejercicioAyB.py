class PerceptronFestival:
    def __init__(self, pesos, umbral):
        self.pesos = pesos
        self.umbral = umbral

    def decidir(self, entradas):
        suma = sum(e * p for e, p in zip(entradas, self.pesos))
        return 1 if suma >= self.umbral else 0

print("=== PUNTO 2: PERCEPTRÓN DEL FESTIVAL (INTERACTIVO) ===")
try:
    c = int(input("¿Hay buen clima? (1 = Sí / 0 = No): "))
    d = int(input("¿Hay dinero? (1 = Sí / 0 = No): "))
    p = int(input("¿Va la pareja - factor clave? (1 = Sí / 0 = No): "))
    
    # Pesos del punto 2: Pareja con mayor peso [1, 1, 4] y umbral 3
    festival = PerceptronFestival(pesos=[1, 1, 4], umbral=3)
    resultado = festival.decidir([c, d, p])
    suma_total = (c * 1) + (d * 1) + (p * 4)
    
    print(f"\nSuma ponderada: {suma_total}")
    print(f"Decisión (Umbral 3): {'SÍ va al festival (1)' if resultado == 1 else 'NO va (0)'}\n")
except ValueError:
    print("Error: Ingresa solo números 0 o 1.")

print("=== PUNTO 3: TABLA DE VERDAD COMPLETA (Umbral 5 vs Umbral 3) ===")
f_u5 = PerceptronFestival(pesos=[1, 1, 2], umbral=5)
f_u3 = PerceptronFestival(pesos=[1, 1, 2], umbral=3)

print("Clima | Dinero | Pareja | Suma | Salida (Umbral=5) | Salida (Umbral=3)")
for c in [0, 1]:
    for d in [0, 1]:
        for p in [0, 1]:
            ent = [c, d, p]
            suma = sum(e * w for e, w in zip(ent, [1, 1, 2]))
            o5 = f_u5.decidir(ent)
            o3 = f_u3.decidir(ent)
            print(f"  {c}   |   {d}    |   {p}    |  {suma}   |         {o5}         |         {o3}         ")