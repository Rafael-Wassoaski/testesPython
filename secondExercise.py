
def litersPerKM(time, velocity):
    distance = time * velocity
    print(f"Listros gastos {round(distance/12,2)}")
    print(f"Tempo médio {time}")
    print(f"distancia {distance}")
    print(f"Velocidade média {velocity}")


time = float(input("Informe o tempo gasto em horas "))
velocity = float(input("Informe a velocidade média "))

litersPerKM(time, velocity)
