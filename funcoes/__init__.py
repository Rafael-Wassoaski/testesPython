def getTemperatura():
    temperatura = float(input("Digite a temperatura: "))

    return temperatura


def toFahrenheit(celciusTemp: float):
    fahrenheitTemp = (9 * celciusTemp + 160) / 5
    return fahrenheitTemp

def celciusToFahrenheit():
    temperatura = getTemperatura()
    fahrenheitTemp = toFahrenheit(temperatura)

    print(f"Temperatura em Fahrenheit {fahrenheitTemp}")


# ///////////// 2
def getTime():
    distance: float = float(input("Digite o tempo de viagem: "))
    return distance

def getVelocity():
    velocity: float = float(input("Digite a velocidade média: "))
    return velocity

def getDistance(time: float, velocity: float):
    return time * velocity

def getConsumedFuel(distance: float = 0):
    return distance / 12

def calcConsumedFuel():
    time = getTime()
    velocity = getVelocity()
    distance = getDistance(time, velocity)

    print(f"Combustivel gasto {getConsumedFuel(distance)}")




celciusToFahrenheit()
# calcConsumedFuel()