def calculadora():
    pesetas = float(input("Introduce pesetas: "))

    def calcular(pesetas):
        euros = pesetas / 166.386
        return euros
    
    resultado = calcular(pesetas)

    print(f"El resultado es {resultado}ptas")
calculadora()