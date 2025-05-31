def calculadora():
    nacimiento = int(input("Cuando naciste? "))
    añoActual = int(input("En que año estamos? "))

    def calcular(nacimiento, añoActual):
        diasViviendo = (añoActual-nacimiento)*365
        return diasViviendo
    resultado = calcular(nacimiento,añoActual)
    print(f"Tienes {resultado} días vividos")
calculadora()
