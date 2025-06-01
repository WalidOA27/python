def calculadora():
    centigrados = float(input("Introduce centigrados: "))

    def calcular(centigrados):
        farenheit = centigrados * 9/5 + 32
        return farenheit
    
    resultado = calcular(centigrados)

    print(f"El resultado es {resultado} grados Farenheit")
calculadora()