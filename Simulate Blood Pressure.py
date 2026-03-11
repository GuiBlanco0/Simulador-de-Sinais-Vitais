import random
import time

def ler_pressao():
    sistolica = random.gauss(120, 5)
    diastolica = random.gauss(80, 3)
    return sistolica, diastolica

def ler_temperatura():
    return random.gauss(36.8, 0.2)

def ler_oxigenacao():
    valor = random.gauss(98, 1)
    return max(90, min(valor, 100))

while True:
    sistolica, diastolica = ler_pressao()
    temperatura = ler_temperatura()
    spo2 = ler_oxigenacao()

    print(f"Pressao: {sistolica:.0f}/{diastolica:.0f} mmHg")
    print(f"Temperatura: {temperatura:.2f} C")
    print(f"Oxigenacoo (SpO2): {spo2:.1f}%")
    print("---------------------------")

    time.sleep(1)